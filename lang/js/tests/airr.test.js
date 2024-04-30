//
// airr.test.js
// Unit tests for AIRR Standards reference library
//
// Copyright (C) 2023 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

var path = require('path');
var airr = require("../airr")

// Paths
var data_path = path.resolve(__dirname, 'data');

// Test data
var rearrangement_good = path.resolve(data_path, 'good_rearrangement.tsv');
var rearrangement_bad = path.resolve(data_path, 'bad_rearrangement.tsv')
var rep_good = path.resolve(data_path, 'good_repertoire.yaml')
var rep_bad = path.resolve(data_path, 'bad_repertoire.yaml')
var germline_good = path.resolve(data_path, 'good_germline_set.json')
var germline_bad = path.resolve(data_path, 'bad_germline_set.json')
var genotype_good = path.resolve(data_path, 'good_genotype_set.json')
var genotype_bad = path.resolve(data_path, 'bad_genotype_set.json')
var combined_yaml = path.resolve(data_path, 'good_combined_airr.yaml')
var combined_json = path.resolve(data_path, 'good_combined_airr.json')

// Output data
//var output_rep = os.path.join(data_path, 'output_rep.json')
//var output_good = os.path.join(data_path, 'output_data.json')
//var output_blank = os.path.join(data_path, 'output_blank.json')

test('load schema', async () => {
  const schema = await airr.load_schema();
  expect(schema).not.toBeNull();
});

test('load good airr yaml', () => {
  const data = airr.read_airr(rep_good, true);
  expect(data).not.toBeNull();
});

test('load good rearrangement tsv', () => {
  const data = airr.load_rearrangement(rearrangement_good, true);
  expect(data).not.toBeNull();
});
