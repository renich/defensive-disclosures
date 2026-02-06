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
The repository implements a hardened, **Zero-Dependency** automated pipeline for defensive publication.

Automation Infrastructure
-------------------------
* **The Brain (instructions.rst):** Centralized clinical guidelines that enforce technical rigor, "PHOSITA" enabling descriptions, and "Alice/Mayo" doctrine compliance.
* **Native Engine (bin/generate_native.py):** A dependency-free Python script utilizing only the Standard Library (`urllib`, `json`) to communicate with local LLM servers (e.g., Ollama/OpenCode).
* **Indexing (bin/update_index.py):** Automatically maintains jurisdictional sub-indices and root documentation hierarchy.
* **Orchestration (GNUmakefile):** Unified interface for generation, indexing, and PDF compilation via Pandoc.

Automated Publishing Pipeline
-----------------------------
This system leverages a "Distributed Cryptographic System" for legal proof of existence:

#. **Git Integrity:** Every disclosure is cryptographically hashed via Git commits.
#. **CI/CD Trigger:** GitHub Actions (`.github/workflows/publish.yml`) detect changes in the `ideas/` directory.
#. **Permanent Archival:** Automated Releases trigger Zenodo to mint a permanent, immutable **Digital Object Identifier (DOI)**.

Usage
=====

Agent-Driven SOP (Standard Operating Procedure)
-----------------------------------------------
The preferred workflow uses the **Opencode Agent** directly as the generation engine:

1. Add a new concept to ``ideas.json``.
2. Provide the Agent with the **SOP Prompt** (found in project documentation).
3. The Agent reads ``instructions.rst`` and the jurisdictional templates to write the ``.rst`` files directly.
4. Run ``make publish`` to finalize.

Manual/Native Pipeline
----------------------
The system supports a zero-dependency local pipeline:

.. code-block:: bash

   # 1. Start your local LLM server (e.g., Ollama)
   # 2. Run the automated publication cycle
   make publish

By default, this connects to ``http://localhost:11434/v1``. You can override settings via environment variables:

.. code-block:: bash

   export OPENAI_BASE_URL="http://your-server:port/v1"
   export OPENAI_MODEL="your-model-id"
   make publish

Engagement & Commercialization
==============================
While the *ideas* disclosed herein are dedicated to the public domain to ensure freedom to operate, the **execution expertise, specific code implementations, and trade secret optimizations** remain with the author.

Contact
-------
renich@woralelandia.com / +52 33 3576-5013

Licensing & Usage
-----------------
This repository and its contents are licensed under **CC BY 4.0**. You are free to share and adapt the material as long as you provide appropriate attribution (citing the Author and the DOI).
