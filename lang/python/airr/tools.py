"""
AIRR tools and utilities
"""

#
# tools.py
#
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
# 

import argparse
import versioneer
import airr

def main():
    """Utility commands for AIRR Community Standards files"""

    parser = argparse.ArgumentParser(add_help=False);
    parser.description='AIRR Community Standards utility commands.'

    group_help = parser.add_argument_group('help')
    group_help.add_argument('--version', action='version',
                            version='%(prog)s:' + ' %s' %(versioneer.get_version()))
    group_help.add_argument('-h', '--help', action='help', help='show this help message and exit')

    # TODO: workflow provenance
    group_prov = parser.add_argument_group('provenance')
    group_prov.add_argument('-p', '--provenance', action='store', dest='prov_file', default=None,
                              help='''File name for storing workflow provenance. If specified, airr-tools
                                   will record provenance for all activities performed.''')

    # TODO: study metadata
    group_meta = parser.add_argument_group('study metadata')
    group_meta.add_argument('-m', '--metadata', action='store', dest='metadata_file', default=None,
                            help='''File name containing study metadata.''')

    subparsers = parser.add_subparsers(title='subcommands', dest='command', metavar='',
                                       help='Database operation')
    # TODO:  This is a temporary fix for Python issue 9253
    subparsers.required = True

    # Subparser to merge files
    parser_merge = subparsers.add_parser('merge', parents=[parser],
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
    parser_merge.set_defaults(func=airr.merge)

    # Subparser to validate files
    parser_validate = subparsers.add_parser('validate', parents=[parser],
                                            add_help=False,
                                            help='Validate AIRR rearrangement files.',
                                            description='Validate AIRR rearrangement files.')
    group_validate = parser_validate.add_argument_group('validate arguments')
    group_validate.add_argument('-a', nargs='+', action='store', dest='airr_files', required=True,
                                help='A list of AIRR rearrangement files.')
    parser_validate.set_defaults(func=airr.validate)

    args = parser.parse_args()

    print(args)

    if (not args):
        args.print_help()
        sys.exit()
