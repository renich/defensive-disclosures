============================================================================
System and Method for Automated Candidate Screening and Technical Assessment
============================================================================

:Date: 2026-02-06
:Author: René Bon Ćirić
:Status: Defensive Publication

.. note::
   This document constitutes a Defensive Publication. It discloses technical mechanisms to prevent patenting of the described methods by establishing prior art.

Abstract
========
An automated recruitment system designed to perform high-scale screening and technical ranking of job candidates. The system features a multi-format ingestion engine that parses resumes (PDF/DOCX), extracting structured data such as work history, technical skills, and educational background using Named Entity Recognition (NER). A "Requirement Matcher" evaluates extracted data against a specific job description (JD), assigning a weighted "Compatibility Score." The system also incorporates an automated "Asynchronous Interviewer" that delivers sector-specific technical questions via chat or video, evaluating responses using LLMs to verify technical depth and communication skills. By filtering hundreds of applicants into a ranked "Shortlist" of qualified talent, the system significantly reduces the "Time-to-Hire" for HR departments and technical leads.

Technical Field
===============
This disclosure relates to the field of Human Resources Technology (HRTech), automated document parsing, and AI-driven candidate assessment.

Background & Problem Statement
==============================
Recruitment in the digital age often results in hundreds of applications for a single position. A significant portion of these applicants may lack the fundamental technical requirements, yet recruiters must spend hours manually reviewing resumes to find the "hidden gems." Furthermore, a resume often fails to convey the actual technical depth of a candidate. There is a need for a system that can not only "read" a resume but also "test" the candidate's claims automatically before a human interview takes place.

Detailed Description
====================


Specific Embodiments
====================
In one embodiment, the system includes a "Bias Mitigation" mode that masks a candidate's name, gender, and age during the initial screening process, ensuring that the ranking is based purely on technical merit and experience.

Claims of Novelty
=================
The system claims novelty in the combination of NER-based resume parsing with an LLM-driven asynchronous technical assessment bot, specifically focusing on the automated "validation" of claimed skills through open-ended technical questions before human involvement.

