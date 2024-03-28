AIRR Data Commons API Release Notes
================================================================================

Version 2.0: June 2024
--------------------------------------------------------------------------------

**Version 2.0 ADC API release.**

General ADC API Changes:

1. Operators ``is`` and ``not`` have been depcreated. These operators based on the GDC API
are non-inutitive in that the ``not`` operator is not the boolean ``not`` operator. These operators 
were functionally equivalent to the more aptly named ``is missing`` and ``is not missing`` operators,
which still remain and should be used.

