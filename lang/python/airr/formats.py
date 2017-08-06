"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from __future__ import print_function
import re
import sys

from prov import model

from airr.specs import rearrangements


class RearrangementsFile(object):

    def __init__(self, state, filename=None, handle=None, debug=False):
        if not filename and not handle:
            sys.exit("Error: filename or handle must be provided to RearrangementsFile\n")
            return None

        # set logging level. for now, just True/False to issue warnings.
        self.debug = debug

        # define fields
        self.mandatoryFieldNames = []
        self.optionalFieldNames = []
        self.additionalFieldNames = []
        self._inputFieldNames = []
        for f in rearrangements['fields']:
            if f['mandatory']: self.mandatoryFieldNames.append(f['name'])
            else: self.optionalFieldNames.append(f['name'])

        if state:
            self.writableState = state
            if filename:
                self.dataFile = open(filename, 'w')
            else:
                self.dataFile = handle
            self.metadata = model.ProvDocument()
            self.metadata.set_default_namespace('http://airr-community.org/')
            self.wroteMetadata = False
        else:
            self.writableState = state
            if filename:
                self.dataFile = open(filename, 'r')
            else:
                self.dataFile = handle
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
            self._inputFieldNames = header.split('\t')
            for f in self._inputFieldNames:
                if f in self.mandatoryFieldNames: continue
                if f in self.optionalFieldNames: continue
                if f not in self.additionalFieldNames: self.additionalFieldNames.append(f)

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
        self.additionalFieldNames = list(anObj.additionalFieldNames)

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
            if name in self.mandatoryFieldNames: continue
            if name in self.optionalFieldNames: continue
            if name not in self.additionalFieldNames: self.additionalFieldNames.append(name)
        return self.additionalFieldNames

    def writeMetadata(self):
        if not self.writableState: return
        if self.wroteMetadata: return
        text = self.metadata.serialize(None, 'json', indent=2)
        lines = text.split('\n')
        for line in lines:
            self.dataFile.write('#M ' + line + '\n')
        # write headers after metadata
        self.dataFile.write('\t'.join(self.mandatoryFieldNames))
        if len(self.optionalFieldNames) > 0:
            self.dataFile.write('\t' + '\t'.join(self.optionalFieldNames))
        if len(self.additionalFieldNames) > 0:
            self.dataFile.write('\t' + '\t'.join(self.additionalFieldNames))
        self.dataFile.write('\n')
        self.wroteMetadata = True

    # row operations
    def __iter__(self):
        return self

    def __next__(self):
        if self.writableState: raise StopIteration
        line = self.dataFile.readline().rstrip('\n')
        if not line: raise StopIteration
        fields = line.split('\t')
        return dict(zip(self._inputFieldNames, fields))

    def next(self):
        return self.__next__()

    def write(self, row):
        if not self.writableState: return
        if not self.wroteMetadata: self.writeMetadata()

        # validate row?
        first = True
        for field in self.mandatoryFieldNames:
            if not first: self.dataFile.write('\t')
            first = False
            value = row.get(field, None)
            if value is not None:
                self.dataFile.write(str(value))
            else:
                self.dataFile.write('')
                if self.debug:
                    sys.stderr.write('Warning: Record is missing AIRR mandatory field (' + field + ').\n')

        for field in self.optionalFieldNames:
            if not first: self.dataFile.write('\t')
            first = False
            value = row.get(field, '')
            self.dataFile.write(str(value))

        for field in self.additionalFieldNames:
            if not first: self.dataFile.write('\t')
            first = False
            value = row.get(field, '')
            self.dataFile.write(str(value))

        self.dataFile.write('\n')
