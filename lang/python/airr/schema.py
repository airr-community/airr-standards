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
      info (collections.OrderedDict): schema info.
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
        # Info is not a valid schema
        if definition == 'Info':
            raise KeyError('Info is an invalid schema definition name')

        # Load object definition
        with resource_stream(__name__, 'specs/airr-schema.yaml') as f:
            spec = yaml.load(f, Loader=yamlordereddictloader.Loader)

        try:
            self.definition = spec[definition]
        except KeyError:
            raise KeyError('Schema definition %s cannot be found in the specifications' % definition)
        except:
            raise

        try:
            self.info = spec['Info']
        except KeyError:
            raise KeyError('Info object cannot be found in the specifications')
        except:
            raise

        self.properties = self.definition['properties']

        try:
            self.required = self.definition['required']
        except KeyError:
            self.required = []
        except:
            raise

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
            raise ValidationError('invalid bool %s' % value)
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
            raise ValidationError('invalid bool %s' % value)
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
                raise ValidationError('invalid int %s'% value)
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
                raise ValidationError('invalid float %s' % value)
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
        # Check for missing header
        if header is None:
            raise ValidationError('missing header')

        # Check required fields
        missing_fields = [f for f in self.required if f not in header]

        if missing_fields:
            raise ValidationError('missing required fields (%s)' % ', '.join(missing_fields))
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
                raise ValidationError('field %s has %s' %(f, e))

        return True

    def validate_object(self, obj, missing=True, nonairr = True, context=None):
        """
        Validate Repertoire object data against schema

        Arguments:
          obj (dict): dictionary containing a single repertoire object.
          missing (bool): provides warnings for missing optional fields.
          nonairr (bool: provides warning for non-AIRR fields that cannot be validated.
          context (string): used by recursion to indicate place in object hierarchy

        Returns:
          bool: True if a ValidationError exception is not raised.

        Raises:
          airr.ValidationError: raised if object fails validation.
        """

        # object has to be a dictionary
        if not isinstance(obj, dict):
            if context is None:
                raise ValidationError('object is not a dictionary')
            else:
                raise ValidationError('field %s is not a dictionary object' %(context))

        # first warn about non-AIRR fields
        if nonairr:
            for f in obj:
                if context is None: full_field = f
                else: full_field = context + '.' + f
                if self.properties.get(f) is None:
                    sys.stderr.write('Warning: Object has non-AIRR field that cannot be validated (' + full_field + ').\n')

        # now walk through schema and check types
        for f in self.properties:
            if context is None: full_field = f
            else: full_field = context + '.' + f
            spec = self.spec(f)
            xairr = spec.get('x-airr')

            # check if deprecated
            if xairr and xairr.get('deprecated'):
                continue

            # check if null and if key is missing
            is_missing_key = False
            is_null = False
            if obj.get(f) is None:
                is_null = True
                if obj.get(f, 'missing') == 'missing':
                    is_missing_key = True

            # check MiAIRR keys exist
            if xairr and xairr.get('miairr'):
                if is_missing_key:
                    raise ValidationError('MiAIRR field %s is missing' %(full_field))

            # check if required field
            if f in self.required and is_missing_key:
                raise ValidationError('Required field %s is missing' %(full_field))

            # check if identifier field
            if xairr and xairr.get('identifier'):
                if is_missing_key:
                    raise ValidationError('Identifier field %s is missing' %(full_field))

            # check nullable requirements
            if is_null:
                if not xairr:
                    # default is true
                    continue
                if xairr.get('nullable') or xairr.get('nullable', 'missing') == 'missing':
                    # nullable is allowed
                    continue
                else:
                    # nullable not allowed
                    raise ValidationError('Non-nullable field %s is null or missing' %(full_field))

            # if get to here, field should exist with non null value

            # check types
            field_type = self.type(f)
            if field_type is None:
                # for referenced object, recursively call validate with object and schema
                if spec.get('$ref') is not None:
                    schema_name = spec['$ref'].split('/')[-1]
                    if CachedSchema.get(schema_name):
                        schema = CachedSchema[schema_name]
                    else:
                        schema = Schema(schema_name)
                    schema.validate_object(obj[f], missing, nonairr, full_field)
                else:
                    raise ValidationError('Internal error: field %s in schema not handled by validation. File a bug report.' %(full_field))
            elif field_type == 'array':
                if not isinstance(obj[f], list):
                    raise ValidationError('field %s is not an array' %(full_field))

                # for array, check each object in it
                for row in obj[f]:
                    if spec['items'].get('$ref') is not None:
                        schema_name = spec['items']['$ref'].split('/')[-1]
                        schema = Schema(schema_name)
                        schema.validate_object(row, missing, nonairr, full_field)
                    elif spec['items'].get('allOf') is not None:
                        for s in spec['items']['allOf']:
                            if s.get('$ref') is not None:
                                schema_name = s['$ref'].split('/')[-1]
                                if CachedSchema.get(schema_name):
                                    schema = CachedSchema[schema_name]
                                else:
                                    schema = Schema(schema_name)
                                schema.validate_object(row, missing, False, full_field)
                    elif spec['items'].get('enum') is not None:
                        if row not in spec['items']['enum']:
                            raise ValidationError('field %s has value "%s" not among possible enumeration values' %(full_field, row))
                    elif spec['items'].get('type') == 'string':
                        if not isinstance(row, str):
                            raise ValidationError('array field %s does not have string type: %s' %(full_field, row))
                    elif spec['items'].get('type') == 'boolean':
                        if not isinstance(row, bool):
                            raise ValidationError('array field %s does not have boolean type: %s' %(full_field, row))
                    elif spec['items'].get('type') == 'integer':
                        if not isinstance(row, int):
                            raise ValidationError('array field %s does not have integer type: %s' %(full_field, row))
                    elif spec['items'].get('type') == 'number':
                        if not isinstance(row, float) and not isinstance(row, int):
                            raise ValidationError('array field %s does not have number type: %s' %(full_field, row))
                    else:
                        raise ValidationError('Internal error: array field %s in schema not handled by validation. File a bug report.' %(full_field))
            elif field_type == 'object':
                # right now all arrays of objects use $ref
                raise ValidationError('Internal error: field %s in schema not handled by validation. File a bug report.' %(full_field))
            else:
                # check basic types
                if field_type == 'string':
                    if not isinstance(obj[f], str):
                        raise ValidationError('Field %s does not have string type: %s' %(full_field, obj[f]))
                elif field_type == 'boolean':
                    if not isinstance(obj[f], bool):
                        raise ValidationError('Field %s does not have boolean type: %s' %(full_field, obj[f]))
                elif field_type == 'integer':
                    if not isinstance(obj[f], int):
                        raise ValidationError('Field %s does not have integer type: %s' %(full_field, obj[f]))
                elif field_type == 'number':
                    if not isinstance(obj[f], float) and not isinstance(obj[f], int):
                        raise ValidationError('Field %s does not have number type: %s' %(full_field, obj[f]))
                else:
                    raise ValidationError('Internal error: Field %s with type %s in schema not handled by validation. File a bug report.' %(full_field, field_type))

        return True


# Preloaded schema
CachedSchema = {
    'Alignment': Schema('Alignment'),
    'Rearrangement': Schema('Rearrangement'),
    'Repertoire': Schema('Repertoire'),
    'Ontology': Schema('Ontology'),
    'Study': Schema('Study'),
    'Subject': Schema('Subject'),
    'Diagnosis': Schema('Diagnosis'),
    'CellProcessing': Schema('CellProcessing'),
    'PCRTarget': Schema('PCRTarget'),
    'NucleicAcidProcessing': Schema('NucleicAcidProcessing'),
    'SequencingRun': Schema('SequencingRun'),
    'RawSequenceData': Schema('RawSequenceData'),
    'DataProcessing': Schema('DataProcessing'),
    'SampleProcessing': Schema('SampleProcessing')
}

AlignmentSchema = CachedSchema['Alignment']
RearrangementSchema = CachedSchema['Rearrangement']
RepertoireSchema = CachedSchema['Repertoire']

