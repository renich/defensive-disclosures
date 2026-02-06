========================================================================================
Sistema Criptográfico Distribuido para la Publicación Defensiva Inmutable
========================================================================================

:Fecha: 2026-02-06
:Autor: René Bon Ćirić
:Estado: Publicación Defensiva

.. note::
   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.

Resumen Técnico
===============
Un sistema descentralizado para establecer el estado de la técnica mediante la integración de sistemas de control de versiones distribuidos (DVCS), flujos de integración continua (CI) automatizados y repositorios persistentes de identificadores de objetos digitales (DOI). La arquitectura del sistema comprende un repositorio basado en Git que aloja divulgaciones técnicas en formato estructurado (ReStructuredText), un orquestador de CI/CD activado por eventos de commit criptográficos y un puente de API seguro hacia servicios de archivo de terceros (ej. Zenodo). Al automatizar la creación de DOIs tras versiones verificadas, el sistema proporciona un sello de tiempo inalterable y sincronizado globalmente para innovaciones técnicas, asegurando la validez legal bajo las leyes internacionales de patentes.

Campo Técnico
=============
Esta divulgación se relaciona con el campo del sellado de tiempo criptográfico, flujos de documentación automatizados y sistemas descentralizados para el establecimiento legal del estado de la técnica.

Antecedentes y Problema Técnico
===============================
El establecimiento del estado de la técnica para innovaciones técnicas a menudo requiere la publicación en revistas especializadas o bases de datos de patentes, lo que implica altos costos, carga operativa manual y latencia significativa. Las publicaciones digitales tradicionales son mutables y carecen de una prueba criptográfica integrada de existencia en un momento específico. Existe una necesidad técnica de un sistema de publicación automatizado, de baja latencia e inmutable que aproveche la infraestructura de desarrollo de software existente para asegurar la innovación.

Descripción Detallada
=====================

Arquitectura del Sistema
------------------------
El sistema consta de tres capas técnicas principales:
1. **Capa de Integridad de Origen (Git)**: Utiliza hashing SHA-256 para asegurar que cualquier modificación a una divulgación resulte en un nuevo identificador único.
2. **Motor de Orquestación (GitHub Actions)**: Una capa de automatización basada en disparadores que monitorea el espacio de nombres "ideas/". Filtra documentos estructurados nuevos o modificados e inicia el flujo de liberación.
3. **Capa de Persistencia de Archivo (Zenodo)**: Un repositorio de terceros que acepta instantáneas del repositorio y asigna un DOI, creando un vínculo inmutable entre el estado criptográfico del repositorio Git y un registro legal reconocido globalmente.

Flujo del Proceso
-----------------
1. El usuario realiza un commit de una nueva divulgación .rst a la rama principal.
2. GitHub Action detecta el evento de push en el directorio ideas/.
3. La Action genera una etiqueta de versión semántica (vYYYY.MM.DD-runID).
4. La Action crea una Release en GitHub, que emite una carga útil de webhook.
5. Zenodo recibe la carga útil, clona la etiqueta específica y genera un DOI permanente.

Ejemplos de Realización
=======================
En una realización, el sistema utiliza un flujo de ReStructuredText (RST) para generar artefactos PDF vía Pandoc antes del archivo, asegurando que la divulgación sea legible en formatos legales y de ingeniería estándar.

Reivindicación de Novedad
=========================
El sistema implementa un puente automatizado entre identificadores criptográficos de código (hashes de Git) e identificadores persistentes legales (DOIs), convirtiendo efectivamente un flujo de desarrollo de software en un motor de invalidación de patentes legalmente reconocido sin intervención manual.
