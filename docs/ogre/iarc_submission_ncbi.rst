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
      submitters own data can be submitted as ??? to Genbank. Note that
      Genbank typically only holds data that has a physical correlate
      which is not necessarily true for infered sequences.

   *  TPA (Third-party annotation): A segment of Genbank dedicated
      inferences. Note that in contrast to Genbank, TPA does require
      a peer-reviewed publication describing the details of the
      inference process.

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
   quality, coverage and diversity of the reads in a dataset that _potentially_  support the inference. This means that the
   ``select set`` SHOULD be a superset of the reads that support the
   inference. It is NOT REQUIRED that inference tools deterministically return the inferred allele upon being fed with the ``select set``.
   Generation of the ``select set`` from the complete set is described
   below.


Generating the ``select set``
-----------------------------

Below is the current procedure describing how to generate a ``select
set`` using general purpose tools. This procedure was designed in a
rather generic fashion so that it is easy to implement and does NOT
REQUIRE inference tools to provide their own mechanisms. Note that it
is currently assumed that the procedure is not fully deterministic,
i.e. the ``select set`` cannot simply be generated using the complete
read data and the inferred sequence, as there are additional filter
criteria that apply.

1. Assemble paired-end reads. The two reads MUST overlap. Recommended
   tool: PandaSeq
2. Perform PHRED filtering that is equivalent to the one performed by 
   inference pipeline.	Recommened tool: Immcantination suite
3. Perform a `blastn` serch using the data from (2.) as query and bp
   1-312 of the inferred gene as reference library. Require matches to be
   full-length and >99.6% ID. Record all matching read ID. Recommended
   tool: NCBI BLAST
4. Select the reads with the read ID found in (3.) from the original
   unmerged FASTQs. Recommended tool: Christian's cryptic extractor script
5. Submit the ``select set`` to SRA
