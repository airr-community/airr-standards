'use strict';

//
// airr.js
// AIRR Standards reference library for antibody and TCR sequencing data
// node edition
//
// Copyright (C) 2023 The AIRR Community
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

var airr = {};
module.exports = airr;

// load AIRR standards schema
airr.load_schema = async function() {
    // Load AIRR spec
    var airrFile = path.resolve(__dirname, './airr-schema-openapi3.yaml');
    var doc = yaml.load(fs.readFileSync(airrFile));
    if (!doc) Promise.reject(new Error('Could not load AIRR schema yaml file.'));

    // dereference all $ref objects
    var spec = await $RefParser.dereference(doc);
    // merge allOfs
    for (let obj in spec) {
        if (spec[obj]['type'] || spec[obj]['allOf']) {
            spec[obj] = merge.merge(spec[obj]);
        }
    }
    var schema = require('./schema')(airr, spec);
    var io = require('./io')(airr);

    return Promise.resolve(spec);
};

// load custom schema
airr.load_custom_schema = async function(obj, filename) {
    // Load schema file
    //var airrFile = path.resolve(__dirname, filename);
    var doc = yaml.load(fs.readFileSync(filename));
    if (!doc) Promise.reject(new Error('Could not load custom schema yaml file.'));

    // dereference all $ref objects
    var spec = await $RefParser.dereference(doc);
    // merge allOfs
    for (let obj in spec) {
        if (spec[obj]['type'] || spec[obj]['allOf']) {
            spec[obj] = merge.merge(spec[obj]);
        }
    }
    var schema = require('./schema')(obj, spec);

    return Promise.resolve(spec);
};
