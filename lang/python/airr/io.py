"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from __future__ import print_function
import sys
import csv
from airr.schema import RearrangementSchema, ValidationError


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

    def __init__(self, handle, base=1, validate=False, debug=False):
        """
        Initialization

        Arguments:
          handle (file): file handle of the open Rearrangement file.
          base (int): one of 0 or 1 specifying the coordinate schema in the input file.
                      If 1, then the file is assumed to contain 1-based closed intervals
                      that will be converted to python style 0-based half-open intervals
                      for known fields. If 0, then values will be unchanged.
          validate (bool): perform validation. If True then basic validation will be
                           performed will reading the data. A ValidationError exception
                           will be raised if an error is found.
          debug (bool): debug state. If True prints debug information.

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

    def __iter__(self):
        """
        Iterator initializer

        Returns:
          airr.io.RearrangementReader
        """
        # Validate fields
        if (self.validate):
            self.schema.validate_header(self.dict_reader.fieldnames)

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

        for f in row:
            # Convert types
            spec = self.schema.type(f)
            try:
                if spec == 'boolean':
                    row[f] = self.schema.to_bool(row[f], validate=self.validate)
                if spec == 'integer':
                    row[f] = self.schema.to_int(row[f], validate=self.validate)
                if spec == 'number':
                    row[f] = self.schema.to_float(row[f], validate=self.validate)
            except ValidationError as e:
                raise ValidationError('field %s has %s' %(f, e))

            # Adjust coordinates
            if f.endswith('_start') and self.base == 1:
                try:
                    row[f] = row[f] - 1
                except TypeError:
                    row[f] = None

        return row

    def close(self):
        """
        Closes the Rearrangement file
        """
        self.handle.close()

    def next(self):
        """
        Next method
        """
        return self.__next__()


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
                try:
                    row[f] = self.schema.to_int(row[f]) + 1
                except TypeError:
                    row[f] = None

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


