#
# ADC API Example
# retrieve_data.py
#
# Author: Scott Christley
# Date: July 26, 2019
#
# This example code shows how repertoires and associated rearrangments
# may be queried from a data repository. The retrieved data is stored
# in files using the AIRR standards python library. A separate script
# reads the data and performs some simple analysis.
#
# Repertoire output file: repertoires.airr.json
# Rearrangement output file: rearrangements.tsv
#
# We could have written the example to perform the data retrieval and
# analysis in a single script, but we wanted to show the data could be
# saved into files for later use.
#
# This script retrieves data for the following study, which is identified
# by NCBI BioProject PRJNA300878. In this example, we are only going to
# query and retrieve the T cell repertoires.
#
# Rubelt, F. et al., 2016. Individual heritable differences result in
# unique cell lymphocyte receptor repertoires of naive and
# antigen-experienced cells. Nature communications, 7, p.11112.
#
# Basic study description:
# 5 pairs of human twins
# B-cells and T-cells sequenced
# B-cells sorted into naive and memory
# T-cells sorted into naive CD4, naive CD8, memory CD4 and memory CD8
# total of 60 repertoires
# 

import json
import airr
import requests

# This study is stored at VDJServer data repository
host_url='https://vdjserver.org/airr/v1'

#
# Query the repertoire endpoint
#

# POST data is sent with the query. Here we construct an object for
# the query ((study_id == "PRJNA300878") AND (locus == "TRB"))

query = {
    "filters":{
        "op":"and",
        "content": [
            {
                "op":"=",
                "content": {
                    "field":"study.study_id",
                    "value":"PRJNA300878"
                }
	    },
	    {
                "op":"=",
                "content": {
                    "field":"sample.pcr_target.pcr_target_locus",
                    "value":"TRB"
                }
	    }
	]
    }
}

# Send the query
resp = requests.post(host_url + '/repertoire', json = query)

# The data is returned as JSON, use AIRR library to write out data
data = resp.json()
airr.write_airr('repertoires.airr.json', data, info=data['Info'])
repertoires = data['Repertoire']

# Print out some Info
print('       Info: ' + data['Info']['title'])
print('    version: ' + str(data['Info']['version']))
print('description: ' + data['Info']['description'])

# There should be 40 repertoires
# Save them out to a file
print('Received ' + str(len(data['Repertoire'])) + ' repertoires.')

#
# Query the rearrangement endpoint
#

# Define a generic query object, and we will replace the repertoire_id
# within the loop. We also only request productive rearrangements as
# an additional filter.

query = {
    "filters":{
        "op":"and",
        "content": [
            {
                "op":"=",
                "content": {
                    "field":"repertoire_id",
                    "value":"XXX"
                }
	    },
	    {
                "op":"=",
                "content": {
                    "field":"productive",
                    "value":True
                }
	    }
	]
    },
    "size":1000,
    "from":0
}

# Loop through each repertoire and query rearrangement data for
# each. In this example, we only download 10000 rearrangements for each
# repertoire in chunks of 1000 using the from and size parameters.

# Not all repertoires have 10000 productive rearrangements, this code
# should download a total of 293,414 rearrangements.

# If you wanted to download all rearrangements, keep looping until
# zero rearrangements are returned for each repertoire. In that case,
# you might also want to increase the size parameter to return more
# rearrangements with each request. Be careful though because some
# repositories might have a maximum size for a single request.

first = True
for r in repertoires:
    print('Retrieving rearrangements for repertoire: ' + r['repertoire_id'])
    query['filters']['content'][0]['content']['value'] = r['repertoire_id']
    query['size'] = 1000
    query['from'] = 0

    cnt = 0
    while True:
        # send the request
        resp = requests.post(host_url + '/rearrangement', json = query)
        data = resp.json()
        rearrangements = data['Rearrangement']

        # Open a file for writing the rearrangements. We do this here
        # because we need to know the full set of fields being
        # returned from the data repository, otherwise by default only
        # the required fields will be written to the file.
        if first:
            out_file = airr.create_rearrangement('rearrangements.tsv', fields=rearrangements[0].keys())
            first = False

        # save the rearrangements to a file
        for row in rearrangements:
            out_file.write(row)

        # stop when downloaded at most 10,000 rearrangements or if the
        # response doesn't return the full amount, which indicates no more
        # data. If you wanted to download all rearrangements, keep
        # looping until zero rearrangements are returned from the query.
        cnt += len(rearrangements)
        if cnt >= 10000 or len(rearrangements) < 1000:
            break

        # Need to update the from parameter to get the next chunk
        query['from'] = cnt

    print('Retrieved ' + str(cnt) + ' rearrangements for repertoire: ' + r['repertoire_id'])
