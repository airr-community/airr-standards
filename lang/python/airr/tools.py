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

# Local imports
from airr import __version__
from airr.interface import merge, validate

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

    # Call tool function
    args.func(**args_dict)

