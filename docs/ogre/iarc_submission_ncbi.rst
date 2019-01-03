Submission of IARC gene inference data to NCBI
==============================================

General outline
---------------

IARC submission currently follows a "INSDC first" approach, means that
all sequence data related to the reported inference is REQUIRED to be
properly deposited in a general purpose sequence repository before it is
reviewed by IARC. The submitter needs to complete the initial steps of
submission to one of the INSDC repositories. Upon submission to IARC,
some of this data will be pulled in from NCBI (TODO: What kind of data
can we actually pull down from INSDC?)

The aim of this procedure is to ensure that inferences reviewed by
IARC are public and will remain available in the long run. It is however
explicitly *not* the aim to provide data that deterministically will
yield the same inference results.


Deposition of inferred gene data at NCBI
----------------------------------------

At the end of the deposition process there should be three types of
records present at NCBI:

1. A single record containing the final and full-length inferred
   sequence. The record is deposited in one of the following:

   *  Genbank: All inferences that have been performed on the
      submitters own data CAN be submitted as [???] to Genbank. Note
      that Genbank typically only holds data that has a physical
      correlate which is not necessarily true for infered sequences.
      Nevertheless NCBI currently accepts this as a kind of consensus
      building if it is performed on your own data. The Genbank record
      MUST link to the ``select set`` record (see 3.) via the
      ``DBLINK/DR`` field. Genbank records will be publicly available
      independent of other publications. Note that the for Genbank, the ``DBLINK`` field does not appear to be available through the `BankIt <https://www.ncbi.nlm.nih.gov/WebSub/?tool=genbank>`_ submission interface. You can use ``Tbl2asn`` and ``Sequin``, and edit the ``DBLINK`` field manually (as "Sequence Read Archive" is not one of the options on the `template creation page <https://submit.ncbi.nlm.nih.gov/genbank/template/submission/>`_. A sample Genbank deposit can be found under accession `MK321694 <https://www.ncbi.nlm.nih.gov/nuccore/MK321694>`_.

   *  TPA (Third-party annotation): A segment of Genbank dedicated
      inferences. Also the TPA record MUST link to the ``select set``
      record (see 3.) via the ``DBLINK/DR`` field. Note that in contrast
      to Genbank, TPA does REQUIRE a peer-reviewed publication
      describing the details of the inference process before the record
      will be made publicly available. A sample TPA deposit can be found under accession `BK01573 <https://www.ncbi.nlm.nih.gov/nuccore/BK010573>`_.

   The format for both record types the Genbank format (link) with
   a standardized feature table (FT). Note that your initial submission
   MUST NOT contain any potential name for the gene as this will be
   assigned by IARC later on.

   TODO: Is there any metadata that should be provided into the GB
   record?

2. One or multiple SRA records containing all raw reads of the
   the respective sequencing run. Note that if you are performing
   inference using third-party data, these records MUST be submitted
   by the original owner of the data. These record type will typically
   be present before the other. The metadata annotation of the records
   SHOULD be MiAIRR compliant [Rebult et al.].

3. One or multiple SRA records containing the ``select set`` of reads
   from (2). The aim of these records is to document the number,
   quality, coverage and diversity of the reads in a dataset that
   _potentially_  support the inference. This means that the
   ``select set`` SHOULD be a superset of the reads that support the
   inference. It is NOT REQUIRED that inference tools deterministically
   return the inferred allele upon being fed with the ``select set``.
   Generation of the ``select set`` from the complete set is described
   below. When submitting the ``select set`` to SRA the metadata
   context, i.e. the original links to project, sample and
   (if possible) experiment) SHOULD be maintained. Reads originating
   from multiple subjects or samples MUST NOT be pooled into a single
   new entry. The new record SHOULD be titled "Reads from
   <original_run_accession> supporting inference of Homo sapiens
   immunoglobulin heavy chain variable gene” and contain a design
   description, e.g., “Experimental workflow as described in original
   SRA/ENA record [<run_accession>]. Gene inference was performed
   using <software+version+parameters>. The reported reads were
   selected based on <selection_criteria>.”

**NOTE:** It is reasonably likely, in the short term, that you will encounter questions from the SRA/ENA/Genbank staff about the nature of these deposits. If so, you can respond that they are made as part of a community effort to document novel alleles with an emphasis on transparency in data provenance. You can link to the `IARC page <https://www.antibodysociety.org/inferred-allele-review-committee-iarc/>`_ and note that we worked together with IMGT and Genbank/TPA staff in designing this procedure.

Generating the ``select set``
-----------------------------

Below is the current procedure describing how to generate a ``select
set`` using general purpose tools. This procedure was designed in a
rather generic fashion so that it is easy to implement and does NOT
REQUIRE inference tools to provide their own mechanisms. Note that it
is currently assumed that the procedure is not fully deterministic,
i.e. the ``select set`` cannot simply be generated using the complete
read data and the inferred sequence, as there are additional filter
criteria that apply. In addition the ``select set`` SHOULD not be
subject to any modifications that are not listed below. This includes
UMI-based consensus building or other aggregation steps that are not
fully transparent to a third-party.

1. Assemble paired-end reads. The two reads MUST overlap. Recommended
   tool: PandaSeq
2. Perform PHRED filtering that is equivalent to the one performed by 
   inference pipeline.	Recommened tool: Immcantination suite
3. Perform a `blastn` serch using the data from (2.) as query and bp
   1-312 of the inferred gene as reference library. Require matches to be
   full-length and >99.6% ID. Record all matching read ID. Recommended
   tool: NCBI BLAST
4. Select the reads with the read ID found in (3.) from the original
   unmerged FASTQs. Note that each ``select set`` MUST be derived from
   a single donor and sample. Recommended tool: Christian's cryptic
   extractor script
5. Submit the ``select set`` to SRA
