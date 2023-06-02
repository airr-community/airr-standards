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

var airr = {};
module.exports = airr;

airr.load_schema = async function() {
    // Load AIRR spec
    var airrFile = path.resolve(__dirname, './airr-schema-openapi3.yaml');
    var doc = yaml.safeLoad(fs.readFileSync(airrFile));
    if (!doc) Promise.reject(new Error('Could not load AIRR schema yaml file.'));

    // dereference all $ref objects
    var spec = await $RefParser.dereference(doc);
    var schema = require('./schema')(airr, spec);
    var io = require('./io')(airr);

    return Promise.resolve(spec);
};

// schema functions
//const schema = require('./schema')(AIRRSchema);
// i/o functions
//const io = require('./io');

/* TODO? UMD
(function (root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['b'], factory);
    } else if (typeof module === 'object' && module.exports) {
        // Node.
        module.exports = factory(require('b'));
    } else {
        // Browser globals (root is window)
        root.returnExports = factory(root.b);
    }
}(typeof self !== 'undefined' ? self : this, function (b) {
    // Use b in some fashion.

    // Just return a value to define the module export.
    // This example returns an object, but the module
    // can return a function as the exported value.
    return {};
})); */

