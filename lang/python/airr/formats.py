"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from __future__ import print_function
import re

from prov import model

from airr.specs import rearrangements


class RearrangementsFile(object):

    def __init__(self, filename, state):
        if state:
            self.writableState = state
            self.dataFile = open(filename, 'w')
            self.metadata = model.ProvDocument()
            self.metadata.set_default_namespace('http://airr-community.org/')
            self.wroteMetadata = False
            self.fieldNames = list(rearrangements['mandatory'])
        else:
            self.writableState = state
            self.dataFile = open(filename, 'r')
            self.wroteMetadata = None
            # read metadata
            header = None
            done = False
            text = ''
            while not done:
                line = self.dataFile.readline()
                m = re.match('^#M', line)
                if m: text += re.sub('^#M', '', line)
                else:
                    done = True
                    header = line.rstrip('\n')
            if len(text) > 0:
                self.metadata = model.ProvDocument.deserialize(
                    None, text, 'json')
            if not header: header = self.dataFile.readline().rstrip('\n')
            self.fieldNames = header.split('\t')

    # document operations
    def close(self):
        if self.dataFile:
            self.writeMetadata()
            self.dataFile.close()
            self.dataFile = None
            self.writableState = None

    def deriveFrom(self, anObj):
        # copy metadata
        text = anObj.metadata.serialize(None, 'json', indent=2)
        self.metadata = model.ProvDocument.deserialize(None, text, 'json')
        # copy fields
        self.fieldNames = list(anObj.fieldNames)

    # metadata operations
    def addRearrangementActivity(self, inputEntity, germlineDatabase,
                                 outputEntity, toolEntity, activity):
        """Record provenance for original generation of rearrangements from the
        VDJ assignment tool
        """
        ie = self.metadata.entity('input_sequences', {'filename': inputEntity})
        ge = self.metadata.entity(
            'germline_database', {'name': germlineDatabase})
        oe = self.metadata.entity('rearrangements', {'filename': outputEntity})
        te = self.metadata.entity('rearrangement_tool', {'name': toolEntity})
        a = self.metadata.activity(
            'vdj_assignment', other_attributes={'name': activity})
        self.metadata.wasGeneratedBy(oe, a)
        self.metadata.wasDerivedFrom(oe, ie, activity=a)
        self.metadata.used(a, ge)
        self.metadata.used(a, te)

    def addRearrangementActivityWithParser(self, inputEntity, germlineDatabase,
                                           outputEntity, toolEntity, activity,
                                           parserTool,
                                           intermediateOutputEntity,
                                           parseActivity):
        """Record provenance for original generation of rearrangements from the
        VDJ assignment tool with intermediate parsing step
        """
        ie = self.metadata.entity('input_sequences', {'filename': inputEntity})
        ge = self.metadata.entity(
            'germline_database', {'name': germlineDatabase})
        oe = self.metadata.entity('rearrangements', {'filename': outputEntity})
        te = self.metadata.entity('rearrangement_tool', {'name': toolEntity})
        ra = self.metadata.activity(
            'vdj_assignment', other_attributes={'name': activity})
        pte = self.metadata.entity(
            'rearrangement_tool_parser', {'name': parserTool})
        ioe = self.metadata.entity(
            'intermediate_vdj_assignment_output',
            {'filename': intermediateOutputEntity})
        pa = self.metadata.activity(
            'parse_vdj_assignment_output',
            other_attributes={'name': parseActivity})
        # vdj assignment
        self.metadata.wasGeneratedBy(ioe, ra)
        self.metadata.wasDerivedFrom(ioe, ie, activity=ra)
        self.metadata.used(ra, ge)
        self.metadata.used(ra, te)
        # parsing
        self.metadata.wasGeneratedBy(oe, pa)
        self.metadata.wasDerivedFrom(oe, ioe, activity=pa)
        self.metadata.used(pa, pte)

    def addAnnotationActivity(self, inputEntity, outputEntity, toolEntity,
                              activity, auxiliaryEntities, namespace,
                              namespaceURI):
        """Record provenance for downstream annotation tool"""
        self.metadata.add_namespace(namespace, namespaceURI)
        ie = self.metadata.entity(inputEntity)
        oe = self.metadata.entity(outputEntity)
        e = self.metadata.entity(toolEntity)
        a = self.metadata.activity(activity)
        self.metadata.wasGeneratedBy(oe, a)
        self.metadata.wasDerivedFrom(oe, ie, activity=a)
        self.metadata.used(a, e)

    def annotationTools(self):
        return None

    def annotationToolForNamespace(self, namespace):
        return None

    def addFields(self, namespace, names):
        for name in names:
            if name not in self.fieldNames: self.fieldNames.append(name)
        return self.fieldNames

    def writeMetadata(self):
        if not self.writableState: return
        if self.wroteMetadata: return
        text = self.metadata.serialize(None, 'json', indent=2)
        lines = text.split('\n')
        for line in lines:
            self.dataFile.write('#M ' + line + '\n')
        self.dataFile.write('\t'.join(self.fieldNames) + '\n')
        self.wroteMetadata = True

    # row operations
    def __iter__(self):
        return self

    def __next__(self):
        if self.writableState: raise StopIteration
        line = self.dataFile.readline().rstrip('\n')
        if not line: raise StopIteration
        fields = line.split('\t')
        if len(fields) != len(self.fieldNames):
            print("Incorrect number of fields in row.")
            return None
        return dict(zip(self.fieldNames, fields))

    def next(self):
        return self.__next__()

    def write(self, row):
        if not self.writableState: return
        if not self.wroteMetadata: self.writeMetadata()
        # validate row?
        first = True
        for field in self.fieldNames:
            if not first: self.dataFile.write('\t')
            first = False
            value = row.get(field)
            if value: self.dataFile.write(value)
        self.dataFile.write('\n')
