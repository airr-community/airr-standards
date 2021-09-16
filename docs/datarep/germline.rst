.. _GermlineRepresentations:

Germline Schema (Experimental)
==============================

Motivation
----------

Understanding and cataloguing receptor germline genes and allele sequences is critical to the analysis of AIRR data. 
While the human set is relatively well understood in outline, although probably still far from complete, those of other 
species, even those that are relatively closely studied, is at a much earlier stage. There is an urgent need to define a 
standardised format for listing such genes, so that they can be shared between researchers and easily consumed by software 
tools.

Receptor Germline Schema
------------------------

The receptor germline schema defines the data elements necessary to describe one or more receptor germline genes, together 
with supporting evidence. The fundamental object is the ``GeneDescription``, which describes a single gene or allele, containing 
the necessary details for the annotation of a rearranged sequence such as the location of CDRs (in the case of a V-gene) and 
framing information (in the case of a J-gene). ``GeneDescription`` also contains fields to delineate RSS, and the leader regions 
of V-genes, should those be covered by the sequence provided.

Evidence supporting the gene or allele can be provided in linked ``GermlineSequence`` and ``RearrangedSequence`` objects. Information 
represented in these objects will typically be stored in a repository: either an INSDC repository such as Genbank or SRA, or 
a lower-tier repository such as OGRDB. Please note that the key distinction between these object types is whether the V(D)J 
genes have rearranged, rather than the origin of the material, as mature B and T cells carry rearranged sequences in chromosomal 
DNA. It is most likely that supporting sequences will be GermlineSequences, i.e. prior to rearrangement. In the case of a 
germline inference from a repertoire, the inferred germline sequence should be provided as a ``GermlineSequence``, if the evidence 
has been deposited in a repository.

For V-genes, an IMGT-gapped sequence (i.e.,. a sequence delineated in accordance with the 
`IMGT numbering scheme <http://www.imgt.org/IMGTindex/numbering.php>`_)  is provided in 
``GeneDescription``. Other delineations, such as  `Chothia <http://www.bioinf.org.uk/abs/info.html#chothianum>`_ and 
`Kabat <http://www.bioinf.org.uk/abs/info.html#kabatnum>`_, can be provided via linked ``GeneDelineationV`` objects.
A ``GermlineSet`` brings together multiple ``GeneDescriptions`` from the same locus to form a curated set. The schema assumes that germline 
sets will be published by multiple repositories. A germline set may be uniquely referenced by means of the ``germline_set_ref:`` 
this is a composite field containing the repository id, germline set label, and version.

Gene and Allele Naming
----------------------

The International Union of Immunological Societies allocates gene symbols for receptor genes. GeneDescription contains a gene_symbol 
field, but it is optional, recognising that a symbol may not have been assigned. Gene symbols are long-lasting, but the underlying 
sequence may be revised over time. GeneDescription contains a mandatory coding_sequence_identifier, which will be updated should the 
sequence change. It is anticipated that publishers of gene sets will provide mechanisms to issue these identifiers, and to allow 
researchers to review change history of GeneDescriptions and GermlineSets. In the interests of consistency and transparency, when 
referring to a gene or allele, the gene_symbol should be used wherever possible, however coding_sequence_identifier provides a fallback 
where a gene symbol has not been assigned.

Genotypes
---------

A ``ReceptorGenotype`` describes the specific alleles found in an individual, and also identifies genes that are not found (deleted). 
Depending on the data available and the inference method used, genotypes may contain haplotyping information, which may be full, or partial. 
As an example of partial haplotyping, the genotype may have been determined from genomic sequencing in which the sequence of the locus was 
assembled into contigs, but could not be fully assembled. In this case the co-location of alleles in each contig has been established, but 
the co-location across the entire locus can not be. Co-location is therefore indicated by means of the ``phasing`` parameter, which in this 
case would be assigned a different value for alleles on each contig. 

File Format Specification
-------------------------

The file format has not been specified yet.

.. _GermlineSetFields:

GermlineSet Fields
-----------------------------

:download:`Download as TSV <../_downloads/GermlineSet.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in GermlineSet_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _GeneDescriptionFields:

GeneDescription Fields
-----------------------------

:download:`Download as TSV <../_downloads/GeneDescription.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in GeneDescription_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _RearrangedSequenceFields:

RearrangedSequence Fields
-----------------------------

:download:`Download as TSV <../_downloads/RearrangedSequence.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in RearrangedSequence_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _GermlineSequenceFields:

GermlineSequence Fields
-----------------------------

:download:`Download as TSV <../_downloads/GermlineSequence.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in GermlineSequence_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _GeneDelineationVFields:

GeneDelineationV Fields
-----------------------------

:download:`Download as TSV <../_downloads/GeneDelineationV.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in GeneDelineationV_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _ReceptorGenotypeFields:

ReceptorGenotype Fields
-----------------------------

:download:`Download as TSV <../_downloads/ReceptorGenotype.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in ReceptorGenotype_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _MHCGenotypeFields:

MHCGenotype Fields
-----------------------------

:download:`Download as TSV <../_downloads/MHCGenotype.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in MHCGenotype_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}
