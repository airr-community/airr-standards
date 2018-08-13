"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from __future__ import print_function
import sys
import csv
from airr.schema import RearrangementSchema

class ValidationException(Exception):
    """
    Exception raised when validation errors are encountered.
    """
    pass

class RearrangementReader:
    """
    Iterator for reading Rearrangement objects in TSV format

    Attributes:
      fields (list): field names in the input Rearrangement file.
      external_fields (list): list of fields in the input file that are not
                              part of the Rearrangement definition.
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
        Get list of field that are not in the Rearrangement schema

        Returns:
          list : field names.
        """
        return [f for f in self.dict_reader.fieldnames \
                if f not in self.schema.properties]

    def __init__(self, handle, base=1, debug=False, validate=False):
        """
        Initialization

        Arguments:
          handle (file): file handle of the open Rearrangement file.
          base (int): one of 0 or 1 specifying the coordinate schema in the input file.
                      If 1, then the file is assumed to contain 1-based closed intervals
                      that will be converted to python style 0-based half-open intervals
                      for known fields. If 0, then values will be unchanged.
          debug (bool): debug state. If True prints debug information.
          validate (bool): perform validation. If True then basic validation will be
                           performed will reading the data, and ValidationException
                           will be raised if an error is found. Validation can be manually
                           performed with the validate_header and validate_row functions.

        Returns:
          airr.io.RearrangementReader: reader object.
        """
        # arguments
        self.handle = handle
        self.base = base
        self.debug = debug
        self.validate = validate
        self.schema = RearrangementSchema

        # data reader, collect field names
        self.dict_reader = csv.DictReader(self.handle, dialect='excel-tab')

        if (self.validate):
            self.validate_header()

    def __iter__(self):
        """
        Iterator initializer

        Returns:
          airr.io.RearrangementReader
        """
        return self

    def __next__(self):
        """
        Next method

        Returns:
          dict: parsed Rearrangement data.
        """
        try:
            row = next(self.dict_reader)
        except StopIteration:
            raise StopIteration

        if (self.validate):
            self.validate_row(row)

        for f in row.keys():
            # Convert types
            spec = self.schema.type(f)
            if spec == 'boolean':  row[f] = self.schema.to_bool(row[f])
            if spec == 'integer':  row[f] = self.schema.to_int(row[f])
            if spec == 'number':  row[f] = self.schema.to_float(row[f])
            # Adjust coordinates
            if f.endswith('_start') and self.base == 1:
                row[f] = row[f] - 1

        return row

    def close(self):
        """
        Closes the Rearrangement file
        """
        self.handle.close()

    def validate_header(self):
        """
        Validate Rearrangements header data against schema

        :raises: ValidationException
        """
        # check required fields
        valid = True
        missing_fields = []
        required_fields = list(self.schema.required)
        for f in required_fields:
            if f not in self.fields:
                valid = False
                missing_fields.append(f)

        if not valid:
            raise ValidationException('File is missing AIRR mandatory fields (' + ','.join(missing_fields) + ').')

    def validate_row(self, row):
        """
        Validate Rearrangements row data against schema

        :raises: ValidationException
        """
        for f in row.keys():
            # empty strings are valid
            if type(row[f]) == type('') and len(row[f]) == 0:
                continue

            # check types
            spec = self.schema.type(f)
            if spec == 'boolean':
                if self.schema.to_bool(row[f]) is None:
                    raise ValidationException(f + ' is not boolean value')
            if spec == 'integer':
                if self.schema.to_int(row[f]) is None:
                    raise ValidationException(f + ' is not integer value')
            if spec == 'number':
                if self.schema.to_float(row[f]) is None:
                    raise ValidationException(f + ' is not float value fdas')


class RearrangementWriter:
    """
    Writer class for Rearrangement objects in TSV format

    Attributes:
      fields (list): field names in the output Rearrangement file.
      external_fields (list): list of fields in the output file that are not
                              part of the Rearrangement definition.
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
        Get list of field that are not in the Rearrangements schema

        Returns:
          list : field names.
        """
        return [f for f in self.dict_writer.fieldnames \
                if f not in self.schema.properties]

    def __init__(self, handle, fields=None, base=1, debug=False):
        """
        Initialization

        Arguments:
          handle (file): file handle of the open Rearrangements file.
          fields (list) : list of non-required fields to add. May include fields undefined by the schema.
          base (int): one of 0 or 1 specifying the coordinate schema in the output file.
                      Data provided to the write is assumed to be in python style 0-based
                      half-open intervals. If 1, then data will be converted to 1-based
                      closed intervals for known fields before writing. If 0, then values will be unchanged.
          debug (bool): debug state. If True prints debug information.

        Returns:
          airr.io.RearrangementWriter: writer object.
        """
        # arguments
        self.handle = handle
        self.base = base
        self.debug = debug
        self.schema = RearrangementSchema

        # order fields according to spec
        field_names = list(self.schema.required)
        if fields is not None:
            additional_fields = []
            for f in fields:
                if f in self.schema.required:
                    continue
                elif f in self.schema.optional:
                    field_names.append(f)
                else:
                    additional_fields.append(f)
            field_names.extend(additional_fields)

        # open writer and write header
        self.dict_writer = csv.DictWriter(self.handle, fieldnames=field_names, dialect='excel-tab',
                                          extrasaction='ignore', lineterminator='\n')
        self.dict_writer.writeheader()

    def close(self):
        """
        Closes the Rearrangement file
        """
        self.handle.close()

    def write(self, row):
        """
        Write a row to the Rearrangement file

        Arguments:
            row (dict): row to write.
        """
        # validate row
        if self.debug:
            for field in self.schema.required:
                if row.get(field, None) is None:
                    sys.stderr.write('Warning: Record is missing AIRR required field (' + field + ').\n')

        for f in row.keys():
            # Adjust coordinates
            if f.endswith('_start') and self.base == 1:
                row[f] = row[f] + 1
            # Convert types
            spec = self.schema.type(f)
            if spec == 'boolean':  row[f] = self.schema.from_bool(row[f])

        self.dict_writer.writerow(row)


# TODO: pandas validation need if we load with pandas directly
# def validate_df(df, airr_schema):
#     valid = True
#
#     # check required fields
#     missing_fields = set(airr_schema.required) - set(df.columns)
#     if len(missing_fields) > 0:
#         print('Warning: file is missing mandatory fields: {}'.format(', '.join(missing_fields)))
#         valid = False
#
#     if not valid:
#         raise ValueError('invalid AIRR data file')


# class MetaWriter:
#     """
#     Class structure for AIRR standard metadata
#
#     Attributes:
#       debug (bool): debug state. If True prints debug information.
#     """
#
#     def __init__(self, state, handle, debug=False):
#         """
#         Initialization
#
#         Arguments:
#           state (bool): whether the file is in a writeable state.
#           handle (file): file handle of the open metadata file.
#
#         Returns:
#           airr.formats.MetaReader
#         """
#         self.debug = debug
#
#         # writing or reading
#         if state:
#             # writing
#             self.writableState = state
#             self.dataFile = handle
#             # self.metaFile = open(handle.name + '.meta.json', 'w')
#             # self.metadata = model.ProvDocument()
#             # self.metadata.set_default_namespace('http://airr-community.org/')
#             self.metaFile = None
#             self.metadata = None
#             self.wroteMetadata = False
#         else:
#             # reading
#             self.writableState = state
#             self.dataFile = handle
#             # try:
#             #     self.metaFile = open(handle.name + '.meta.json', 'r')
#             # except IOError:
#             #     self.metaFile = None
#             self.metaFile = None
#             self.wroteMetadata = None
#
#             # read metadata
#             self.metadata = None
#             if self.metaFile:
#                 text = self.metaFile.read()
#                 self.metaFile.close()
#                 self.metadata = model.ProvDocument.deserialize(None, text, 'json')
#
#     def close(self):
#         """
#         Closes the Rearrangment file
#         """
#         if self.dataFile:
#             self.writeMetadata()
#             self.dataFile.close()
#             self.dataFile = None
#             self.writableState = None
#
#     def deriveFrom(self, anObj):
#         """
#         Does something
#
#         Arguments:
#           anObj (TODO): TODO
#         """
#         # copy metadata
#         if anObj.metadata:
#             text = anObj.metadata.serialize(None, 'json', indent=2)
#             self.metadata = model.ProvDocument.deserialize(None, text, 'json')
#         # copy fields
#         self.additionalFieldNames = list(anObj.additionalFieldNames)
#
#     # metadata operations
#     def addRearrangementActivity(self, inputEntity, germlineDatabase,
#                                  outputEntity, toolEntity, activity):
#         """
#         Record provenance for original generation of Rearrangements from the V(D)J annotation tool
#
#         Arguments:
#           inputEntity (TODO): TODO
#           germlineDatabase (TODO): TODO
#           outputEntity (TODO): TODO
#           toolEntity (TODO): TODO
#           activity (TODO): TODO
#         """
#         if not self.metadata:
#             return
#
#         ie = self.metadata.entity('input_sequences', {'filename': inputEntity})
#         ge = self.metadata.entity(
#             'germline_database', {'name': germlineDatabase})
#         oe = self.metadata.entity('rearrangements', {'filename': outputEntity})
#         te = self.metadata.entity('rearrangement_tool', {'name': toolEntity})
#         a = self.metadata.activity(
#             'vdj_assignment', other_attributes={'name': activity})
#         self.metadata.wasGeneratedBy(oe, a)
#         self.metadata.wasDerivedFrom(oe, ie, activity=a)
#         self.metadata.used(a, ge)
#         self.metadata.used(a, te)
#
#     def addRearrangementActivityWithParser(self, inputEntity, germlineDatabase,
#                                            outputEntity, toolEntity, activity,
#                                            parserTool,
#                                            intermediateOutputEntity,
#                                            parseActivity):
#         """
#         Record provenance for original generation of rearrangements from the V(D)J annotation tool with intermediate parsing step
#
#         Arguments:
#           inputEntity (TODO): TODO
#           germlineDatabase (TODO): TODO
#           outputEntity (TODO): TODO
#           toolEntity (TODO): TODO
#           activity (TODO): TODO
#           parserTool (TODO): TODO
#           intermediateOutputEntity (TODO): TODO
#           parseActivity (TODO): TODO
#         """
#
#         if not self.metadata:
#             return None
#
#         ie = self.metadata.entity('input_sequences', {'filename': inputEntity})
#         ge = self.metadata.entity(
#             'germline_database', {'name': germlineDatabase})
#         oe = self.metadata.entity('rearrangements', {'filename': outputEntity})
#         te = self.metadata.entity('rearrangement_tool', {'name': toolEntity})
#         ra = self.metadata.activity(
#             'vdj_assignment', other_attributes={'name': activity})
#         pte = self.metadata.entity(
#             'rearrangement_tool_parser', {'name': parserTool})
#         ioe = self.metadata.entity(
#             'intermediate_vdj_assignment_output',
#             {'filename': intermediateOutputEntity})
#         pa = self.metadata.activity(
#             'parse_vdj_assignment_output',
#             other_attributes={'name': parseActivity})
#         # vdj assignment
#         self.metadata.wasGeneratedBy(ioe, ra)
#         self.metadata.wasDerivedFrom(ioe, ie, activity=ra)
#         self.metadata.used(ra, ge)
#         self.metadata.used(ra, te)
#         # parsing
#         self.metadata.wasGeneratedBy(oe, pa)
#         self.metadata.wasDerivedFrom(oe, ioe, activity=pa)
#         self.metadata.used(pa, pte)
#
#     # TODO: has dead arguments
#     def addAnnotationActivity(self, inputEntity, outputEntity, toolEntity,
#                               activity, auxiliaryEntities, namespace,
#                               namespaceURI):
#         """
#         Record provenance for downstream annotation tool
#
#         Arguments:
#           inputEntity (TODO): TODO
#           outputEntity (TODO): TODO
#           toolEntity (TODO): TODO
#           activity (TODO): TODO
#           auxiliaryEntities (TODO): TODO
#           namespace (TODO): TODO
#           namespaceURI (TODO): TODO
#         """
#         if not self.metadata:
#             return None
#
#         self.metadata.add_namespace(namespace, namespaceURI)
#         ie = self.metadata.entity(inputEntity)
#         oe = self.metadata.entity(outputEntity)
#         e = self.metadata.entity(toolEntity)
#         a = self.metadata.activity(activity)
#         self.metadata.wasGeneratedBy(oe, a)
#         self.metadata.wasDerivedFrom(oe, ie, activity=a)
#         self.metadata.used(a, e)
#
#     # TODO: does nothing
#     def annotationTools(self):
#         return None
#
#     # TODO: does nothing
#     def annotationToolForNamespace(self, namespace):
#         return None
#
#     def writeMetadata(self):
#         """
#         Write metadata document
#         """
#         if not self.writableState: return
#         if self.wroteMetadata: return
#         if not self.metaFile: return
#         text = self.metadata.serialize(None, 'json', indent=2)
#         self.metaFile.write(text)
#         self.metaFile.close()
#         self.wroteMetadata = True
#
#     def __iter__(self):
#         """
#         Iterator initializer
#
#         Returns:
#           airr.formats.RearrangementFile
#         """
#         return self
#
#     def __next__(self):
#         """
#         Next method
#
#         Returns:
#           dict: parsed Rearrangements data.
#         """
#         pass
#
#     def write(self, row):
#         """
#         Write a row to the Rearrangement file
#
#         Arguments:
#             row (dict): row to write.
#         """
#         if not self.writableState: return
#         if not self.wroteMetadata: self.writeMetadata()
