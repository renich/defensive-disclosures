============================================================================
System and Method for Automated Medical Appointment Orchestration and Intake
============================================================================

:Date: 2026-02-06
:Author: René Bon Ćirić
:Status: Defensive Publication

.. note::
   This document constitutes a Defensive Publication. It discloses technical mechanisms to prevent patenting of the described methods by establishing prior art.

Abstract
========
An automated medical appointment management system designed to orchestrate patient scheduling and initial clinical intake via instant messaging (e.g., WhatsApp). The system integrates with medical calendars (e.g., Google Calendar, specialized EHRs) to provide real-time availability. A conversational agent employs a clinical decision-tree to collect "Pre-Consultation" data, including symptoms, medical history, and insurance details. The system features a "Triage Scorer" that prioritizes urgent cases for immediate scheduling while managing routine follow-ups. By automating the administrative burden of appointment booking and data collection, the system increases clinic throughput, reduces "No-Show" rates via automated reminders, and provides physicians with a structured summary of the patient's condition before they enter the consultation room.

Technical Field
===============
This disclosure relates to the field of Digital Health (HealthTech), automated scheduling systems, and conversational AI for clinical administrative workflows.

Background & Problem Statement
==============================
Medical clinics often lose patients due to slow response times or the friction of calling a receptionist during business hours. Furthermore, doctors often spend the first 10 minutes of a consultation asking routine questions about history or symptoms. Existing online booking tools are often "passive" and do not collect the clinical context needed for triage. There is a need for an "Active" agent that can handle the entire patient entry process, from initial greeting to a confirmed, triaged appointment.

Detailed Description
====================


Specific Embodiments
====================
In one embodiment, the system includes a "Cancellation Filler" feature that, if a patient cancels an appointment, automatically reaches out to patients on a "Waitlist" who have similar triage scores to offer them the newly opened slot.

Claims of Novelty
=================
The system claims novelty in the combination of real-time calendar orchestration with adaptive clinical intake logic and a triage-based prioritization engine specifically designed for instant messaging environments, automating the "Pre-Consultation" lifecycle of a medical practice.

