===============================================
System and Method for Automated Trademark Surveillance and Similarity Detection
===============================================

:Date: 2026-02-06
:Author: René Bon Ćirić
:Status: Defensive Publication

.. note::
   This document constitutes a Defensive Publication. It discloses technical mechanisms to prevent patenting of the described methods by establishing prior art.

Abstract
========
An automated trademark monitoring system designed to protect intellectual property by detecting similar trademark applications in official gazettes (e.g., Mexico's IMPI "Gaceta de la Propiedad Industrial"). The system utilizes a high-frequency ingestion engine to capture new applications and a dual-path analysis engine. The first path performs phonetic and orthographic similarity analysis on text-based marks using specialized distance algorithms (e.g., Levenshtein, Metaphone). The second path utilizes computer vision and feature-extraction models to identify visual similarities in logos and figurative marks. By cross-referencing new filings against a client's "Watch List" of protected brands and Nice Classes, the system provides early-warning alerts, enabling legal teams to file oppositions within the narrow statutory windows provided by law.

Technical Field
===============
This disclosure relates to the field of Intellectual Property (IP) technology, automated image recognition, and legal monitoring systems.

Background & Problem Statement
==============================
Trademark protection requires proactive enforcement. When a third party attempts to register a brand that is "confusingly similar" to an existing one, the owner must file an opposition. However, thousands of trademarks are filed every month. Manual review of the official Gaceta is slow and often misses similar-sounding names or visually similar logos. If the opposition window is missed, the owner must resort to more expensive and uncertain cancellation proceedings.

Detailed Description
====================


Specific Embodiments
====================
In one embodiment, the system includes a "Global Risk Map" that monitors trademark filings across multiple jurisdictions (WIPO, USPTO, EUIPO), providing a unified dashboard for multinational brand protection.

Claims of Novelty
=================
The system claims novelty in the combination of Spanish-optimized phonetic similarity algorithms with deep-learning-based figurative mark analysis applied specifically to the automation of official trademark gazette monitoring for the purpose of legal opposition.

