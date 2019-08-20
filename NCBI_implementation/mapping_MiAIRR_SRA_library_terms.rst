Mapping MiAIRR to NCBI SRA library_* terms
==========================================

SRA requires that each record is tagged with four ``library_*`` terms
upon submission. There is no direct mapping between the MiAIRR
``library_generation_method`` and ``template_class`` keywords and the
SRA terms. Therefore this document aims to provide a basic guidance on
how to perform reasonable MiAIRR-to-SRA mapping:

   * ``library_strategy``: Will be ``AMPLICON`` for the majority of
     current applications, ``RNA-Seq`` for whole transcriptome.

   * ``library_source``: ``GENOMIC`` for DNA, ``TRANSCRIPTOMIC`` for
     RNA, ``SYNTHETIC`` for synthetic libraries.

   * ``library_selection``: Should typically be one of ``PCR``,
     ``RT-PCR``, ``cDNA`` or ``RACE``.

   * ``library_layout``: This term does primarily describe the
     sequencing process, rather than library construction. See `Mapping
     to library_layout`_.


Mapping from library_generation_method
--------------------------------------

The following list enumerates the currently accepted values for the
``library_generation_method`` keyword. The values given in "SRA mapping"
are listed in the order `library_strategy``, ``library_source``,
``library_selection``. If there are multiple mappings for a given
method, the distinction can be made based on the criteria listed in
"requires". Note that while ``template_class`` is currently redundant as
its information is fully contained in ``library_generation_method``, it
is nevertheless a REQUIRED keyword in the MiAIRR data standard.

   * PCR: Conventional PCR on genomic DNA.
      - requires: ``template_class`` = ``DNA`` AND NOT ``synthetic``
      - SRA mapping: ``AMPLICON``, ``GENOMIC``, ``PCR``

   * PCR: Conventional PCR on synthetic DNA.
      - requires: ``template_class`` = ``DNA`` AND ``synthetic``
      - SRA mapping: ``AMPLICON``, ``SYNTHETIC``, ``PCR``

   * RT(RHP)+PCR: RT-PCR using random hexamer primers.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(oligo-dT)+PCR: RT-PCR using oligo-dT primers.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(oligo-dT)+TS+PCR: 5'-RACE PCR (i.e. RT is followed by a template
     switch (TS) step) using oligo-dT primers.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(oligo-dT)+TS(UMI)+PCR: 5'-RACE PCR using oligo-dT primers and
     template switch primers containing unique molecular identifiers
     (UMI), i.e. the 5' end is UMI-coded.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+PCR: RT-PCR using transcript-specific primers.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(specific)+TS+PCR: 5'-RACE PCR using transcript-specific primers.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+TS(UMI)+PCR: 5'-RACE PCR using transcript-specific
     primers and template switch primers containing UMIs.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific+UMI)+PCR: RT-PCR using transcript-specific primers
     containing UMIs (i.e. the 3' end is UMI-coded).
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(specific+UMI)+TS+PCR: 5'-RACE PCR using transcript-specific
     primers containing UMIs (i.e. the 3' end is UMI-coded).
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+TS: RT-based generation of dsDNA **without**
     subsequent PCR. This is used by RNA-seq kits.
      - requires: ``template_class`` = ``RNA``
      - SRA mapping: ``RNA-Seq``, ``TRANSCRIPTOMIC``, ``RACE``

   * other: Any methodology not covered above.


Mapping to library_layout
-------------------------

NCBI currently defines two possible values for the `library_layout`
term (``single`` and ``paired``) to describe whether a library has been
subjected to paired-end sequencing or not. MiAIRR does not specify a
dedicated field for this information as it was considered more important
to annotate whether a sequence is a ``complete_sequence`` or not.

Therefore the information for ``library_layout`` has to be derived from
the ``read_length`` keyword, which contains a JSON array with one or two
positive integer values, providing the maximum length of each read
direction. The existence of a non-zero second value SHOULD be
interpreted as indication for ``paired``-end sequencing.
