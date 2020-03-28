.. _RequirementLevels:

========================================
Requirement Levels of AIRR Schema Fields
========================================

Clarification of Terms
======================

-  The terms "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT",
   "RECOMMENDED", "MAY" and "OPTIONAL" are to be interpreted as
   described in [RFC2119]_.
-  The terms "IF" and "ONLY IF" are are to be interpreted as sufficent
   and necessary requirement, respectively.
-  The term "NULL-LIKE" is an extension of the ``NULL`` term in SQL and
   its equivalents in other programming languages, referring to the
   absence of data in a field (i.e., the field is empty). NULL-LIKE
   **additionally** includes the following terms, which also define the
   reason why the information is missing. As these terms are expected to
   be provided as text, the field would not be ``NULL`` but nevertheless
   NULL-LIKE (i.e., it lacks biologically interpretable information).

   -  ``not_applicable``: There is no meaningful value for this field
      due to study design (e.g., ``sex`` for a phage library).
   -  ``not_collected``: Data for this field was not collected during
      the study.
   -  ``missing``: Data for field was collected, but is not available
      now.


Categories of AIRR Schema Fields
================================

-  Fields MUST be indicated by the ``x-airr:miairr`` property IF and
   ONLY IF the field or its content is governed by the MiAIRR data
   standard [Rubelt_2017]_.
-  The ``x-airr:miairr`` property MUST be assigned to one of the
   following three requirement levels:

   -  ``essential``: Information on this field MUST be provided and is
      considered critical for the meaningful interpretation of the data.
      Therefore the value of such a field MUST NOT be NULL-LIKE. Due to
      this strict requirement, this level is only assigned to a small
      set of fields. Importantly, fields are **not** elevated to this
      level based on the fact that the respective information should
      typically be available to the data generator. This was decided to
      simplify MiAIRR-compliant data annotation by third parties, who
      might perform this task based on publicly available information
      only.
   -  ``important``: Information for this field MUST be provided.
      However, the field MAY be assigned a NULL-LIKE value if the
      respective information is not available. The majority of fields
      governed by the MiAIRR data standard are assigned to this level.
   -  ``defined``: Information for this field MAY be provided. However,
      IF information matching the semantic definition of the field is
      provided, this field MUST be used for reporting.


Compliance with the MiAIRR Data Standard
========================================

-  Compliance to the MiAIRR Data Standard is currently a binary state,
   i.e., a data either is or is not compliant, there are not "grades"
   of compliance. However, additional requirements for specific use
   cases might be defined in the future.
-  Data sets are considered MiAIRR-compliant ONLY IF all ``essential``
   and ``important`` fields are reported.
-  Note that ``important`` fields with NULL-LIKE values MUST NOT be
   dropped from a data set.
-  Implementors of data entry interfaces SHOULD NOT set the default
   value of ``important`` fields to NULL-LIKE values, i.e., users should
   be required to actively select the values.
