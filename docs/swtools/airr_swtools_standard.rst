AIRR Software WG - Guidance for AIRR Software Tools
---------------------------------------------------

Version 1.0

Introduction
------------

The `Adaptive Immune Receptor Repertoire (AIRR) Community`_ will benefit
greatly from cooperation among groups developing software tools and
resources for AIRR research. The goal of the `AIRR Software Working Group`_
is to promote standards for AIRR software tools and resources in order
to enable rigorous and reproducible immune repertoire research at the
largest scale possible. As one contribution to this goal, we have
established the following standards for software tools. Authors whose
tools comply with this standard will, subject to ratification from the
AIRR Software WG, be permitted to advertise their tools as being
AIRR-compliant.

.. _`Adaptive Immune Receptor Repertoire (AIRR) Community`: https://www.antibodysociety.org/airrc/
.. _`AIRR Software Working Group`: https://www.antibodysociety.org/software-working-group/

Requirements
------------

Tools must:

1. Be published in source code form, and hosted on a publicly available
       repository with a clear versioning system.

2. Support community-curated standard file formats and strive for
       modularity and interoperability with other tools. In particular,
       tools must read and write :ref:`DataRepresentations` standards corresponding to their tool.
	   
3. Include example data (in AIRR standard formats where applicable) and
       checks for expected output from that data, in order to provide a
       minimal example of functionality allowing users to check that the
       software is performing as described.

4. Provide information about run parameters as part of output.

5. Provide a container build file that can be used to create an image
       which encapsulates the software tool, its dependencies, and
       required run environment. This needs to be remotely and
       automatically built. We currently recognize two software
       solutions, although we will adapt as software evolves:

   a. A `Dockerfile`_ that automatically builds a `container
      image`_ on `Docker Hub`_
		  
.. _`Dockerfile`: https://docs.docker.com/engine/reference/builder/
.. _`container image`: https://docs.docker.com/docker-hub/builds/
.. _`Docker Hub`: https://docs.docker.com/docker-hub/

   b. A `Singularity recipe file`_ that `automatically builds a container image`_ 
      on `Singularity Hub`_.

.. _`Singularity recipe file`: https://www.sylabs.io/docs/	
.. _`automatically builds a container image`: https://github.com/singularityhub/singularityhub.github.io/wiki/Automated-Build
.. _`Singularity Hub`: https://singularity-hub.org/	  
		  
6. Provide user support, clearly stating which level of support users
       can expect, and how and from whom to obtain it.

Recommendation
--------------

We suggest software tools be published under a license that permits free
access, use, modification, and sharing, such as GPL, Apache 2.0, or MIT.
However, we understand that this depends on institutional IP
restrictions, thus it is a recommendation rather than a requirement.

Explanatory Notes
-----------------

Open Source Software, Versioned Repositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software tools in the AIRR field are evolving rapidly. In the interests
of reproducibility and transparency, published work should be based on
tools (and versions of tools) that can be obtained easily by other
researchers in the future. To that end, AIRR compliant tools must be
published in open repositories such as GitHub or Bitbucket, and we
encourage publishing the specifics on the version and configuration of
tools that thave been employed.

Community-Curated File Formats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AIRR Data Representation Working Group has defined standards for
immune receptor repertoire sequencing datasets. Software tool authors
are requested to support these standards as much as possible, for
applicable data sets. The currently implemented standard covers
submission of reads to NCBI repositories (BioProject, BioSample, SRA and
Genbank) and annotated immune receptor rearrangements. Tool authors can
assist by easing/guiding the process of submission as much as possible.

Example Data and Checks
~~~~~~~~~~~~~~~~~~~~~~~

Because the installation and operation of the tools in this field may be
complex, we require example data and details of expected output, so that
users can confirm that their installation is functioning as expected.
Furthermore, metadata (such as for example germline gene libraries) and
other software dependenciesshould be checked when the tool runs, and
informative error messages issued if necessary.

Dependencies and Containers
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Containers

Containers encapsulate everything needed to run a piece of software into
a single convenient executable that is largely independent of the user’s
software environment. For the following purposes, providers of
AIRR-compliant tools must provide a containerized implementation (based
on a published build script as described above) as one download option
that users can choose:

-  Containers allow users to use and evaluate a tool easily and
       reproduce results, without the need to resolve dependencies,
       configure the environment, etc.

-  Having these containers be automatically built also provides a
       self-validated way to understand the fine details of installation
       from a known starting point.

To ensure that containers are up to date,they must be built
automatically when the current release version of the tool is updated.
We will use automated builds on Docker Hub and Singularity Hub for this
purpose. The corresponding build files document dependencies clearly,
and make it easy for the maintainer to keep the container’s dependencies
up to date in subsequent releases.

An example Docker container is provided by the Software WG on
`GitHub`_. This example encapsulates `IgBLAST`_, and implements
the `bioboxes`_ command-line standard.

.. _`GitHub`: https://github.com/airr-community/software-wg
.. _`IgBLAST`: https://www.ncbi.nlm.nih.gov/igblast/
.. _`bioboxes`: http://bioboxes.org


Analysis Workflows

-  At the moment, we do not endorse a specific workflow technology
       standard:

   -  Technology is evolving too rapidly for us to commit to a
          particular workflow.

   -  Typically, AIRR analysis tools have many options and modes, which
          would make it difficult to support a ‘plug and play’
          environment without unduly restricting functionality.

-  As tools and workflows evolve, we will keep the position under review
       and may make stronger technology recommendations in the future.

-  We strongly encourage authors of tools to provide concrete,
       documented, examples of workflows that employ their tools,
       together with sample input and output data.

-  Likewise we encourage authors of research publications to provide
       documented workflows that will enable interested readers to
       reproduce the results.

Standard Data Sets
~~~~~~~~~~~~~~~~~~

The WG is working on the development and evaluation of simulated data
sets. Lists of published real-world datasets are maintained in the
`AIRR Forum Wiki`_.

.. _`AIRR Forum Wiki`: https://b-t.cr/c/wiki

Support Statements
~~~~~~~~~~~~~~~~~~

Tool authors must provide support for the tool. They must state
explicitly what level of support is provided, and explain how support
can be obtained. We recommend a method such as the issues tracker on
Github, that publishes support requests transparently and links
resolutions to specific versions or releases. Users are advised to check
that the level of support and the frequency of software updates matches
their expectations before committing to a tool.

Ratification
------------

Authors may submit tools to the AIRR Software WG requesting ratification
against the standard. The submission must include reviewable and
itemised evidence of compliance with each Requirement listed above.

The Software WG will, where appropriate, issue a Certificate of
Compliance, stating the version of the tool reviewed and the version of
the Standard with which compliance was ratified. After receiving a
Certificate, authors will be entitled to claim compliance with the
Standard, and may incorporate any artwork provided by AIRR for that
purpose.

The Software WG will maintain and publish a list of compliant software.

If a tool does not achieve ratification, the Software WG will provide an
explanation. The Software WG encourages resubmission once issues have
been resolved.

Authors must re-submit tools for ratification following major upgrades
or substantial modifications. The Software WG may, at its discretion,
request resubmission at any time. If a certified tool subsequently fails
ratification, or is not re-submitted in response to a request from the
Software WG, AIRR compliance may no longer be claimed and the associated
artwork may no longer be used.

The Software WG may, at its discretion, issue a new version of this
standard at any time. Tools certified against previous version(s) of the
standard may continue to claim compliance with those versions and to use
the associated artwork. Authors wishing to claim compliance with the new
version must submit a new request for certification and may not claim
compliance with the new version, or use associated artwork, until and
unless certification is obtained.
