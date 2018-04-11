"""
AIRR tools and utilities
"""
# Copyright (c) 2018 AIRR Community
#
# This file is part of the AIRR Community Standards.
#
# Author: Scott Christley <schristley@mac.com>
# Author: Jason Anthony Vander Heiden
# Date: March 29, 2018
#
# This library is free software; you can redistribute it and/or modify
# it under the terms of the Creative Commons Attribution 4.0 License.
# 
# This library is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# Creative Commons Attribution 4.0 License for more details.

# Imports
import argparse
import sys
import versioneer
from collections import OrderedDict
from itertools import chain
from airr.io import RearrangementReader, RearrangementWriter


def merge(out_handle, airr_files, drop=False, debug=False):
    """
    Merge one or more AIRR rearrangements files

    Arguments:
      out_handle (file): output file handle.
      airr_files (list): list of input files to merge.
      drop (bool): drop flag. If True then drop fields that do not exist in all input
                   files, otherwise combine fields from all input files.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files were successfully merged, otherwise False.
    """
    try:
        # gather fields from input files
        readers = [RearrangementReader(open(f, 'r'), debug=debug) for f in airr_files]
        field_list = [x.fields for x in readers]
        if drop:
            field_set = set.intersection(*map(set, field_list))
        else:
            field_set = set.union(*map(set, field_list))
        field_order = OrderedDict([(f, None) for f in chain(*field_list)])
        out_fields = [f for f in field_order if f in field_set]

        out_file = RearrangementWriter(out_handle, fields=out_fields, debug=debug)

        for reader in readers:
            for rec in reader:
                out_file.write(rec)

        out_file.close()
        return True
    except:
        return False


def validate(airr_files, debug=False):
    """
    Validates one or more AIRR rearrangements files

    Arguments:
      in_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    valid = True
    for file in airr_files:
        reader = RearrangementReader(open(file, 'r'))
        valid &= reader.validate()
        # TODO: how to close file?

    return valid


def define_args():
    """
    Define commandline arguments

    Returns:
      argparse.ArgumentParser: argument parser.
    """
    parser = argparse.ArgumentParser(add_help=False,
                                     description='AIRR Community Standards utility commands.')
    group_help = parser.add_argument_group('help')
    #group_help.add_argument('--version', action='version',
    #                        version='%(prog)s:' + ' %s' %(versioneer.get_version()))
    group_help.add_argument('-h', '--help', action='help', help='show this help message and exit')

    # Setup subparsers
    subparsers = parser.add_subparsers(title='subcommands', dest='command', metavar='',
                                       help='Database operation')
    # TODO:  This is a temporary fix for Python issue 9253
    subparsers.required = True

    # Define arguments common to all subcommands
    common_parser = argparse.ArgumentParser(add_help=False)
    common_help = common_parser.add_argument_group('help')
    #common_help.add_argument('--version', action='version',
    #                        version='%(prog)s:' + ' %s' %(versioneer.get_version()))
    common_help.add_argument('-h', '--help', action='help', help='show this help message and exit')

    # TODO: workflow provenance
    group_prov = common_parser.add_argument_group('provenance')
    group_prov.add_argument('-p', '--provenance', action='store', dest='prov_file', default=None,
                              help='''File name for storing workflow provenance. If specified, airr-tools
                                   will record provenance for all activities performed.''')

    # TODO: study metadata
    group_meta = common_parser.add_argument_group('study metadata')
    group_meta.add_argument('-m', '--metadata', action='store', dest='metadata_file', default=None,
                            help='''File name containing study metadata.''')

    # Subparser to merge files
    parser_merge = subparsers.add_parser('merge', parents=[common_parser],
                                         add_help=False,
                                         help='Merge AIRR rearrangement files.',
                                         description='Merge AIRR rearrangement files.')
    group_merge = parser_merge.add_argument_group('merge arguments')
    group_merge.add_argument('-o', action='store', dest='out_file', required=True,
                              help='''Output file name.''')
    group_merge.add_argument('--drop', action='store_true', dest='drop',
                              help='''If specified, drop fields that do not exist in all input files.
                                   Otherwise, include all columns in all files and fill missing data 
                                   with empty strings.''')
    group_merge.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                             help='A list of AIRR rearrangement files.')
    parser_merge.set_defaults(func=merge)

    # Subparser to validate files
    parser_validate = subparsers.add_parser('validate', parents=[common_parser],
                                            add_help=False,
                                            help='Validate AIRR rearrangement files.',
                                            description='Validate AIRR rearrangement files.')
    group_validate = parser_validate.add_argument_group('validate arguments')
    group_validate.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                                help='A list of AIRR rearrangement files.')
    parser_validate.set_defaults(func=validate)

    return parser


def main():
    """
    Utility commands for AIRR Community Standards files
    """
    parser = define_args()
    args = parser.parse_args()

    print(args)

    if (not args):
        parser.print_help()
        sys.exit()
