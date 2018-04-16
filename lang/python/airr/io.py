"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""
from __future__ import print_function
import sys
import csv
from airr.schema import RearrangementSchema, AlignmentSchema


_true_values =  ['True',  'true',  'TRUE',  'T', 't',
                 'Yes',   'yes',   'YES',   'Y', 'y', '1']
_false_values = ['False', 'false', 'FALSE', 'F', 'f',
                 'No',    'no',    'NO',    'N', 'n', '0']


def validate_df(df, airr_schema):
    valid = True

    # check required fields
    missing_fields = set(airr_schema.required) - set(df.columns)
    if len(missing_fields) > 0:
        print('Warning: file is missing mandatory fields: {}'.format(', '.join(missing_fields)))
        valid = False

    if not valid:
        raise ValueError('invalid AIRR data file')


def load_airr_data(filepath_or_buffer, airr_schema, **kwargs):
    df = pd.read_csv(
        filepath_or_buffer, sep='\t', header=0, index_col=None,
        dtype=airr_schema.get_numpy_type_mapping(), true_values=_true_values,
        false_values=_false_values, **kwargs)
    validate_df(df, airr_schema)
    return df


def dump_airr_data(df, path_or_buf, **kwargs):
    df.to_csv(
        path_or_buf, sep='\t', header=True, index=False, encoding='utf-8',
        **kwargs)


def load_rearrangements(filepath_or_buffer, **kwargs):
    return load_airr_data(filepath_or_buffer, RearrangementSchema, **kwargs)


def load_alignments(filepath_or_buffer, **kwargs):
    return load_airr_data(filepath_or_buffer, AlignmentSchema, **kwargs)
