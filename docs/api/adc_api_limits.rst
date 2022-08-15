.. _DataCommonsAPILimits:

ADC API Limits and Thresholds
-----------------------------

Repertoire endpoint query fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is expected that the number of repertoires in a data repository will
never become so large such that queries become computationally
expensive. A data repository might have thousands of repertoires across
hundreds of studies, yet such numbers are easily handled by databases.
Based upon this, the ADC API does not place limits on the repertoire
endpoint for the fields that can be queried or the operators that can be
used.


Other endpoint query fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike repertoire data, data repositories are expected to store billions
of other records (e.g. Rearrangement, CellExpression, Clone, Cell),
where performing "simple" queries can quickly
become computationally expensive. Data repositories are encouraged to
optimize their databases for performance. Therefore, based upon a set of
query use cases provided by immunology experts, a minimal
set of required fields was defined that can be queried. These required
fields are described in the following Table. The fields also have the
AIRR extension property ``adc-query-support: true`` in the AIRR Schema.


**Minimal Rearrangement Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - sequence_id, repertoire_id, sample_processing_id, data_processing_id, clone_id, cell_id
      - Identifiers; sequence_id allows for query of that specific rearrangement object in the repository, while repertoire_id, sample_processing_id, and data_processing_id are links to the repertoire metadata for the rearrangement. The clone_id and cell_id are identifiers that group rearrangements based on clone assignment and single cell assignment.
    * - locus, v_call, d_call, j_call, c_call, productive, junction_aa, junction_aa_length
      - Commonly used rearrangement annotations.

**Minimal Clone Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - clone_id, repertoire_id, data_processing_id
      - Identifiers; clone_id allows for query of that specific clone object in the repository, while repertoire_id and data_processing_id are links to the repertoire metadata for the clone.
    * - v_call, d_call, j_call, junction_aa, junction_aa_length, clone_count
      - Commonly used clone annotations.

**Minimal Cell Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - cell_id, repertoire_id, data_processing_id
      - Identifiers; cell_id allows for query of that specific cell object in the repository, while repertoire_id and data_processing_id are links to the repertoire metadata for the cell.
    * - rearrangements, receptors, reactivity_measurements, expression_study_method, virtual_pairing
      - Commonly used cell attributes.

**Minimal CellExpression Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - expression_id, cell_id, repertoire_id, data_processing_id
      - Identifiers; expression_id allows for query of that specific expression object in the repository, while repertoire_id and data_processing_id are links to the repertoire metadata for the cell. cell_id allows for searching for expression data for a specific cell.
    * - property, value
      - Commonly used cell expression attributes.

**Minimal Receptor Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - receptor_id, receptor_hash
      - Identifiers; receptor_id allows for query of that specific receptor object in the repository. receptor_hash allows for a fast/efficient look up of the globally unique receptor hash.
    * - receptor_type, receptor_variable_domain_1_aa, receptor_variable_domain_1_locus, receptor_variable_domain_2_aa, receptor_variable_domain_2_locus, receptor_ref, reactivity_measurements
      - Commonly used receptor attributes.

**Minimal ReceptorReactivity Query Fields**

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field(s)
      - Description
    * - receptor_reactivity_id
      - Identifiers; receptor_reactivity_id allows for query of that specific receptor reactivity object in the repository.
    * - ligand_type, antigen_type, antigen, antigen_source_species, peptide_sequence_aa, mhc_class, mhc_gene_1, mhc_allele_1, mhc_gene_2, mhc_allele_2, reactivity_method, reactivity_readout, reactivity_value, reactivity_unit
      - Commonly used receptor reactivity attributes.

Data repository specific limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A data repository may impose limits on the size of the data sent to and
returned by the repository.
This might be because of limitations imposed by the back-end database
being used or because of the need to manage the load placed on the
server. For example, MongoDB databases have document size limits
(16 megabytes) which limit the size of a query that can be sent to a
repository and the size of a single repertoire or rearrangement object
that is returned. As a result a repository might choose to set a
maximum query size.

Size limits can be retrieved from the ``info`` endpoint. These limits are 
repository wide (the same for all endpoints). If the data
repository does not provide a limit, then no limit is assumed.


.. list-table::
    :widths: auto
    :header-rows: 1

    * - Field
      - Description
    * - ``max_size``
      - The maximum value for the ``size`` query parameter. Attempting to retrieve data from a repository beyond this maximum should trigger an error response. The error response should include information about why the query failed and what the maximum size limit is. 
    * - ``max_query_size``
      - The maximum size (in bytes) of the JSON query object. Atempting to send a query to a repository larger than this size should trigger an error.
