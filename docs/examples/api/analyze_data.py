#
# ADC API Example
# analyze_data.py
#
# Author: Scott Christley
# Date: July 26, 2019
#
# This example code shows how repertoires and associated rearrangments
# may be queried from a data repository. In a prior script, the
# retrieved data is stored in files using the AIRR standards python
# library. This script reads the data from those files and performs
# some simple analysis.
#
# Repertoire input file: repertoires.airr.json
# Rearrangement input file: rearrangements.tsv
# CDR3 Histogram output chart: plot.png
#
# We could have written the example to perform the data retrieval and
# analysis in a single script, but we wanted to show the data could be
# saved into files for later use.
#
# This script analyzes the data that was retrieve and saved to files
# by the retrieve_data.py script. You need to run that script first
# before running this one.
#
# This example analyzes the following study, which is identified by
# NCBI BioProject PRJNA300878. In this example, only going to the T
# cell repertoires were retrieved. In this analysis, we are going to
# generate a CDR3 amino acid length histogram where we group the
# rearrangements by the four T cell subsets.
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

import airr
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# We have 4 T cell subsets
subsets = {
    'CL_0000895': [0 for number in range(0,50)],
    'CL_0000900': [0 for number in range(0,50)],
    'CL_0000897': [0 for number in range(0,50)],
    'CL_0000909': [0 for number in range(0,50)]
    }

# Load the repertoire metadata
data = airr.load_repertoire('repertoires.airr.json')
repertoires = { obj['repertoire_id'] : obj for obj in data['Repertoire'] }

# Iterate through the rearrangement data and tabulate the counts
reader = airr.read_rearrangement('rearrangements.tsv')
for row in reader:
    # get the appropriate repertoire
    rep = repertoires[row['repertoire_id']]
    # use the cell_subset field in the repertoire
    c = subsets[rep['sample'][0]['cell_subset']['id']]
    # increment the length count
    if row['junction_aa_length']:
        if int(row['junction_aa_length']) >= 50:
            continue
        #print(int(row['junction_aa_length']))
        c[int(row['junction_aa_length'])] += 1

# normalize the counts so the histograms are comparable
for cnts in subsets:
    total = 0
    for c in subsets[cnts]:
        total += c
    subsets[cnts] = [float(number) / float(total) for number in subsets[cnts]]

# Plot only lengths 10 through 20
labels = [str(label) for label in range(10,20)]

x = np.arange(len(labels))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width, subsets['CL_0000895'][10:20], width/2, label='Naive CD4+ T cell')
rects2 = ax.bar(x - width/2, subsets['CL_0000900'][10:20], width/2, label='Naive CD8+ T cell')
rects3 = ax.bar(x, subsets['CL_0000897'][10:20], width/2, label='Memory CD4+ T cell')
rects4 = ax.bar(x + width/2, subsets['CL_0000909'][10:20], width/2, label='Memory CD8+ T cell')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Relative Counts')
ax.set_title('CDR3 AA Length Histogram')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

fig.savefig('plot.png', transparent=False, dpi=240, bbox_inches="tight")
