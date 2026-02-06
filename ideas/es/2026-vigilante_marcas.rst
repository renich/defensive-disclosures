===============================================================================
System and Method for Automated Trademark Surveillance and Similarity Detection
===============================================================================

:Fecha: 2026-02-06
:Autor: René Bon Ćirić
:Estado: Publicación Defensiva

.. note::
   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.

Resumen Técnico
===============
Sistema automatizado de monitoreo de marcas diseñado para proteger la propiedad intelectual mediante la detección de solicitudes de marcas similares en gacetas oficiales (ej. la "Gaceta de la Propiedad Industrial" del IMPI en México). El sistema utiliza un motor de ingesta de alta frecuencia para capturar nuevas solicitudes y un motor de análisis de doble vía. La primera vía realiza análisis de similitud fonética y ortográfica en marcas denominativas utilizando algoritmos de distancia especializados (ej. Levenshtein, Metaphone). La segunda vía utiliza modelos de visión computacional y extracción de características para identificar similitudes visuales en logotipos y marcas figurativas. Al cruzar las nuevas solicitudes con una "Lista de Vigilancia" de marcas protegidas y Clases de Niza de un cliente, el sistema proporciona alertas tempranas, permitiendo que los equipos legales presenten oposiciones dentro de los estrechos plazos estatutarios previstos por la ley.

Campo Técnico
=============
This disclosure relates to the field of Intellectual Property (IP) technology, automated image recognition, and legal monitoring systems.

Antecedentes y Problema Técnico
===============================
Trademark protection requires proactive enforcement. When a third party attempts to register a brand that is "confusingly similar" to an existing one, the owner must file an opposition. However, thousands of trademarks are filed every month. Manual review of the official Gaceta is slow and often misses similar-sounding names or visually similar logos. If the opposition window is missed, the owner must resort to more expensive and uncertain cancellation proceedings.

Descripción Detallada
=====================


Ejemplos de Realización
=======================
In one embodiment, the system includes a "Global Risk Map" that monitors trademark filings across multiple jurisdictions (WIPO, USPTO, EUIPO), providing a unified dashboard for multinational brand protection.

Reivindicación de Novedad
=========================
The system claims novelty in the combination of Spanish-optimized phonetic similarity algorithms with deep-learning-based figurative mark analysis applied specifically to the automation of official trademark gazette monitoring for the purpose of legal opposition.

