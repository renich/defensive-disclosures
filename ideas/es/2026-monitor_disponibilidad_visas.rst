===============================================
System and Method for Automated Dynamic Monitoring of Appointment Availability Portals
===============================================

:Fecha: 2026-02-06
:Autor: René Bon Ćirić
:Estado: Publicación Defensiva

.. note::
   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.

Resumen Técnico
===============
Sistema de monitoreo automatizado diseñado para la identificación y alerta de disponibilidad en tiempo real en portales de programación de citas saturados (ej. centros "CAS" para Visas de EE. UU. u oficinas del SAT). El sistema utiliza un motor de sondeo de alta frecuencia que interactúa con la API de programación del portal de destino o la interfaz de usuario del frontend mediante la automatización de navegadores sin cabezal (headless). Un detector de cambios de estado identifica la aparición de nuevos "Espacios Abiertos" comparando la disponibilidad actual con el último estado registrado. El sistema cuenta con un "Despachador Crítico" de baja latencia que entrega alertas a los usuarios a través de mensajería instantánea (WhatsApp/Telegram), proporcionando la fecha, hora y ubicación específicas de la cita disponible. Al automatizar la "Caza" de citas en sistemas caracterizados por una demanda extrema y una oferta limitada, el sistema permite a los usuarios asegurar servicios gubernamentales o profesionales esenciales sin la necesidad de una actualización manual constante.

Campo Técnico
=============
This disclosure relates to the field of Automated Web Monitoring, API interaction, and real-time notification systems for resource scheduling.

Antecedentes y Problema Técnico
===============================
Many critical services (Visa appointments, Tax office visits, Passport renewals) suffer from "Appointment Scarcity." New slots are released randomly or upon cancellations and are often taken within seconds by automated bots or diligent manual users. For the average person, obtaining an appointment is a frustrating experience involving constant manual checks of a slow website. There is a need for a "Proactive Watcher" that monitors the portal on behalf of the user and alerts them the millisecond a slot opens.

Descripción Detallada
=====================


Ejemplos de Realización
=======================
In one embodiment, the system includes an "Automated Booking Assistant" that, with the user's explicit consent, can automatically attempt to "Reserve" the identified slot for a short period (if the portal allows) to give the user time to finalize the booking.

Reivindicación de Novedad
=========================
The system claims novelty in the combination of persistent session management and high-frequency state-change detection applied specifically to the "Hunting" of ephemeral availability in government and consular scheduling portals.

