'use strict';

//
// deref.js
// AIRR Standards reference library for antibody and TCR sequencing data
// generate a dereferenced version of the spec
//
// Copyright (C) 2023 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

// The I/O file routines are provided with the node edition.

// Node Libraries
var yaml = require('js-yaml');
var fs = require('fs');
var path = require('path');
var airr = require('./airr');

airr.load_schema().then(function() {
    var outFile = path.resolve(__dirname, './airr-schema-openapi3-deref.yaml');
    fs.writeFile(outFile, yaml.safeDump(airr.Schema['specification']), (err) => {
        if (err) {
            console.error(err);
            process.exit(1);
        }
    });
}).catch(function(error) {
    console.error(error);
    process.exit(1);
});
