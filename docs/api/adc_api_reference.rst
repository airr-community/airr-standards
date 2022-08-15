.. _DataCommonsAPIReference:

ADC API Reference Implementation
================================

The AIRR Community provides a reference implementation for an ADC API
service. The reference implementation can be utilized for any number
of tasks. For example, a data repository might use the source code as
a starting point for their own implementation and can compare the
behaviour of their service against the reference. Another example is a
tool developer, who wishes to use the API, can setup a local data
repository so they can develop and test their tool before sending API
requests across the internet to remote data repositories. While the
reference implementation is functionally complete, it has minimal
security and no optimizations for large data so it should not be used
directly for production systems.

The reference implementation consists of three GitHub repositories:
`adc-api`_, `adc-api-js-mongodb`_, and `adc-api-mongodb-repository`_.
The three repositories correspond to the top-level service composition
(adc-api), a JavaScript web service that responds to API requests and
queries a MongoDB database (adc-api-js-mongodb), and a MongoDB
database for holding AIRR-seq data
(adc-api-mongodb-repository). Docker and docker-compose are used to
provide a consistent deployment environment and compose the multiple
components together into a single service. Complete documentation for
configuring and deploying the reference implementation is available in
the adc-api repository.


.. _`adc-api`: https://github.com/airr-community/adc-api
.. _`adc-api-js-mongodb`: https://github.com/airr-community/adc-api-js-mongodb
.. _`adc-api-mongodb-repository`: https://github.com/airr-community/adc-api-mongodb-repository
