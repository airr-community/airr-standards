.. _MiAIRR_Elements:

======================
MiAIRR Data Elements
======================

The AIRR Community has adopted six
high-level data sets that will guide the publication, curation and
sharing of AIRR-Seq data and metadata: Study and subject, sample
collection, sample processing and sequencing, raw sequences, processing
of sequence data, and processed AIRR sequences.

:download:`Download as TSV <../_downloads/AIRR_Minimal_Standard_Data_Elements.tsv>`.

.. list-table::
    :header-rows: 1
    :widths: 1 3 3 3 6 4

    * - Set / Subset
      - Designation / Field
      - Type / Format
      - Level
      - Definition
      - Example
    {%- for field in MiAIRR_schema %}
    * - **{{ field.Set }}** / {{ field.Subset }}
      - {{ field.Designation }} |br| ``{{ field.Name }}``
      - {{ field.Type }} |br| *{{ field.Format }}*
      - {{ field.Level }}
      - {{ field.Definition | trim }}
      - {{ field.Example | trim }}
    {%- endfor %}

