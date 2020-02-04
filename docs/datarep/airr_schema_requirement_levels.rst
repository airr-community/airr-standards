.. _Requirement_Levels:

========================================
Requirement Levels of AIRR Schema Fields
========================================


Clarification of Terms
======================

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in [RFC2119]_.

Categories of AIRR Schema Fields
================================

-  MiAIRR fields (``miairr=true``) are either REQUIRED or RECOMMENDED,
   but never OPTIONAL, as this would be in conflict with the idea of
   a minimal information standard.
-  Non-MiAIRR fields can have all three requirement levels.
-  Fields are REQUIRED if and only if they are critical for the
   meaningful interpretation of the data. Importantly, fields are
   **not** elevated to REQUIRED based on the fact that the respective
   information can be expected to be available to the data generator.
   This was decided to simplify MiAIRR-compliant data annotation by
   third parties, who might perform annotation based on publicly
   available information only.
-  REQUIRED fields MUST NOT contain a value that is ``NULL`` or
   ``NULL``-like. ``NULL``-like values currently include the terms:

   -  ``not_applicable``: There is no meaningful value for this key due
      to study design (e.g. ``sex`` for a phage library).
   -  ``not_collected``: Data for this field was not collected during
      the study.
   -  ``missing``: Data for field was collected, but is not available
      now.

This results in the following table that maps the requirement levels
to the respective ``x-airr`` terms:

.. _Table_1:

+-------------------------------+--------------+--------------+
| AIRR schema requirement level | ``required`` | ``nullable`` |
+===============================+==============+==============+
| REQUIRED                      | ``true``     | ``false``    |
+-------------------------------+--------------+--------------+
| RECOMMENDED                   | ``true``     | ``true``     |
+-------------------------------+--------------+--------------+
| OPTIONAL                      | ``false``    | ``false``    |
+-------------------------------+--------------+--------------+


References
==========

.. [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
   <https://tools.ietf.org/html/rfc2119>
