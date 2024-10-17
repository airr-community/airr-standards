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
var jsonDiff = require('json-diff');

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
var output_rearrangement_good = path.resolve(data_path, 'output_good_rearrangement.tsv')
var output_rearrangement_good_gz = path.resolve(data_path, 'output_good_rearrangement.tsv.gz')
//var output_rep = os.path.join(data_path, 'output_rep.json')
var output_good = path.resolve(data_path, 'output_data.json')
var output_good_yaml = path.resolve(data_path, 'output_data.yaml')
//var output_blank = os.path.join(data_path, 'output_blank.json')

test('load schema', async () => {
    const schema = await airr.load_schema();
    expect(schema).not.toBeNull();
});

test('load good airr yaml', () => {
    const data = airr.read_airr(rep_good, true);
    expect(data).not.toBeNull();
});

test('load good rearrangement tsv', async () => {
    const data = await airr.load_rearrangement(rearrangement_good, true);
    expect(data).not.toBeNull();
});

test('write good AIRR Rearrangement TSV', async () => {
    const data = await airr.load_rearrangement(rearrangement_good, true);
    expect(data).not.toBeNull();

    var idx = 0;
    var row_callback = function(fields) {
        if (idx >= data.length) return null;
        else return data[idx++];
    };

    await airr.create_rearrangement(output_rearrangement_good, row_callback);

    const new_data = await airr.load_rearrangement(output_rearrangement_good, true);
    expect(new_data).not.toBeNull();
});

test('dump good AIRR Rearrangement TSV', async () => {
    const data = await airr.load_rearrangement(rearrangement_good, true);
    expect(data).not.toBeNull();

    await airr.dump_rearrangement(data, output_rearrangement_good);

    const new_data = await airr.load_rearrangement(output_rearrangement_good, true);
    expect(new_data).not.toBeNull();
});

test('derive good AIRR Rearrangement TSV', async () => {
    const data = await airr.load_rearrangement(rearrangement_good, true);
    expect(data).not.toBeNull();

    var idx = 0;
    var row_callback = function(fields) {
        if (idx >= data.length) return null;
        else return data[idx++];
    };

    await airr.derive_rearrangement(output_rearrangement_good, rearrangement_good, row_callback);

    const new_data = await airr.load_rearrangement(output_rearrangement_good, true);
    expect(new_data).not.toBeNull();
});

test('validate good rearrangement tsv', async () => {
    let isValid = true;
    const data = await airr.validate_rearrangement(rearrangement_good, true)
        .catch(function(error) { isValid = false; });
    expect(data).not.toBeNull();
    expect(isValid).toBe(true);
});

test('validate bad rearrangement tsv', async () => {
    let isValid = true;
    const data = await airr.validate_rearrangement(rearrangement_bad, true)
        .catch(function(error) { isValid = false; });
    expect(isValid).toBe(false);
});

test('merge good AIRR Rearrangement TSV', async () => {
    var in_files = [ rearrangement_good, rearrangement_good, rearrangement_good];
    await airr.merge_rearrangement(output_rearrangement_good, in_files, false, true);

    const new_data = await airr.load_rearrangement(output_rearrangement_good, true);
    expect(new_data).not.toBeNull();
});

test('write good AIRR DataFile', () => {
    const repertoire_data = airr.read_airr(rep_good, validate=true, debug=true);
    expect(repertoire_data).not.toBeNull();
    const germline_data = airr.read_airr(germline_good, validate=true, debug=true);
    expect(germline_data).not.toBeNull();
    const genotype_data = airr.read_airr(genotype_good, validate=true, debug=true);
    expect(genotype_data).not.toBeNull();

    // combine together and write
    let obj = {}
    obj['Repertoire'] = repertoire_data['Repertoire'];
    obj['GermlineSet'] = germline_data['GermlineSet'];
    obj['GenotypeSet'] = genotype_data['GenotypeSet'];
    airr.write_airr(output_good, obj, validate=true, debug=true);

    // verify we can read it
    let data = airr.read_airr(output_good, validate=true, debug=true);

    // is the data identical?
    delete data['Info'];
    let d = jsonDiff.diff(obj, data);
    expect(d).toBeUndefined();
});
