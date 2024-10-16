'use strict';

//
// io.js
// AIRR Standards reference library for antibody and TCR sequencing data
//
// Copyright (C) 2023 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

// Node Libraries
var yaml = require('js-yaml');
var fs = require('fs');
const zlib = require('zlib');
var csv = require('csv-parser');

function isPromise(promise) {
    return !!promise && typeof promise.then === 'function'
}

//
// Interface functions for file operations
//
module.exports = function(airr) {

    airr.read_rearrangement = async function(filename, header_callback=null, row_callback=null, validate=false, model=true, debug=false) {
        var is_gz = false;
        var ext = filename.split('.').pop().toLowerCase();
        if (ext == 'gz') is_gz = true;

        var schema = new airr.SchemaDefinition('Rearrangement');

        var mapValues = function(map) {
            return schema.map_value(map);
        };

        return new Promise(function(resolve, reject) {
            var readable = fs.createReadStream(filename);
            if (is_gz) readable.pipe(zlib.createGunzip());
            readable.pipe(csv({separator:'\t', mapValues: mapValues}))
                .on('headers', async function(headers) {
                    readable.pause();

                    if (validate) {
                        try {
                            schema.validate_header(headers);
                        } catch (err) {
                            reject(err);
                        }
                    }

                    if (header_callback) {
                        if (isPromise(header_callback)) await header_callback(headers);
                        else header_callback(headers);
                    }

                    readable.resume();
                })
                .on('data', async function(row) {
                    readable.pause();

                    if (validate) {
                        try {
                            schema.validate_row(row);
                        } catch (err) {
                            reject(err);
                        }
                    }

                    if (row_callback) {
                        if (isPromise(row_callback)) await row_callback(row);
                        else row_callback(row);
                    }

                    readable.resume();
                })
                .on('end', async function() {
                    return resolve();
                });
        });
    }

    airr.create_rearrangement = function(file) {
        return null;
    }

    airr.derive_rearrangement = function(file) {
        return null;
    }

    airr.load_rearrangement = async function(filename, validate=false, debug=false) {
        var rows = [];

        var got_row = function(row) { rows.push(row); }
        await airr.read_rearrangement(filename, null, got_row, validate, true, debug)
            .catch(function(error) { Promise.reject(error); });

        return Promise.resolve(rows);
    }

    airr.dump_rearrangement = function(file) {
        return null;
    }

    airr.merge_rearrangement = function(file) {
        return null;
    }

    airr.validate_rearrangement = function(file) {
        return null;
    }

    airr.read_airr = function(filename, validate=false, model=true, debug=false) {
        var data = null;
        var ext = filename.split('.').pop().toLowerCase();
        if ((ext == 'yaml') || (ext == 'yml') || (ext == 'json')) {
            data = yaml.safeLoad(fs.readFileSync(filename));
        } else {
            let msg = 'Unknown file type:' + ext + '. Supported file extensions are "yaml", "yml" or "json"';
            if (debug) console.error(msg);
            throw new Error(msg);
        }

        if (validate) {
            if (debug) console.log('Validating:', filename);
            try {
                var schema = new airr.SchemaDefinition('DataFile');
                schema.validate_object(data);
            } catch (err) {
                if (debug) console.error(filename, 'failed validation.');
                throw new ValidationError(err);
            }
        }
    
        return data;
    }

    airr.validate_airr = function(filename) {
        return airr.read_airr(filename, true);
    }

    airr.write_airr = function(filename, data, format=null, info=null, validate=false, model=true, debug=false, check_nullable=true) {
        // data parameter should be an object
        if (typeof data != 'object') {
            let msg = 'Data parameter is not an object.';
            if (debug) console.error(msg)
            throw new Error(msg);
        }

        var DataFileSchema = new airr.SchemaDefinition('DataFile');

        // Validate if requested
        if (validate) {
            if (debug) console.log('Validating:', filename);
            try {
                let schema = new airr.SchemaDefinition('DataFile');
                schema.validate_object(data);
            } catch (err) {
                if (debug) console.error(filename, 'failed validation.');
                throw new ValidationError(err);
            }
        }

        // output object
        var md = {}
        md['Info'] = info
        if (!info) {
            md['Info'] = DataFileSchema.info.copy()
            md['Info']['title'] = 'AIRR Data File'
            md['Info']['description'] = 'AIRR Data File written by AIRR Standards JavaScript Library'
        }

        // Loop through each entry and add them to the output object
        for (let k in data) {
            if (k == 'Info') continue;
            if (k == 'DataFile') continue;
            if (!data[k]) continue;
            if (model && !DataFileSchema.properties[k]) {
                if (debug) console.error('Skipping non-DataFile object:', k);
                continue
            }
            md[k] = data[k];
        }

        // Determine file type from extension and use appropriate format
        var ext = filename.split('.').pop().toLowerCase();
        if (ext == 'yaml' || ext == 'yml') {
            const yamlString = yaml.dump(data);
            fs.writeFileSync(filename, yamlString);
        } else if (ext == 'json') {
            const jsonData = JSON.stringify(data, null, 2);
            fs.writeFileSync(filename, jsonData);
        } else {
            let msg = 'Unknown file type:' + ext + '. Supported file extensions are "yaml", "yml" or "json"';
            if (debug) console.error(msg);
            throw new Error(msg);
        }

        return true;
    }

    return airr;
};


