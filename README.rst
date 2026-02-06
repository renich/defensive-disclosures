============================
Defensive Disclosure Archive
============================

:Maintainer: René Bon Ćirić (Rénich)
:License: Creative Commons Attribution 4.0 International (CC BY 4.0)
:DOI Status: Indexed via Zenodo

Purpose & Legal Status
======================
This repository serves as a permanent, immutable record of technical innovation to establish **Prior Art** under:

* **35 U.S.C. § 102** (United States)
* **Ley Federal de Protección a la Propiedad Industrial** (Mexico)
* **Article 54 of the EPC** (European Patent Convention)

**To Patent Examiners and Competitors:**

The mechanisms, algorithms, and system architectures described herein have been publicly disclosed with cryptographic timestamping via Zenodo. Any subsequent attempt to patent these specific technical implementations (or obvious variations thereof) will be challenged using these records as invalidating prior art.

System Architecture
===================
The repository implements a hardened, automated pipeline for defensive publication.

Automation Infrastructure
------------------------
* **Generation Engine (bin/generator.py):** An LLM-powered drafting tool that transforms structured concepts (via `ideas.json`) into rigorous technical disclosures. It enforces jurisdictional requirements for both USPTO (USA) and IMPI (Mexico).
- **Hardened Security:** Includes input sanitization (CWE-22 mitigation) and secure shell execution.
- **Alice/Mayo Compliance:** Strictly engineered to describe "Technical Realization" rather than abstract business logic.
* **Indexing (bin/update_index.py):** Automatically maintains jurisdictional sub-indices and root documentation hierarchy.
* **Orchestration (GNUmakefile):** Provides a unified interface for generation, indexing, and PDF compilation via Pandoc.

Automated Publishing Pipeline
-----------------------------
This system leverages a "Distributed Cryptographic System" for legal proof of existence:

#. **Git Integrity:** Every disclosure is cryptographically hashed via Git commits.
#. **CI/CD Trigger:** GitHub Actions (`.github/workflows/publish.yml`) detect changes in the `ideas/` directory.
#. **Permanent Archival:** Automated Releases trigger Zenodo to mint a permanent, immutable **Digital Object Identifier (DOI)**.

Usage
=====

Environment Setup
-----------------
The generator requires an OpenAI API key and allows for jurisdictional overrides:

.. code-block:: bash

   export OPENAI_API_KEY='your-key-here'
   export DISCLOSURE_AUTHOR='Your Name'
   export OPENAI_MODEL='gpt-4-turbo'

Generation & Indexing
---------------------
To process new ideas from ``ideas.json``:

.. code-block:: bash

   make all

This command executes:
1. ``make generate``: LLM drafting of missing disclosures.
2. ``make index``: Rebuilding of RST toctrees.
3. ``make pdf``: Compilation of PDF artifacts in the ``build/`` directory.

Engagement & Commercialization
==============================
While the *ideas* disclosed herein are dedicated to the public domain to ensure freedom to operate, the **execution expertise, specific code implementations, and trade secret optimizations** remain with the author.

We are open to:

* **Consulting & Implementation:** If you wish to deploy these systems.
* **Strategic Partnerships:** For joint development.
* **Prior Art Citations:** If you are filing a related (but distinct) patent, you are legally required to cite these documents.

Contact
-------
renich@woralelandia.com / +52 33 3576-5013

Licensing & Usage
-----------------
This repository and its contents (Technical Disclosures) are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.

**You are free to:**
* **Share** — copy and redistribute the material in any medium or format.
* **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

**Under the following terms:**
* **Attribution** — You must give appropriate credit (citing the Author and the DOI), provide a link to the license, and indicate if changes were made.
