"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from __future__ import print_function
import sys
import csv
from prov import model
from airr.specs import definitions


class RearrangementSchema:
    """
    Rearrangement schema definitions

    Attributes:
      properties (collections.OrderedDict): Rearrangement field definitions.
      mandatory (list): mandatory Rearrangement fields.
      optional (list): non-required Rearrangement fields.
    """
    properties = definitions['Rearrangement']['properties']
    mandatory = definitions['Rearrangement']['required']
    optional = [f for f in definitions['Rearrangement']['properties'] \
                 if f not in definitions['Rearrangement']['required']]

    @staticmethod
    def spec(field):
        """
        Get the properties for a field

        Arguments:
          name (str): field name.

        Returns:
          collections.OrderedDict: Rearrangement definition for the field.
        """
        return RearrangementSchema.properties.get(field, None)

    @staticmethod
    def type(field):
        """
        Get the type for a field

        Arguments:
          name (str): field name.

        Returns:
          str: the type definition for the field
        """
        field_spec = RearrangementSchema.properties.get(field, None)
        field_type = field_spec.get('type', None) if field_spec else None
        return field_type

    @staticmethod
    def to_bool(value):
        """
        Converts strings to boolean

        Arguments:
          value (str): logical value as a string.

        Returns:
          bool: conversion of the string to True or False.
        """
        if type(value) is bool:
            return value
        if value.upper() in [ "F", "FALSE", "NO", "N" ]:
            return False
        if value.upper() in [ "T", "TRUE", "YES", "Y" ]:
            return True

        return None

    @staticmethod
    def to_int(value):
        """
        Converts strings to integers

        Arguments:
          value (str): integer value as a string.

        Returns:
          int: conversion of the string to an integer.
        """
        if type(value) is int:
            return value
        try:
            return int(value)
        except ValueError:
            return None

    @staticmethod
    def to_float(value):
        """
        Converts strings to floats

        Arguments:
          value (str): float value as a string.

        Returns:
          float: conversion of the string to a float.
        """
        if type(value) is float:
            return value
        try:
            return float(value)
        except ValueError:
            return None


class RearrangementReader:
    """
    Iterator for reading Rearrangement objects in TSV format

    Attributes:
      fields (list): field names in the input Rearrangement file.
      external_fields (list): list of fields in the input file that are not
                              part of the Rearrangements definition.
    """
    @property
    def fields(self):
        """
        Get list of fields

        Returns:
          list : field names.
        """
        return self.dict_reader.fieldnames

    @property
    def external_fields(self):
        """
        Get list of field that are not in the Rearrangements spec

        Returns:
          list : field names.
        """
        return [f for f in self.dict_reader.fieldnames \
                if f not in RearrangementSchema.properties]

    def __init__(self, handle, debug=False):
        """
        Initialization

        Arguments:
          handle (file): file handle of the open Rearrangements file.
          debug (bool): debug state. If True prints debug information.

        Returns:
          airr.formats.RearrangementReader : reader object.
        """
        # arguments
        self.handle = handle
        self.debug = debug

        # data reader, collect field names
        self.dict_reader = csv.DictReader(self.handle, dialect='excel-tab')

    def __iter__(self):
        """
        Iterator initializer

        Returns:
          airr.formats.RearrangementReader
        """
        return self

    def __next__(self):
        """
        Next method

        Returns:
          dict: parsed Rearrangements data.
        """
        try:
            row = next(self.dict_reader)
        except StopIteration:
            self.handle.close()
            raise StopIteration

        for f in row.keys():
            spec = RearrangementSchema.type(f)
            if spec == 'boolean':  row[f] = RearrangementSchema.to_bool(row[f])
            if spec == 'integer':  row[f] = RearrangementSchema.to_int(row[f])
            if spec == 'number':  row[f] = RearrangementSchema.to_float(row[f])

        return row


class RearrangementWriter:
    """
    Writer class for Rearrangement objects in TSV format

    Attributes:
      fields (list): field names in the output Rearrangement file.
      external_fields (list): list of fields in the output file that are not
                              part of the Rearrangements definition.
    """
    @property
    def fields(self):
        """
        Get list of fields

        Returns:
          list : field names.
        """
        return self.dict_writer.fieldnames

    @property
    def external_fields(self):
        """
        Get list of field that are not in the Rearrangements spec

        Returns:
          list : field names.
        """
        return [f for f in self.dict_writer.fieldnames \
                if f not in RearrangementSchema.properties]

    def __init__(self, handle, fields=None, debug=False):
        """
        Initialization

        Arguments:
          handle (file): file handle of the open Rearrangements file.
          fields (list) : list of non-mandatory fields to add. May fields undefined by the spec.
          debug (bool): debug state. If True prints debug information.

        Returns:
          airr.formats.RearrangementWriter : writer object.
        """
        # arguments
        self.handle = handle
        self.debug = debug

        # order fields according to spec
        field_names = list(RearrangementSchema.mandatory)
        if fields is not None:
            additional_fields = []
            for f in fields:
                if f in RearrangementSchema.mandatory:
                    continue
                elif f in RearrangementSchema.optional:
                    field_names.append(f)
                else:
                    additional_fields.append(f)
            field_names.extend(additional_fields)

        # open writer and write header
        self.dict_writer = csv.DictWriter(self.handle, fieldnames=field_names,
                                          dialect='excel-tab', extrasaction='ignore')
        self.dict_writer.writeheader()

    def close(self):
        """
        Closes the Rearrangement file
        """
        self.handle.close()

    # TODO: I don't think we need this anymore
    # def addFields(self, fields):
    #     """
    #     Add fields
    #
    #     Arguments:
    #         fields (list): list of fields to add.
    #
    #     Returns:
    #       list: updated list of undefined field names in the Rearrangement file.
    #     """
    #     if isinstance(fields, str):
    #         fields = [fields]
    #
    #     for f in fields:
    #         if f not in self.additional_fields or RearrangementSchema.mandatory:
    #             self.additional_fields.append(f)
    #
    #     return self.additional_fields

    def write(self, row):
        """
        Write a row to the Rearrangement file

        Arguments:
            row (dict): row to write.
        """
        # validate row
        if self.debug:
            for field in RearrangementSchema.mandatory:
                if row.get(field, None) is None:
                    sys.stderr.write('Warning: Record is missing AIRR mandatory field (' + field + ').\n')

        self.dict_writer.writerow(row)


class MetaWriter:
    """
    Class structure for AIRR standard metadata

    Attributes:
      debug (bool): debug state. If True prints debug information.
    """

    def __init__(self, state, handle, debug=False):
        """
        Initialization

        Arguments:
          state (bool): whether the file is in a writeable state.
          handle (file): file handle of the open metadata file.

        Returns:
          airr.formats.MetaReader
        """
        self.debug = debug

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

    def close(self):
        """
        Closes the Rearrangment file
        """
        if self.dataFile:
            self.writeMetadata()
            self.dataFile.close()
            self.dataFile = None
            self.writableState = None

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
        pass

    def write(self, row):
        """
        Write a row to the Rearrangement file

        Arguments:
            row (dict): row to write.
        """
        if not self.writableState: return
        if not self.wroteMetadata: self.writeMetadata()
