"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from __future__ import print_function
import sys
import csv
from prov import model
from airr.specs import definitions


class RearrangementsFile(object):
    """
    Class structure for I/O of files containing Rearrangment object in TSV format

    Attributes:
      debug (bool): debug state. If True prints debug information.
      mandatoryFieldNames (list): list of fields required by the data standard present in the file.
      optionalSpecFieldNames (list): list of optional fields defined by the data standard present in the file.
      additionalFieldNames (list): unrecongnized fields present in the file.
      writableState (bool) : whether the file is in a writeable state.
      dataFile (file) : file handle of the open Rearrangements file.
      metaFile (file): file handle of the open metadata file.
      metaFile (prov.model.ProvDocument): metadata document.
      wroteMetadata (bool): TODO
      dictReader (csv.DictReader): file reader object.
      dictWriter (csv.DictWriter): file writer object.
    """
    def __init__(self, state, handle, debug=False):
        # set logging level. for now, just True/False to issue warnings.
        self.debug = debug

        # define fields
        self.mandatoryFieldNames = []
        self.optionalSpecFieldNames = []
        self.additionalFieldNames = []
        self._inputFieldNames = []
        for f in definitions['Rearrangement']['properties']:
            if f in definitions['Rearrangement']['required']: self.mandatoryFieldNames.append(f)
            else: self.optionalSpecFieldNames.append(f)

        # writing or reading
        if state:
            # writing
            self.writableState = state
            self.dataFile = handle
            # self.metaFile = open(handle.name + '.meta.json', 'w')
            # self.metadata = model.ProvDocument()
            # self.metadata.set_default_namespace('http://airr-community.org/')
            self.metaFile = None
            self.metadata = None
            self.wroteMetadata = False
            self.dictWriter = None
        else:
            # reading
            self.writableState = state
            self.dataFile = handle
            # try:
            #     self.metaFile = open(handle.name + '.meta.json', 'r')
            # except IOError:
            #     self.metaFile = None
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

    def specForField(self, name):
        """
        Don't know what this does...

        Arguments:
          name (str): field name.

        Returns:
          str: TODO.
        """
        for f in definitions['Rearrangement']['properties']:
            if f == name: return definitions['Rearrangement']['properties'][f]

        return None

    def convertBool(self, value):
        """
        Converts strings to boolean

        Arguments:
          value (str): logical value as a string.

        Returns:
          bool: conversion of the string to True or False.
        """
        if type(value) is bool: return value
        if value.upper() in [ "F", "FALSE", "NO", "N" ]:
            return False
        if value.upper() in [ "T", "TRUE", "YES", "Y" ]:
            return True
        return None

    def convertInt(self, value):
        """
        Converts strings to integers

        Arguments:
          value (str): integer value as a string.

        Returns:
          int: conversion of the string to an integer.
        """
        if type(value) is int: return value
        try: return int(value)
        except ValueError: return None

    def convertNumber(self, value):
        """
        Converts strings to floats

        Arguments:
          value (str): float value as a string.

        Returns:
          float: conversion of the string to a float.
        """
        if type(value) is float: return value
        try: return float(value)
        except ValueError: return None

    def close(self):
        """
        Closes the Rearrangment file
        """
        if self.dataFile:
            self.writeMetadata()
            self.dataFile.close()
            self.dataFile = None
            self.writableState = None
            self.dictWriter = None
            self.dictReader = None

    def deriveFrom(self, anObj):
        """
        Does something

        Arguments:
          anObj (TODO): TODO
        """
        # copy metadata
        if anObj.metadata:
            text = anObj.metadata.serialize(None, 'json', indent=2)
            self.metadata = model.ProvDocument.deserialize(None, text, 'json')
        # copy fields
        self.additionalFieldNames = list(anObj.additionalFieldNames)

    # metadata operations
    def addRearrangementActivity(self, inputEntity, germlineDatabase,
                                 outputEntity, toolEntity, activity):
        """
        Record provenance for original generation of Rearrangements from the V(D)J annotation tool

        Arguments:
          inputEntity (TODO): TODO
          germlineDatabase (TODO): TODO
          outputEntity (TODO): TODO
          toolEntity (TODO): TODO
          activity (TODO): TODO
        """
        if not self.metadata:
            return

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
        """
        Record provenance for original generation of rearrangements from the V(D)J annotation tool with intermediate parsing step

        Arguments:
          inputEntity (TODO): TODO
          germlineDatabase (TODO): TODO
          outputEntity (TODO): TODO
          toolEntity (TODO): TODO
          activity (TODO): TODO
          parserTool (TODO): TODO
          intermediateOutputEntity (TODO): TODO
          parseActivity (TODO): TODO
        """

        if not self.metadata:
            return None

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

    # TODO: has dead arguments
    def addAnnotationActivity(self, inputEntity, outputEntity, toolEntity,
                              activity, auxiliaryEntities, namespace,
                              namespaceURI):
        """
        Record provenance for downstream annotation tool

        Arguments:
          inputEntity (TODO): TODO
          outputEntity (TODO): TODO
          toolEntity (TODO): TODO
          activity (TODO): TODO
          auxiliaryEntities (TODO): TODO
          namespace (TODO): TODO
          namespaceURI (TODO): TODO
        """
        if not self.metadata:
            return None

        self.metadata.add_namespace(namespace, namespaceURI)
        ie = self.metadata.entity(inputEntity)
        oe = self.metadata.entity(outputEntity)
        e = self.metadata.entity(toolEntity)
        a = self.metadata.activity(activity)
        self.metadata.wasGeneratedBy(oe, a)
        self.metadata.wasDerivedFrom(oe, ie, activity=a)
        self.metadata.used(a, e)

    # TODO: does nothing
    def annotationTools(self):
        return None

    # TODO: does nothing
    def annotationToolForNamespace(self, namespace):
        return None

    # TODO: has dead arguments
    def addFields(self, namespace, names, types=None):
        """
        Add fields

        Arguments:
            namespace (str): Not used.
            names (list): list of fields to add.
            types (list): Not used.

        Returns:
          list: complete list of undefined field names in the Rearrangement file.
        """
        for name in names:
            if name in self.mandatoryFieldNames: continue
            if name not in self.additionalFieldNames: self.additionalFieldNames.append(name)
        return self.additionalFieldNames

    def writeMetadata(self):
        """
        Write metadata document
        """
        if not self.writableState: return
        if self.wroteMetadata: return
        if not self.metaFile: return
        text = self.metadata.serialize(None, 'json', indent=2)
        self.metaFile.write(text)
        self.metaFile.close()
        self.wroteMetadata = True

    def __iter__(self):
        """
        Iterator initializer

        Returns:
          airr.formats.RearrangementFile
        """
        return self

    def __next__(self):
        """
        Next method

        Returns:
          dict: parsed Rearrangements data.
        """
        if self.writableState: raise StopIteration
        row = next(self.dictReader)
        for f in row.keys():
            spec = self.specForField(f)
            if spec:
                if spec['type'] == 'boolean': row[f] = self.convertBool(row[f])
                if spec['type'] == 'integer': row[f] = self.convertInt(row[f])
                if spec['type'] == 'number': row[f] = self.convertNumber(row[f])
        return row

    # TODO: unneeded
    def next(self):
        return self.__next__()

    def write(self, row):
        """
        Write a row to the Rearrangement file

        Arguments:
            row (dict): row to write.
        """
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
