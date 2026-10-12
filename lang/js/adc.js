'use strict';

//
// adc.js
// AIRR Standards reference library for antibody and TCR sequencing data
// ADC API schema
// node edition
//
// Copyright (C) 2026 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

// The I/O file routines are provided with the node edition.

// Node Libraries
var yaml = require('js-yaml');
var path = require('path');
var fs = require('fs');
const $RefParser = require("@apidevtools/json-schema-ref-parser");
const merge = require('allof-merge');

var adc = {};
module.exports = adc;

// load ADC API schema
adc.load_adc_schema = async function() {
    // Load ADC API spec
    var airrFile = path.resolve(__dirname, './adc-api-openapi3.yaml');
    var doc = yaml.safeLoad(fs.readFileSync(airrFile));
    if (!doc) Promise.reject(new Error('Could not load ADC API yaml file.'));

    // dereference all $ref objects
    var spec = await $RefParser.dereference(doc);

    // get the schemas
    var schema_doc = doc['components']['schemas'];
    if (!schema_doc) Promise.reject(new Error('Cannot find schemas in the ADC API yaml file.'));

    // merge allOfs
    for (let obj in schema_doc) {
        if (schema_doc[obj]['type'] || schema_doc[obj]['allOf']) {
            schema_doc[obj] = merge.merge(schema_doc[obj]);
        }
    }

    schema_doc['Info'] = doc['info'];
    var schema = require('./schema')(adc, schema_doc);
    //var io = require('./io')(adc);

    return Promise.resolve(schema_doc);
};
