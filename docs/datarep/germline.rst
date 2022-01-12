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
with supporting evidence. The fundamental object is the ``AlleleDescription``, which describes a single gene or allele, containing 
the necessary details for the annotation of a rearranged sequence such as the location of CDRs (in the case of a V-gene) and 
framing information (in the case of a J-gene). ``AlleleDescription`` also contains fields to delineate RSS, and the leader regions 
of V-genes, should those be covered by the sequence provided.

Evidence supporting the gene or allele can be provided in linked ``UnrearrangedSequence`` and ``RearrangedSequence`` objects. Information 
represented in these objects will typically be stored in a repository: either an INSDC repository such as Genbank or SRA, or 
a lower-tier repository such as OGRDB. Please note that the key distinction between these object types is whether the V(D)J 
genes have rearranged, rather than the origin of the material, as mature B and T cells carry rearranged sequences in chromosomal 
DNA. It is most likely that supporting sequences will be ``UnrearrangedSequences``, i.e. prior to rearrangement. In the case of a 
germline inference from a repertoire, the inferred germline sequence should be provided as a ``RearrangedSequence``, if the evidence 
has been deposited in a repository.

For V-genes, an IMGT-gapped sequence (i.e.,. a sequence delineated in accordance with the 
`IMGT numbering scheme <http://www.imgt.org/IMGTindex/numbering.php>`_)  is provided in 
``AlleleDescription``. Other delineations, such as  `Chothia <http://www.bioinf.org.uk/abs/info.html#chothianum>`_ and 
`Kabat <http://www.bioinf.org.uk/abs/info.html#kabatnum>`_, can be provided via linked ``SequenceDelineationV`` objects.
A ``GermlineSet`` brings together multiple ``AlleleDescriptions`` from the same locus to form a curated set. The schema assumes that germline 
sets will be published by multiple repositories. A germline set may be uniquely referenced by means of the ``germline_set_ref``: 
this is a composite field containing the repository id, germline set label, and version.

Gene and Allele Naming
----------------------

``AlleleDescription`` contains a ``label`` field, which should contain the accepted name for the field, as determined by the authors/curators 
of the record. The International Union of Immunological Societies allocates gene symbols for receptor genes, and, if a gene symbol has been 
allocated, this should be used as the label.  Where a gene symbol has not been allocated (for example, because the gene or allele has only 
recently been discovered, or because the available evidence does not meet IUIS standards, a 'tempporary label' should be used.  It is anticipated 
that publishers of gene sets will provide mechanisms to issue these temporary labels, and to allow researchers to review change history of 
``AlleleDescriptions`` and ``GermlineSets``. To provide consistency across research groups, the  
`Germline Database Working Group of the AIRR Community <https://www.antibodysociety.org/the-airr-community/airr-working-groups/germline_database/>`_ is 
developing a `community-wide approach <https://github.com/williamdlees/IgLabel>`_ to the allocation of temporary labels.

Genotypes
---------

A ``GenotypeSet`` describes the specific alleles found in an individual, and also identifies genes that are not found (this could be either 
because they are not present in the chromosomal locus, or brcause they are not expressed or expressed only at low levels). 
Depending on the data available and the inference method used, genotypes may contain haplotyping information, which may be full, or partial. 
As an example of partial haplotyping, the genotype may have been determined from genomic sequencing in which the sequence of the locus was 
assembled into contigs, but could not be fully assembled. In this case the co-location of alleles in each contig has been established, but 
the co-location across the entire locus can not be. Co-location is therefore indicated by means of the ``phasing`` parameter, which in this 
case would be assigned a different value for alleles on each contig. 

File Format Specification
-------------------------

Files are YAML/JSON with a structure defined below. Files should be
encoded as UTF-8. Identifiers are case-sensitive. Files should have the
extension ``.yaml``, ``.yml``, or ``.json``.

File Structure
~~~~~~~~~~~~~~

The file structure has not been specified yet.

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

.. _AlleleDescriptionFields:

AlleleDescription Fields
-----------------------------

:download:`Download as TSV <../_downloads/AlleleDescription.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in AlleleDescription_schema %}
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

.. _UnrearrangedSequenceFields:

UnrearrangedSequence Fields
-----------------------------

:download:`Download as TSV <../_downloads/UnrearrangedSequence.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in UnrearrangedSequence_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _SequenceDelineationVFields:

SequenceDelineationV Fields
-----------------------------

:download:`Download as TSV <../_downloads/SequenceDelineationV.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in SequenceDelineationV_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _GenotypeSetFields:

GenotypeSet Fields
-----------------------------

:download:`Download as TSV <../_downloads/GenotypeSet.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in GenotypeSet_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _GenotypeFields:

Genotype Fields
-----------------------------

:download:`Download as TSV <../_downloads/Genotype.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in Genotype_schema %}
    * - ``{{ field.Name }}``
      - {{ field.Type }}
      - {{ field.Attributes }}
      - {{ field.Definition | trim }}
    {%- endfor %}

.. _MHCGenotypeSetFields:

MHCGenotypeSet Fields
-----------------------------

:download:`Download as TSV <../_downloads/MHCGenotypeSet.tsv>`

.. list-table::
    :widths: 20, 15, 15, 50
    :header-rows: 1

    * - Name
      - Type
      - Attributes
      - Definition
    {%- for field in MHCGenotypeSet_schema %}
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
