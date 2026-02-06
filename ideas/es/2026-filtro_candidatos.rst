===============================================
System and Method for Automated Candidate Screening and Technical Assessment
===============================================

:Fecha: 2026-02-06
:Autor: René Bon Ćirić
:Estado: Publicación Defensiva

.. note::
   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.

Resumen Técnico
===============
Sistema de reclutamiento automatizado diseñado para realizar el filtrado y la clasificación técnica a gran escala de candidatos a puestos de trabajo. El sistema cuenta con un motor de ingesta multiformato que analiza currículos (PDF/DOCX), extrayendo datos estructurados como historial laboral, habilidades técnicas y formación académica mediante el reconocimiento de entidades nombradas (NER). Un "Calificador de Requisitos" evalúa los datos extraídos frente a una descripción de puesto (JD) específica, asignando una "Puntuación de Compatibilidad" ponderada. El sistema también incorpora un "Entrevistador Asíncrono" automatizado que entrega preguntas técnicas específicas del sector a través de chat o video, evaluando las respuestas mediante LLM para verificar la profundidad técnica y las habilidades de comunicación. Al filtrar cientos de solicitantes en una "Lista Corta" clasificada de talento calificado, el sistema reduce significativamente el "Tiempo de Contratación" para los departamentos de RRHH y los líderes técnicos.

Campo Técnico
=============
This disclosure relates to the field of Human Resources Technology (HRTech), automated document parsing, and AI-driven candidate assessment.

Antecedentes y Problema Técnico
===============================
Recruitment in the digital age often results in hundreds of applications for a single position. A significant portion of these applicants may lack the fundamental technical requirements, yet recruiters must spend hours manually reviewing resumes to find the "hidden gems." Furthermore, a resume often fails to convey the actual technical depth of a candidate. There is a need for a system that can not only "read" a resume but also "test" the candidate's claims automatically before a human interview takes place.

Descripción Detallada
=====================


Ejemplos de Realización
=======================
In one embodiment, the system includes a "Bias Mitigation" mode that masks a candidate's name, gender, and age during the initial screening process, ensuring that the ranking is based purely on technical merit and experience.

Reivindicación de Novedad
=========================
The system claims novelty in the combination of NER-based resume parsing with an LLM-driven asynchronous technical assessment bot, specifically focusing on the automated "validation" of claimed skills through open-ended technical questions before human involvement.

