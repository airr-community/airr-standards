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

# System imports
import argparse
import sys
from warnings import warn

# Local imports
from airr import __version__
import airr.interface

# internal wrapper function before calling merge interface method
def merge_cmd(out_file, airr_files, drop=False, debug=False):
    """
    Merge one or more AIRR rearrangements files

    Arguments:
      out_file (str): output file name.
      airr_files (list): list of input files to merge.
      drop (bool): drop flag. If True then drop fields that do not exist in all input
                   files, otherwise combine fields from all input files.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      bool: True if files were successfully merged, otherwise False.
    """
    return airr.interface.merge_rearrangement(out_file, airr_files, drop=drop, debug=debug)

# internal wrapper function before calling validate interface method
def validate_rearrangement_cmd(airr_files, debug=True):
    """
    Validates one or more AIRR rearrangements files

    Arguments:
      airr_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    valid = []
    for f in airr_files:
        try:
            v = airr.interface.validate_rearrangement(f, debug=debug)
            valid.append(v)
        except Exception as e:
            sys.stderr.write('%s\n' % e)
            sys.stderr.write('Validation failed for file: %s\n\n' % f)
            valid.append(False)
        else:
            if not v:  sys.stderr.write('Validation failed for file: %s\n\n' % f)

    return all(valid)

def validate_airr_cmd(airr_files, debug=True):
    """
    Validates one or more AIRR Data Model files

    Arguments:
      airr_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    valid = []
    for f in airr_files:
        if debug: sys.stderr.write('Validating: %s\n' % f)
        try:
            data = airr.interface.read_airr(f, validate=False, debug=debug)
            v = airr.interface.validate_airr(data, debug=debug)
            valid.append(v)
        except Exception as e:
            sys.stderr.write('%s\n' % e)
            sys.stderr.write('Validation failed for file: %s\n\n' % f)
            valid.append(False)

    return all(valid)

#### Deprecated ####

# internal wrapper function before calling validate interface method
def validate_repertoire_cmd(airr_files, debug=True):
    """
    Validates one or more AIRR repertoire metadata files

    Arguments:
      airr_files (list): list of input files to validate.
      debug (bool): debug flag. If True print debugging information to standard error.

    Returns:
      boolean: True if all files passed validation, otherwise False
    """
    # Deprecation
    warn('validate_repertoire_cmd is deprecated and will be removed in a future release.\nUse =validate_airr_cmd instead.\n',
         DeprecationWarning, stacklevel=2)

    valid = []
    for f in airr_files:
        try:
            v = airr.interface.validate_repertoire(f, debug=debug)
            valid.append(v)
        except Exception as e:
            sys.stderr.write('%s\n' % e)
            sys.stderr.write('Validation failed for file: %s\n\n' % f)
            valid.append(False)

    return all(valid)

def define_args():
    """
    Define commandline arguments

    Returns:
      argparse.ArgumentParser: argument parser.
    """
    parser = argparse.ArgumentParser(add_help=False,
                                     description='AIRR Community Standards utility commands.')
    group_help = parser.add_argument_group('help')
    group_help.add_argument('-h', '--help', action='help', help='show this help message and exit')
    group_help.add_argument('--version', action='version',
                            version='%(prog)s:' + ' %s' % __version__)

    # Setup subparsers
    subparsers = parser.add_subparsers(title='subcommands', dest='command', metavar='',
                                       help='Database operation')
    # TODO:  This is a temporary fix for Python issue 9253
    subparsers.required = True

    # Define arguments common to all subcommands
    common_parser = argparse.ArgumentParser(add_help=False)
    common_help = common_parser.add_argument_group('help')
    common_help.add_argument('--version', action='version',
                             version='%(prog)s:' + ' %s' % __version__)
    common_help.add_argument('-h', '--help', action='help', help='show this help message and exit')

    # TODO: workflow provenance
    # group_prov = common_parser.add_argument_group('provenance')
    # group_prov.add_argument('-p', '--provenance', action='store', dest='prov_file', default=None,
    #                           help='''File name for storing workflow provenance. If specified, airr-tools
    #                                will record provenance for all activities performed.''')

    # TODO: study metadata
    # group_meta = common_parser.add_argument_group('study metadata')
    # group_meta.add_argument('-m', '--metadata', action='store', dest='metadata_file', default=None,
    #                         help='''File name containing study metadata.''')

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
    parser_merge.set_defaults(func=merge_cmd)

    # Subparser to validate files
    parser_validate = subparsers.add_parser('validate', parents=[common_parser],
                                            add_help=False,
                                            help='Validate files for AIRR Standards compliance.',
                                            description='Validate files for AIRR Standards compliance.')
    validate_subparser = parser_validate.add_subparsers(title='subcommands', metavar='',
                                       help='Database operation')

    # Subparser to validate rearrangement files
    parser_validate = validate_subparser.add_parser('rearrangement', parents=[common_parser],
                                            add_help=False,
                                            help='Validate AIRR rearrangement files.',
                                            description='Validate AIRR rearrangement files.')
    group_validate = parser_validate.add_argument_group('validate arguments')
    group_validate.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                                help='A list of AIRR rearrangement files.')
    parser_validate.set_defaults(func=validate_rearrangement_cmd)

    # Subparser to validate AIRR Data Model files
    parser_validate = validate_subparser.add_parser('airr', parents=[common_parser],
                                            add_help=False,
                                            help='Validate AIRR Data Model files.',
                                            description='Validate AIRR Data Model files.')
    group_validate = parser_validate.add_argument_group('validate arguments')
    group_validate.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                                help='A list of AIRR Data Model files.')
    parser_validate.set_defaults(func=validate_airr_cmd)

    # Subparser to validate repertoire files
    parser_validate = validate_subparser.add_parser('repertoire', parents=[common_parser],
                                                    add_help=False,
                                                    help='Validate AIRR repertoire metadata files.',
                                                    description='Validate AIRR repertoire metadata files.')
    group_validate = parser_validate.add_argument_group('validate arguments')
    group_validate.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                                help='A list of AIRR repertoire metadata files.')
    parser_validate.set_defaults(func=validate_repertoire_cmd)

    return parser


def main():
    """
    Utility commands for AIRR Community Standards files
    """
    # Define argument parsers and print help if subcommand not specified
    parser = define_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # Parse arguments
    args = parser.parse_args()
    args_dict = args.__dict__.copy()
    del args_dict['command']
    del args_dict['func']

    # Deprecation warnings
    if args.func is validate_repertoire_cmd:
        print('The "validate repertoire" subcommand is deprecated and will be removed in a future release.',
              '\nUse the "validate airr" subcommand instead.\n')

    # Call tool function
    result = args.func(**args_dict)

    # set return code to non-zero if error occurred
    if args.__dict__['command'] == 'validate' or args.__dict__['command'] == 'merge':
        if not result:
            sys.exit(1)
