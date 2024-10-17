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
                        let errors = schema.validate_header(headers);
                        if (errors) return reject(errors);
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
                        let errors = schema.validate_object(row);
                        if (errors) return reject(errors);
                    }

                    if (row_callback) {
                        if (isPromise(row_callback)) await row_callback(row);
                        else row_callback(row);
                    } else {
                        // no reason to read the rows if no callback, so just end the stream
                        readable.destroy();
                        return resolve();
                    }

                    readable.resume();
                })
                .on('end', async function() {
                    return resolve();
                });
        });
    }

    airr.create_rearrangement = async function(filename, row_callback, fields=null, debug=false) {
        if (!row_callback) {
            let msg = 'Row callback function not provided.';
            if (debug) console.error(msg);
            throw new Error(msg);
        }

        var is_gz = false;
        var ext = filename.split('.').pop().toLowerCase();
        if (ext == 'gz') is_gz = true;

        var schema = new airr.SchemaDefinition('Rearrangement');

        // order fields according to spec
        var field_names = schema.required.slice();
        if (fields) {
            var additional_fields = [];
            for (let f in fields) {
                if (schema.required.includes(fields[f]))
                    continue;
                else if (schema.properties.includes(fields[f]))
                    field_names.push(fields[f]);
                else
                    additional_fields.push(fields[f]);
            }
            field_names = field_names.concat(additional_fields);
        }

        return new Promise(async function(resolve, reject) {
            var writable = fs.createWriteStream(filename);
            if (is_gz) writable.pipe(zlib.createGunzip());

            // write header
            writable.write(field_names.join('\t'));
            writable.write('\n');

            let row = null;
            if (isPromise(row_callback)) row = await row_callback(field_names);
            else row = row_callback(field_names);

            while (row) {
                let vals = [];
                for (let i = 0; i < field_names.length; ++i) {
                    let p = field_names[i];
                    if (row[p] == undefined) vals.push('');
                    else vals.push(row[p]);
                }
                writable.write(vals.join('\t'));
                writable.write('\n');

                if (isPromise(row_callback)) row = await row_callback(field_names);
                else row = row_callback(field_names);
            }

            writable.end();
            return resolve();
        });
    }

    airr.derive_rearrangement = async function(out_filename, in_filename, row_callback, fields=null, debug=false) {
        if (!row_callback) {
            let msg = 'Row callback function not provided.';
            if (debug) console.error(msg);
            throw new Error(msg);
        }

        var is_gz = false;
        var ext = out_filename.split('.').pop().toLowerCase();
        if (ext == 'gz') is_gz = true;

        // get fields from input file
        var field_names = null;
        var got_headers = function(h) { field_names = h; }
        await airr.read_rearrangement(in_filename, got_headers, null, false, debug)
            .catch(function(error) { Promise.reject(error); });

        // add any additional fields
        if (fields) {
            var additional_fields = [];
            for (let f in fields) {
                if (field_names.includes(fields[f]))
                    continue;
                else
                    additional_fields.push(fields[f]);
            }
            field_names = field_names.concat(additional_fields);
        }

        return new Promise(async function(resolve, reject) {
            var writable = fs.createWriteStream(out_filename);
            if (is_gz) writable.pipe(zlib.createGunzip());

            // write header
            writable.write(field_names.join('\t'));
            writable.write('\n');

            let row = null;
            if (isPromise(row_callback)) row = await row_callback(field_names);
            else row = row_callback(field_names);

            while (row) {
                let vals = [];
                for (let i = 0; i < field_names.length; ++i) {
                    let p = field_names[i];
                    if (row[p] == undefined) vals.push('');
                    else vals.push(row[p]);
                }
                writable.write(vals.join('\t'));
                writable.write('\n');

                if (isPromise(row_callback)) row = await row_callback(field_names);
                else row = row_callback(field_names);
            }

            writable.end();
            return resolve();
        });
    }

    airr.load_rearrangement = async function(filename, validate=false, debug=false) {
        var rows = [];

        var got_row = function(row) { rows.push(row); }
        await airr.read_rearrangement(filename, null, got_row, validate, true, debug)
            .catch(function(error) { Promise.reject(error); });

        return Promise.resolve(rows);
    }

    airr.dump_rearrangement = async function(data, filename, fields=null, debug=false) {
        var idx = 0;
        var row_callback = function(field_names) {
            if (idx >= data.length) return null;
            else return data[idx++];
        };

        return airr.create_rearrangement(filename, row_callback, fields, debug);
    }

    airr.merge_rearrangement = async function(out_filename, in_filenames, drop=false, debug=false) {
        var is_gz = false;
        var ext = out_filename.split('.').pop().toLowerCase();
        if (ext == 'gz') is_gz = true;

        // gather fields from input files
        var first = true;
        var field_names = [];
        var got_headers = function(headers) {
            if (first) {
                field_names = headers;
                first = false;
            } else {
                // intersection
                if (drop) field_names = field_names.filter(value => headers.includes(value));
                else { // or union
                    for (let h in headers) {
                        if (!field_names.includes(headers[h])) {
                            field_names.push(headers[h]);
                        }
                    }
                }
            }
        }
        for (let f in in_filenames) {
            await airr.read_rearrangement(in_filenames[f], got_headers, null, false, debug)
                .catch(function(error) { Promise.reject(error); });
        }

        // write input files to output file sequentially
        return new Promise(async function(resolve, reject) {
            var writable = fs.createWriteStream(out_filename);
            if (is_gz) writable.pipe(zlib.createGunzip());

            // write header
            writable.write(field_names.join('\t'));
            writable.write('\n');

            var got_row = function(row) {
                let vals = [];
                for (let i = 0; i < field_names.length; ++i) {
                    let p = field_names[i];
                    if (row[p] == undefined) vals.push('');
                    else vals.push(row[p]);
                }
                writable.write(vals.join('\t'));
                writable.write('\n');
            }

            for (let f in in_filenames) {
                await airr.read_rearrangement(in_filenames[f], null, got_row, false, debug)
                    .catch(function(error) { Promise.reject(error); });
            }

            writable.end();
            return resolve();
        });
    }

    airr.validate_rearrangement = async function(filename, debug=false) {
        var got_row = function(row) { };
        return airr.read_rearrangement(filename, null, got_row, true, true, debug);
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


