'use strict';

//
// airr-browser.js
// AIRR Standards reference library for antibody and TCR sequencing data
// browser edition
//
// Copyright (C) 2023 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

// The I/O file routines are not provided with the browser edition.

// For webpack, we are utilizing the browser entry in package.json
// Are we assuming Webpack?

export var airr = {};

// the specification, resolved by webpack
import AIRRSchema from 'airr-schema';
// schema functions
var schema = require('./schema')(airr, AIRRSchema);
