#!/usr/bin/env python3

"""
@franasa - f.arcila@dkfz-heidelberg.de

DESCRIPTION
create a tsv file from airr-schema.yaml

"""

try:
    import pandas as pd
except ImportError:
    import pip
    pip.main(["install", "--user", "pandas"])
    import pandas as pd

try:
    import yaml
except ImportError:
    import pip
    pip.main(["install", "--user", "yaml"])
    import yaml

import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=RawTextHelpFormatter)
parser.add_argument("-y", "--yaml_file", required=True, help="define input file")
parser.add_argument("-p", "--output_path_tsv", required=True, help="output file path")
args = parser.parse_args()

yaml_file = args.yaml_file

to_DF = []

# Open yaml file
with open(yaml_file, "r") as stream:
    airr_stream = (yaml.safe_load(stream))

# iterate over first level of yaml items
for key, v in airr_stream.items():
    # iterate over second level of yaml items
    for k, v in airr_stream[key].items():
        # get properties
        if "properties" in k:
            for airr_property, v in airr_stream[key][k].items():

                # get only miairr properties
                if "miairr" in str(v) and airr_stream[
                        key][k][airr_property]["x-airr"]["miairr"] == True:
                    # print (airr_stream[key][k][airr_property])

                    if "type" in v:  # get type
                        airr_data_type = airr_stream[key][k][airr_property]["type"]

                    if "example" in v:
                        airr_field_value_example = airr_stream[key][k][airr_property]["example"]

                    if "description" in v:
                        airr_description = airr_stream[key][k][airr_property]["description"]

                    if "set" in airr_stream[key][k][airr_property]["x-airr"]:
                        airr_set = airr_stream[key][k][airr_property]["x-airr"]["set"]

                    if "subset" in airr_stream[key][k][airr_property]["x-airr"]:
                        airr_subset = airr_stream[key][k][airr_property]["x-airr"]["subset"]

                    if "name" in airr_stream[key][k][airr_property]["x-airr"]:
                        airr_name = airr_stream[key][k][airr_property]["x-airr"]["name"]

                    to_DF.append([airr_set,airr_subset, airr_name,
                                  airr_data_type, airr_description, "Content format",
                                  airr_field_value_example, airr_property])


# columns defined as in current /airr-standards/AIRR_Minimal_Standard_Data_Elements.tsv
airr_dataframe = pd.DataFrame(to_DF, columns=["MiAIRR data set", "subset",
                                              "MiAIRR field designation",
                                              "Data type",
                                              "Content format", # not equivalent found on current yaml file
                                              "MiAIRR content definition",
                                              "Field value example",
                                              "AIRR Formats WG field name"])


airr_dataframe.to_csv(args.output_path_tsv, sep="\t", index=False)

print(" File {}  has been created".format(args.output_path_tsv))
