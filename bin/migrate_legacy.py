import os
import re


def migrate():
    ideas_dir = "ideas"
    en_dir = os.path.join(ideas_dir, "en")
    es_dir = os.path.join(ideas_dir, "es")

    os.makedirs(en_dir, exist_ok=True)
    os.makedirs(es_dir, exist_ok=True)

    files = [
        f for f in os.listdir(ideas_dir) if f.endswith(".rst") and f != "index.rst"
    ]

    for filename in files:
        slug = filename.replace(".rst", "")
        with open(os.path.join(ideas_dir, filename), "r", encoding="utf-8") as f:
            content = f.read()

        # Extract Title
        title_match = re.search(r"^=+\n(.+)\n=+", content)
        title = title_match.group(1) if title_match else "Untitled"

        # Split sections
        sections = re.split(r"\n([A-Za-z &áéíóúÁÉÍÓÚ]+)\n[=-]+\n", content)

        data = {}
        for i in range(1, len(sections), 2):
            header = sections[i].strip()
            body = sections[i + 1].strip()
            data[header] = body

        # Mapping for Spanish Headers
        es_headers = {
            "Abstract": "Resumen Técnico",
            "Technical Field": "Campo Técnico",
            "Background & Problem Statement": "Antecedentes y Problema Técnico",
            "Detailed Description": "Descripción Detallada",
            "Specific Embodiments": "Ejemplos de Realización",
            "Claims of Novelty": "Reivindicación de Novedad",
        }

        # Create EN version
        en_content = f"===============================================\n{title}\n===============================================\n\n"
        en_content += ":Date: 2026-02-06\n:Author: René Bon Ćirić\n:Status: Defensive Publication\n\n"
        en_content += ".. note::\n   This document constitutes a Defensive Publication. It discloses technical mechanisms to prevent patenting of the described methods by establishing prior art.\n\n"

        for h, b in data.items():
            if h not in ["Resumen Técnico"] and h in [
                "Abstract",
                "Technical Field",
                "Background & Problem Statement",
                "Detailed Description",
                "Specific Embodiments",
                "Claims of Novelty",
            ]:
                en_content += f"{h}\n{'=' * len(h)}\n{b}\n\n"

        # Create ES version
        es_content = f"===============================================\n{title}\n===============================================\n\n"
        es_content += ":Fecha: 2026-02-06\n:Autor: René Bon Ćirić\n:Estado: Publicación Defensiva\n\n"
        es_content += ".. note::\n   Este documento constituye una Publicación Defensiva. Establece el estado de la técnica (Prior Art) para impedir el patentamiento de los métodos descritos.\n\n"

        es_abstract = data.get(
            "Resumen Técnico", data.get("Abstract", "Resumen no disponible.")
        )
        es_content += f"Resumen Técnico\n===============\n{es_abstract}\n\n"

        for h, b in data.items():
            if h in es_headers and h != "Abstract":
                es_h = es_headers[h]
                es_content += f"{es_h}\n{'=' * len(es_h)}\n{b}\n\n"

        # Write files
        with open(os.path.join(en_dir, f"2026-{slug}.rst"), "w", encoding="utf-8") as f:
            f.write(en_content)
        with open(os.path.join(es_dir, f"2026-{slug}.rst"), "w", encoding="utf-8") as f:
            f.write(es_content)

        # Remove old file
        os.remove(os.path.join(ideas_dir, filename))
        print(f"Migrated {filename}")


if __name__ == "__main__":
    migrate()
