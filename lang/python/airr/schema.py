"""
AIRR Data Representation Schema
"""

import sys

import yaml
import numpy as np
from pkg_resources import resource_stream


with resource_stream(__name__, 'specs/definitions.yaml') as f:
    spec = yaml.load(f, Loader=yamlordereddictloader.Loader)


class Schema(object):
    """
    AIRR schema helper object

    Attributes:
      data (dict): complete schema.
      properties (dict): field definitions.
      required (list): list of mandatory fields.
    """
    def __init__(self, spec):
        """
        Initialization

        Arguments:
          spec (dict): the schema data

        Returns:
          airr.schema.Schema : schema helper object.
        """
        self.data = spec
        self.properties = self.data['properties']
        self.required = self.data['required']

    def get_property(self, property):
        """
        Get the properties for a field

        Arguments:
          property (str): field name.

        Returns:
          dict: definition for the field.
        """
        return self.properties.get(field, None)


    def get_type(self, property):
        """
        Get the type for a field

        Arguments:
          name (str): field name.

        Returns:
          str: the type definition for the field
        """
        return self.get_property(property)['type']

    def get_numpy_type_mapping(self):
        type_mapping = {}
        for property in self.properties:
            if self.get_type(property) == 'boolean':
                type_mapping[property] = np.bool
            elif self.get_type(property) == 'integer':
                type_mapping[property] = np.int64
            elif self.get_type(property) == 'number':
                type_mapping[property] = np.float64
        return type_mapping


# Preloaded schema
AlignmentSchema = Schema(spec['Alignment'])
RearrangementSchema = Schema(spec['Rearrangement'])
