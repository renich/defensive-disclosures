===============================================
System and Method for Automated Medical Appointment Orchestration and Intake
===============================================

:Fecha: 2026-02-06
:Autor: René Bon Ćirić
:Estado: Publicación Defensiva

.. note::
   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.

Resumen Técnico
===============
Sistema de gestión de citas médicas automatizado diseñado para orquestar la programación de pacientes y la recepción clínica inicial a través de mensajería instantánea (ej. WhatsApp). El sistema se integra con calendarios médicos (ej. Google Calendar, expedientes clínicos electrónicos especializados) para proporcionar disponibilidad en tiempo real. Un agente conversacional emplea un árbol de decisiones clínicas para recopilar datos de "Pre-Consulta", incluyendo síntomas, historial médico y detalles del seguro. El sistema cuenta con un "Calificador de Triaje" que prioriza los casos urgentes para una programación inmediata mientras gestiona los seguimientos de rutina. Al automatizar la carga administrativa de la reserva de citas y la recopilación de datos, el sistema aumenta la capacidad de la clínica, reduce las tasas de inasistencia ("No-Show") mediante recordatorios automatizados y proporciona a los médicos un resumen estructurado del estado del paciente antes de que entre al consultorio.

Campo Técnico
=============
This disclosure relates to the field of Digital Health (HealthTech), automated scheduling systems, and conversational AI for clinical administrative workflows.

Antecedentes y Problema Técnico
===============================
Medical clinics often lose patients due to slow response times or the friction of calling a receptionist during business hours. Furthermore, doctors often spend the first 10 minutes of a consultation asking routine questions about history or symptoms. Existing online booking tools are often "passive" and do not collect the clinical context needed for triage. There is a need for an "Active" agent that can handle the entire patient entry process, from initial greeting to a confirmed, triaged appointment.

Descripción Detallada
=====================


Ejemplos de Realización
=======================
In one embodiment, the system includes a "Cancellation Filler" feature that, if a patient cancels an appointment, automatically reaches out to patients on a "Waitlist" who have similar triage scores to offer them the newly opened slot.

Reivindicación de Novedad
=========================
The system claims novelty in the combination of real-time calendar orchestration with adaptive clinical intake logic and a triage-based prioritization engine specifically designed for instant messaging environments, automating the "Pre-Consultation" lifecycle of a medical practice.

