"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from __future__ import print_function
import re
import sys
import csv

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
        self.optionalSpecFieldNames = []
        self.additionalFieldNames = []
        self._inputFieldNames = []
        for f in rearrangements['fields']:
            if f['mandatory']: self.mandatoryFieldNames.append(f['name'])
            else: self.optionalSpecFieldNames.append(f['name'])

        # writing or reading
        if state:
            # writing
            self.writableState = state
            if filename:
                self.dataFile = open(filename, 'w')
                self.metaFile = open(filename + '.meta.json', 'w')
            else:
                self.dataFile = handle
                self.metaFile = open(handle.name + '.meta.json', 'w')
            self.metadata = model.ProvDocument()
            self.metadata.set_default_namespace('http://airr-community.org/')
            self.wroteMetadata = False
            self.dictWriter = None
        else:
            # reading
            self.writableState = state
            if filename:
                self.dataFile = open(filename, 'r')
                try:
                    self.metaFile = open(filename + '.meta.json', 'r')
                except IOError:
                    self.metaFile = None
            else:
                self.dataFile = handle
                try:
                    self.metaFile = open(handle.name + '.meta.json', 'r')
                except IOError:
                    self.metaFile = None
            self.wroteMetadata = None

            # read metadata
            self.metadata = None
            if self.metaFile:
                text = self.metaFile.read()
                self.metaFile.close()
                self.metadata = model.ProvDocument.deserialize(None, text, 'json')

            # data reader, collect field names
            self.dictReader = csv.DictReader(self.dataFile, dialect='excel-tab')
            self._inputFieldNames = self.dictReader.fieldnames
            for f in self._inputFieldNames:
                if f in self.mandatoryFieldNames: continue
                if f not in self.additionalFieldNames: self.additionalFieldNames.append(f)

    # utility operations
    def specForField(self, name):
        for f in rearrangements['fields']:
            if f['name'] == name: return f
        return None

    def convertBool(self, value):
        if type(value) is bool: return value
        if value.upper() in [ "F", "FALSE", "NO", "N" ]:
            return False
        if value.upper() in [ "T", "TRUE", "YES", "Y" ]:
            return True
        return None

    def convertInt(self, value):
        if type(value) is int: return value
        try: return int(value)
        except ValueError: return None

    def convertNumber(self, value):
        if type(value) is float: return value
        try: return float(value)
        except ValueError: return None

    # document operations
    def close(self):
        if self.dataFile:
            self.writeMetadata()
            self.dataFile.close()
            self.dataFile = None
            self.writableState = None
            self.dictWriter = None
            self.dictReader = None

    def deriveFrom(self, anObj):
        # copy metadata
        if anObj.metadata:
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
        if not self.metadata: return
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
        if not self.metadata: return
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
        if not self.metadata: return
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

    def addFields(self, namespace, names, types=None):
        for name in names:
            if name in self.mandatoryFieldNames: continue
            if name not in self.additionalFieldNames: self.additionalFieldNames.append(name)
        return self.additionalFieldNames

    def writeMetadata(self):
        if not self.writableState: return
        if self.wroteMetadata: return
        if not self.metaFile: return
        text = self.metadata.serialize(None, 'json', indent=2)
        self.metaFile.write(text)
        self.metaFile.close()
        self.wroteMetadata = True

    # row operations
    def __iter__(self):
        return self

    def __next__(self):
        if self.writableState: raise StopIteration
        row = next(self.dictReader)
        for f in row.keys():
            spec = self.specForField(f)
            if spec:
                if spec['type'] == 'boolean': row[f] = self.convertBool(row[f])
                if spec['type'] == 'integer': row[f] = self.convertInt(row[f])
                if spec['type'] == 'number': row[f] = self.convertNumber(row[f])
        return row

    def next(self):
        return self.__next__()

    def write(self, row):
        if not self.writableState: return
        if not self.wroteMetadata: self.writeMetadata()

        if not self.dictWriter:
            fieldNames = []
            fieldNames.extend(self.mandatoryFieldNames)
            # order according to spec
            olist = []
            alist = []
            for f in self.optionalSpecFieldNames:
                if f in self.additionalFieldNames: olist.append(f)
            for f in self.additionalFieldNames:
                if f not in self.optionalSpecFieldNames: alist.append(f)
            self.additionalFieldNames = olist
            self.additionalFieldNames.extend(alist)
            fieldNames.extend(self.additionalFieldNames)
            self.dictWriter = csv.DictWriter(self.dataFile, fieldnames=fieldNames, dialect='excel-tab', extrasaction='ignore')
            self.dictWriter.writeheader()

        # validate row?
        for field in self.mandatoryFieldNames:
            value = row.get(field, None)
            if value is None:
                if self.debug:
                    sys.stderr.write('Warning: Record is missing AIRR mandatory field (' + field + ').\n')

        self.dictWriter.writerow(row)
