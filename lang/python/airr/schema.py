"""
AIRR Data Representation Schema
"""

# Imports
import numpy as np
import sys
import yaml
import yamlordereddictloader
from pkg_resources import resource_stream


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
        with resource_stream(__name__, 'specs/definitions.yaml') as f:
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
          collections.OrderedDict: Rearrangement definition for the field.
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

    def numpy_types(self):
        type_mapping = {}
        for property in self.properties:
            if self.type(property) == 'boolean':
                type_mapping[property] = np.bool
            elif self.type(property) == 'integer':
                type_mapping[property] = np.int64
            elif self.type(property) == 'number':
                type_mapping[property] = np.float64
            elif self.type(property) == 'string':
                type_mapping[property] = np.unicode_

        return type_mapping

    @staticmethod
    def to_bool(value):
        """
        Converts strings to boolean

        Arguments:
          value (str): logical value as a string.

        Returns:
          bool: conversion of the string to True or False.
        """
        return Schema._to_bool_map.get(value, None)

    @staticmethod
    def from_bool(value):
        """
        Converts boolean to a string

        Arguments:
          value (bool): logical value.

        Returns:
          str: conversion of True or False or 'T' or 'F'.
        """
        return Schema._from_bool_map.get(value, None)

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

# Preloaded schema
AlignmentSchema = Schema('Alignment')
RearrangementSchema = Schema('Rearrangement')
