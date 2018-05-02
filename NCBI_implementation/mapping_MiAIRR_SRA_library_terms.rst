Mapping NCBI SRA library terms
==============================

SRA requires that each record is tagged with three ``library_*`` terms
upon submission. There is currently no direct mapping between the
MiAIRR ``template_class`` and ``library_generation_method`` keywords
and the SRA terms, but this files should provide some guidance on how
to perform reasonable mapping:

   * Strategy: Will be ``AMPLICON`` for the majority of current
     applications, ``RNA-Seq`` for whole transcriptome.

   * Source: ``GENOMIC`` for DNA, ``TRANSCRIPTOMIC`` for RNA,
     ``SYNTHETIC`` for synthetic libraries.

   * Selection: Should typically be one of ``PCR``, ``RT-PCR``, ``cDNA``
     or ``RACE``.


Current MiAIRR terms
--------------------

While ``template_class`` can only be ``DNA`` or ``RNA``, the possible
values for ``library_generation_method`` are more complex:

   * PCR: Conventional PCR on genomic DNA.
      - REQUIRES: ``template_class`` = ``DNA`` AND NOT ``synthetic``
      - SRA mapping: ``AMPLICON``, ``GENOMIC``, ``PCR``

   * PCR: Conventional PCR on synthetic DNA.
      - REQUIRES: ``template_class`` = ``DNA`` AND ``synthetic``
      - SRA mapping: ``AMPLICON``, ``SYNTHETIC``, ``PCR``

   * RT(RHP)+PCR: RT-PCR using random hexamer primers.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(oligo-dT)+PCR: RT-PCR using oligo-dT primers.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(oligo-dT)+TS+PCR: 5'-RACE PCR (i.e. RT is followed by a template
     switch (TS) step) using oligo-dT primers.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(oligo-dT)+TS(UMI)+PCR: 5'-RACE PCR using oligo-dT primers and
     template switch primers containing unique molecular identifiers
     (UMI), i.e. the 5' end is UMI-coded.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+PCR: RT-PCR using transcript-specific primers.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(specific)+TS+PCR: 5'-RACE PCR using transcript-specific primers.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+TS(UMI)+PCR: 5'-RACE PCR using transcript-specific
     primers and template switch primers containing UMIs.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific+UMI)+PCR: RT-PCR using transcript-specific primers
     containing UMIs (i.e. the 3' end is UMI-coded).
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RT-PCR``

   * RT(specific+UMI)+TS+PCR: 5'-RACE PCR using transcript-specific
     primers containing UMIs (i.e. the 3' end is UMI-coded).
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``AMPLICON``, ``TRANSCRIPTOMIC``, ``RACE``

   * RT(specific)+TS: RT-based generation of dsDNA **without**
     subsequent PCR. This is used by RNA-seq kits.
      - REQUIRES: ``template_class`` = ``RNA``
      - SRA mapping: ``RNA-Seq``, ``TRANSCRIPTOMIC``, ``RACE``
