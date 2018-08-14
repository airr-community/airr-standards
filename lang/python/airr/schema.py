"""
AIRR Data Representation Schema
"""

# Imports
import sys
import yaml
import yamlordereddictloader
from pkg_resources import resource_stream


class ValidationError(Exception):
    """
    Exception raised when validation errors are encountered.
    """
    pass


class Schema:
    """
    AIRR schema definitions

    Attributes:
      properties (collections.OrderedDict): field definitions.
      required (list): list of mandatory fields.
      optional (list): list of non-required fields.
      false_values (list): accepted string values for False.
      true_values (list): accepted values for True.
    """
    # Boolean list for pandas
    true_values = ['True', 'true', 'TRUE', 'T', 't', '1', 1, True]
    false_values = ['False', 'false', 'FALSE', 'F', 'f', '0', 0, False]

    # Generate dicts for booleans
    _to_bool_map = {x: True for x in true_values}
    _to_bool_map.update({x: False for x in false_values})
    _from_bool_map = {k: 'T' if v else 'F' for k, v in _to_bool_map.items()}
      
    def __init__(self, definition):
        """
        Initialization

        Arguments:
          definition (string): the schema definition to load.

        Returns:
          airr.schema.Schema : schema object.
        """
        # Load object definition
        with resource_stream(__name__, 'specs/airr-schema.yaml') as f:
            spec = yaml.load(f, Loader=yamlordereddictloader.Loader)

        try:
            self.definition = spec[definition]
        except KeyError:
            sys.exit('Schema definition %s cannot be found in the specifications' % definition)
        except:
            raise

        self.properties = self.definition['properties']
        self.required = self.definition['required']
        self.optional = [f for f in self.properties if f not in self.required]

    def spec(self, field):
        """
        Get the properties for a field

        Arguments:
          name (str): field name.

        Returns:
          collections.OrderedDict: definition for the field.
        """
        return self.properties.get(field, None)

    def type(self, field):
        """
        Get the type for a field

        Arguments:
          name (str): field name.

        Returns:
          str: the type definition for the field
        """
        field_spec = self.properties.get(field, None)
        field_type = field_spec.get('type', None) if field_spec else None
        return field_type

    # import numpy as np
    # def numpy_types(self):
    #     type_mapping = {}
    #     for property in self.properties:
    #         if self.type(property) == 'boolean':
    #             type_mapping[property] = np.bool
    #         elif self.type(property) == 'integer':
    #             type_mapping[property] = np.int64
    #         elif self.type(property) == 'number':
    #             type_mapping[property] = np.float64
    #         elif self.type(property) == 'string':
    #             type_mapping[property] = np.unicode_
    #
    #     return type_mapping

    def to_bool(self, value, validate=False):
        """
        Convert a string to a boolean

        Arguments:
          value (str): logical value as a string.
          validate (bool): when True raise a ValidationError for an invalid value.
                           Otherwise, set invalid values to None.

        Returns:
          bool: conversion of the string to True or False.

        Raises:
          airr.ValidationError: raised if value is invalid when validate is set True.
        """
        if value == '' or value is None:
            return None

        bool_value = self._to_bool_map.get(value, None)
        if bool_value is None and validate:
            raise ValidationError('%s is not a bool value' % value)
        else:
            return bool_value

    def from_bool(self, value, validate=False):
        """
        Converts a boolean to a string

        Arguments:
          value (bool): logical value.
          validate (bool): when True raise a ValidationError for an invalid value.
                           Otherwise, set invalid values to None.

        Returns:
          str: conversion of True or False or 'T' or 'F'.

        Raises:
          airr.ValidationError: raised if value is invalid when validate is set True.
        """
        if value == '' or value is None:
            return ''

        str_value = self._from_bool_map.get(value, None)
        if str_value is None and validate:
            raise ValidationError('%s is not a bool value' % value)
        else:
            return str_value

    def to_int(self, value, validate=False):
        """
        Converts a string to an integer

        Arguments:
          value (str): integer value as a string.
          validate (bool): when True raise a ValidationError for an invalid value.
                           Otherwise, set invalid values to None.

        Returns:
          int: conversion of the string to an integer.

        Raises:
          airr.ValidationError: raised if value is invalid when validate is set True.
        """
        if value == '' or value is None:
            return None
        if isinstance(value, int):
            return value

        try:
            return int(value)
        except ValueError:
            if validate:
                raise ValidationError('%s is not an int value' % value)
            else:
                return None

    def to_float(self, value, validate=False):
        """
        Converts a string to a float

        Arguments:
          value (str): float value as a string.
          validate (bool): when True raise a ValidationError for an invalid value.
                           Otherwise, set invalid values to None.

        Returns:
          float: conversion of the string to a float.

        Raises:
          airr.ValidationError: raised if value is invalid when validate is set True.
        """
        if value == '' or value is None:
            return None
        if isinstance(value, float):
            return value

        try:
            return float(value)
        except ValueError:
            if validate:
                raise ValidationError('%s is not a float value' % value)
            else:
                return None

    def validate_header(self, header):
        """
        Validate header against the schema

        Arguments:
          header (list): list of header fields.

        Returns:
          bool: True if a ValidationError exception is not raised.

        Raises:
          airr.ValidationError: raised if header fails validation.
        """
        # Check required fields
        missing_fields = [f for f in self.required if f not in header]

        if missing_fields:
            raise ValidationError('File is missing AIRR required fields (%s).' % ','.join(missing_fields))
        else:
            return True

    def validate_row(self, row):
        """
        Validate Rearrangements row data against schema

        Arguments:
          row (dict): dictionary containing a single record.

        Returns:
          bool: True if a ValidationError exception is not raised.

        Raises:
          airr.ValidationError: raised if row fails validation.
        """
        for f in row:
            # Empty strings are valid
            if row[f] == '' or row[f] is None:
                continue

            # Check types
            spec = self.type(f)
            try:
                if spec == 'boolean':  self.to_bool(row[f], validate=True)
                if spec == 'integer':  self.to_int(row[f], validate=True)
                if spec == 'number':  self.to_float(row[f], validate=True)
            except ValidationError as e:
                raise ValidationError('%s in field %s' %(e, f))

        return True


# Preloaded schema
AlignmentSchema = Schema('Alignment')
RearrangementSchema = Schema('Rearrangement')
