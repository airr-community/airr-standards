'use strict';

//
// airr.js
// AIRR Standards reference library for antibody and TCR sequencing data
//
// Copyright (C) 2023 The AIRR Community
//
// Author: Scott Christley <scott.christley@utsouthwestern.edu>
//

// Node Libraries
var yaml = require('js-yaml');
var path = require('path');
var fs = require('fs');
const zlib = require('zlib');
const $RefParser = require("@apidevtools/json-schema-ref-parser");
var csv = require('csv-parser');
const AJV = require("ajv");
const addFormats = require("ajv-formats")

var airr = {};
module.exports = airr;

// Boolean value mappings
var true_values = ['True', 'true', 'TRUE', 'T', 't', '1', 1, true];
var false_values = ['False', 'false', 'FALSE', 'F', 'f', '0', 0, false];
var _to_bool_map = function(x) {
    if (true_values.indexOf(x) >= 0) return true;
    if (false_values.indexOf(x) >= 0) return false;
    return null;
};
var _from_bool_map = function(x) {
    if (x == true) return 'T';
    if (x == false) return 'F';
    return '';
};

class ValidationError extends Error {  
  constructor (message) {
    super(message)

    // assign the error class name in your custom error (as a shortcut)
    this.name = this.constructor.name

    // capturing the stack trace keeps the reference to your error class
    Error.captureStackTrace(this, this.constructor);
  }
}

function isPromise(promise) {  
    return !!promise && typeof promise.then === 'function'
}

//
// AIRR Schema
//

// Load AIRR schema, returns a promise
airr.Schema = null;
airr.load_schema = async function() {
    // Load AIRR spec
    var airrFile = path.resolve(__dirname, './airr-schema-openapi3.yaml');
    var doc = yaml.safeLoad(fs.readFileSync(airrFile));
    if (!doc) Promise.reject(new Error('Could not load AIRR schema yaml file.'));

    // dereference all $ref objects
    var spec = await $RefParser.dereference(doc);
    airr.Schema = {"specification": spec};
    return Promise.resolve(spec);
};

airr.get_schema = function(definition) {
    if (!airr.Schema) throw new Error('AIRR schema is not loaded.');
    return new airr.SchemaDefinition(definition);
};

airr.get_info = function() {
    if (!airr.Schema) throw new Error('AIRR schema is not loaded.');
    return airr.Schema['specification']['Info'];
}

airr.SchemaDefinition = function(definition) {
    if (!airr.Schema) throw new Error('AIRR schema is not loaded.');

    if (definition == 'Info') {
        throw new Error('Info is an invalid schema definition name');
    }

    this.definition = airr.Schema['specification'][definition];
    if (! this.definition)
        throw new Error('Schema definition ' + definition + ' cannot be found in the specifications');

    this.info = airr.Schema['specification']['Info'];
    if (! this.info)
        throw new Error('Info object cannot be found in the specifications');

    this.properties = this.definition['properties']
    this.required = this.definition['required']
    if (! this.required) this.required = [];

    //this.optional = [f for f in self.properties if f not in self.required]

    return this;
}

airr.SchemaDefinition.prototype.spec = function(field) {
    return this.properties[field];
};

airr.SchemaDefinition.prototype.type = function(field) {
    var field_spec = this.properties[field];
    if (! field_spec) return null;
    var field_type = field_spec['type'];
    return field_type;
};

airr.SchemaDefinition.prototype.is_ontology = function(field) {
    var field_spec = this.properties[field];
    if (! field_spec) return false;
    var field_type = field_spec['type'];
    if (field_type != 'object') return false;
    if ((this.properties[field]['x-airr']) && (this.properties[field]['x-airr']['format'] == 'ontology')) return true;

    return false;
};

airr.SchemaDefinition.prototype.to_bool = function(value, validate) {
    if (value == null) return null;

    var bool_value = _to_bool_map(value);
    if (validate && (bool_value == null))
        throw new Error('invalid bool ' + value);
    return bool_value;
};

airr.SchemaDefinition.prototype.from_bool = function(value, validate) {
    if (value == null) return '';

    var str_value = _from_bool_map(value);
    if (validate && (str_value == null))
        throw new Error('invalid bool ' + value);
    return str_value;
};

airr.SchemaDefinition.prototype.to_int = function(value, validate) {
    if (value == null) return null;
    if (value == '') return null;

    var int_value = parseInt(value);
    if (isNaN(int_value)) {
        if (validate)
            throw new Error('invalid int ' +  value);
        else
            return null;
    }
    return int_value;
};

airr.SchemaDefinition.prototype.to_float = function(value, validate) {
    if (value == null) return null;
    if (value == '') return null;

    var float_value = parseFloat(value);
    if (isNaN(float_value)) {
        if (validate)
            throw new Error('invalid float ' +  value);
        else
            return null;
    }
    return float_value;
};

airr.SchemaDefinition.prototype.map_value = function(map) {
    //console.log('map value: ', map);
    //console.log(this);
    var field_type = this.type(map['header']);
    var field_value = map['value'];
    switch (field_type) {
    case 'boolean':
        field_value = this.to_bool(field_value);
        break;
    case 'integer':
        field_value = this.to_int(field_value);
        break;
    case 'number':
        field_value = this.to_float(field_value);
        break;
    }
    return field_value;
};

//
// Validation functions
//

airr.SchemaDefinition.prototype.validate_header = function(header) {
    return false;
}

airr.SchemaDefinition.prototype.validate_row = function(row) {
    return false;
}

airr.SchemaDefinition.prototype.validate_object = function(object) {
    const ajv = new AJV();
    addFormats(ajv);
    ajv.addVocabulary(['x-airr', 'example']);

    const validate = ajv.compile(this.definition)
    const valid = validate(object)
    if (!valid) console.log(validate.errors)

    return valid;
}

airr.SchemaDefinition.prototype.template = function() {
    // Set defaults for each data type
    var type_default = {'boolean': false, 'integer': 0, 'number': 0.0, 'string': '', 'array':[]};

    var _default = function(spec) {
        if (spec['default']) return spec['default'];
        if (spec['nullable']) return null;
        //if (spec['enum']) return spec['enum'][0];
        return type_default[spec['type']];
    };

    var _populate = function(schema, obj) {
        if (schema.allOf) {
            for (const k in schema.allOf)
                _populate(schema['allOf'][k], obj);
            return;
        }
        for (const k in schema.properties) {
            let spec = schema.properties[k];
            // Skip deprecated
            if (spec['x-airr'] && spec['x-airr']['deprecated'])
                continue
            // populate with value
            switch (spec['type']) {
                case 'object': {
                    let new_obj = {};
                    obj[k] = new_obj;
                    _populate(spec, new_obj);
                    break;
                }
                case 'array':
                    if (spec['items'] && spec['items']['type'] == 'object') {
                        let new_obj = {};
                        obj[k] = [ _populate(spec['items'], new_obj) ];
                    } else
                        obj[k] = _default(spec);
                    break;
                default:
                    obj[k] = _default(spec);
            }
        }
    };

    var obj = {};
    _populate(this, obj);
    return (obj);
}

//
// Interface functions for file operations
//

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

airr.write_airr = function(file) {
    return null;
}

// Given a field, check if included in field set
// Field sets include:
// miairr, for only MiAIRR fields
// airr-core, for all required and identifier fields
// airr-schema, for all fields
airr.checkSet = function(schema, field_set, f) {
    switch (field_set) {
    case 'miairr':
        if ((schema['properties'][f]['x-airr']) && (schema['properties'][f]['x-airr']['miairr']))
            return true;
        break;
    case 'airr-core':
        // miairr
        if ((schema['properties'][f]['x-airr']) && (schema['properties'][f]['x-airr']['miairr']))
            return true;
        // identifer
        if ((schema['properties'][f]['x-airr']) && (schema['properties'][f]['x-airr']['identifier']))
            return true;
        // required
        if ((schema['required']) && (schema['required'].indexOf(f) >= 0))
            return true;
        break;
    case 'airr-schema':
        // all fields
        return true;
    }
    return false;
}

// Recursively walk through schema and collect fields based upon field set.
// The schema loader resolves the $ref references so we do not need to follow them.
airr.collectFields = function(schema, field_set, field_list, context, force) {
    for (var f in schema['properties']) {
        var full_field = f;
        if (context) full_field = context + '.' + f;
        //console.log(full_field);
        //console.log(schema['properties'][f]);

        // check if deprecated
        if ((schema['properties'][f]['x-airr']) && (schema['properties'][f]['x-airr']['deprecated']))
            continue;

        var field_type = schema['properties'][f]['type'];
        switch (field_type) {
        case 'object':
            // sub-object
            if ((schema['properties'][f]['x-airr']) && (schema['properties'][f]['x-airr']['ontology'])) {
                // if it is an ontology object, check the object then force the ontology fields if necessary
                if (airr.checkSet(schema, field_set, f))
                    airr.collectFields(schema['properties'][f], field_set, field_list, full_field, true);
            } else
                airr.collectFields(schema['properties'][f], field_set, field_list, full_field, force);
            break;
        case 'array':
            if (schema['properties'][f]['items']['type'] == 'object') {
                // array of sub-objects
                airr.collectFields(schema['properties'][f]['items'], field_set, field_list, full_field, force);
            } else if (schema['properties'][f]['items']['allOf']) {
                // array of composite objects
                for (var s in schema['properties'][f]['items']['allOf']) {
                    airr.collectFields(schema['properties'][f]['items']['allOf'][s], field_set, field_list, full_field, force);
                }
            } else {
                // array of primitive types
                if (airr.checkSet(schema, field_set, f))
                    field_list.push(full_field);
            }
            break;
        case 'string':
        case 'number':
        case 'integer':
        case 'boolean':
            // primitive types
            if (force)
                field_list.push(full_field);
            else if (airr.checkSet(schema, field_set, f))
                field_list.push(full_field);
            break;
        default:
            // unhandled schema structure
            console.error('VDJServer ADC API INFO: Unhandled schema structure: ' + full_field);
            break;
        }
    }
}

// Add the fields to the document if any are missing
airr.addFields = function(document, field_list, schema) {
    for (var r in field_list) {
        var path = field_list[r].split('.');
        var obj = document;
        var spec = schema;
        for (var p = 0; p < path.length; p++) {
            spec = spec['properties'][path[p]];
            // if not in the spec then give up
            if (!spec) break;

            if (spec['type'] == 'array') {
                if ((spec['items']['type'] == undefined) || (spec['items']['type'] == 'object')) {
                    // array of object
                    if (obj[path[p]] == undefined) obj[path[p]] = [{}];
                    var sub_spec = spec['items'];
                    if (spec['items']['allOf']) {
                        // need to combine the properties
                        sub_spec = { type: 'object', properties: {} };
                        for (var i in spec['items']['allOf']) {
                            var sub_obj = spec['items']['allOf'][i];
                            for (var j in sub_obj['properties']) {
                                sub_spec['properties'][j] = sub_obj['properties'][j];
                            }
                        }
                    }
                    for (var a in obj[path[p]]) {
                        airr.addFields(obj[path[p]][a], [ path.slice(p+1).join('.') ], sub_spec);
                    }
                } else {
                    // array of primitive data types
                    if (obj[path[p]] == undefined) obj[path[p]] = null;
                }
                break;
            } else if (spec['type'] == 'object') {
                if (obj[path[p]] == undefined) {
                    if (p == path.length - 1) obj[path[p]] = null;
                    else obj[path[p]] = {};
                }
                obj = obj[path[p]];
            } else if (obj[path[p]] != undefined) obj = obj[path[p]];
            else if (p == path.length - 1) obj[path[p]] = null;
            else console.error('VDJServer ADC API ERROR: Internal error (addFields) do not know how to handle path element: ' + p);
        }
    }
};

