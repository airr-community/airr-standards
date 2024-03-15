Installation
------------------------------------------------------------------------------

Install in the usual manner from npm::

    > npm install airr-js

Or from the `downloaded <https://github.com/airr-community/airr-standards>`__
source code directory::

    > npm install file:lang/js


Quick Start
------------------------------------------------------------------------------

The ``airr-js`` package supports use in the browser or in nodejs. In the browser, the
file system is not available, so the read/write functions are not implemented but template
objects can be created, objects can be validated, and the OpenAPI V3 specification can be
accessed. For nodejs, the full functionality is available including the read/write functions.

For nodejs, need to await the loading of the schema before using any functions::

    var airr = require('airr-js');

    // await schema to be loaded and dereferenced
    var spec = await airr.load_schema();

For the browser, the schema also needs to be loaded but the package cannot do it itself,
instead you must provide the Open API V3 specification file as part of your packaging
of the website. When using webpack, a resolve alias in ``webpack.config.js`` can be used
to point to the dereferenced yaml file::

    resolve: {
        alias: {
            'airr-schema': path.resolve(__dirname,'node_modules') + '/airr-js/airr-schema-openapi3-deref.yaml'
        }
    }

The ``package.json`` utilizes the ``browser`` setting supported by website packaging tools
like webpack to provide an alternative entry point, and browser code can import like so::

    import { airr } from 'airr-js';


Create Blank Template Schema Objects (browser, nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import the ``airr-js`` package correctly depending upon browser or nodejs usage as
described above, and then blank template objects can be created::

    // Get the schema definition for an AIRR Object
    var repertoire_schema = new airr.SchemaDefinition('Repertoire');
    // Create a template object
    var blank_repertoire = repertoire_schema.template();

Validate Objects (browser, nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import the ``airr-js`` package correctly depending upon browser or nodejs usage as
described above, and then an object can be validated to its schema::

    // Get the schema definition for an AIRR Object
    var repertoire_schema = new airr.SchemaDefinition('Repertoire');
    // Validate a repertoire object
    var is_valid = repertoire_schema.validate_object(obj);

Reading AIRR Data Files (nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr-js`` package contains functions to read and write AIRR Data
Model files. The file format is either YAML or JSON, and the package provides a
light wrapper over the standard parsers. The file needs a ``json``, ``yaml``, or ``yml``
file extension so that the proper parser is utilized. All of the AIRR objects
are loaded into memory at once and no streaming interface is provided::

    var airr = require('airr-js');
    await airr.load_schema();

    // read AIRR DataFile
    var data = await airr.read_airr('input.airr.json');

Writing AIRR Data Files (nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writing an AIRR Data File is also a light wrapper over standard YAML or JSON
parsers. Multiple AIRR objects, such as Repertoire, GermlineSet, and etc., can be
written together into the same file. In this example, we create some blank
Repertoire objects, and write them to a file.
As with the read function, the complete list of repertoires are written at once,
there is no streaming interface::

    var airr = require('airr-js');
    await airr.load_schema();

    // Create some blank repertoire objects in a list
    var repertoire_schema = new airr.SchemaDefinition('Repertoire');
    var data = { 'Repertoire': [] };
    for (let i = 0; i < 5; ++i)
        data['Repertoire'].push(repertoire_schema.template());

    // Write the AIRR Data
    await airr.write_airr('output.airr.json', data);

Reading AIRR Rearrangement TSV files (nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``airr-js`` package contains functions to read and write AIRR Rearrangement
TSV files as either a stream or the complete file. The streaming interface requires
two callback functions to be provided; one for the header and another for each
row as it is read::

    var airr = require('airr-js');
    await airr.load_schema();

    // read file completely
    var data = await airr.load_rearrangement('input.airr.tsv');

    // for streaming, need two callback functions
    var header_callback = function(headers) { console.log('got headers:', headers); }
    var row_callback = function(row) { console.log('got row:', row); }
    // read the file
    await airr.read_rearrangement('input.airr.tsv', header_callback, row_callback);

Writing AIRR Rearrangement TSV files (nodejs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To be implemented. These write functions will been implemented in a patch release.
