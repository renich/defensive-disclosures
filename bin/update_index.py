import os
import glob


def generate_index_content(title, files):
    content = f"{'=' * len(title)}\n{title}\n{'=' * len(title)}\n\n"
    content += ".. toctree::\n   :maxdepth: 1\n\n"
    for f in sorted(files):
        # Fix fragile replacement: use splitext
        rel_path = os.path.splitext(os.path.basename(f))[0]
        content += f"   {rel_path}\n"
    return content


def rebuild_indices():
    en_files = glob.glob("ideas/en/*.rst")
    es_files = glob.glob("ideas/es/*.rst")

    # Filter out index.rst to avoid recursion
    en_files = [f for f in en_files if os.path.basename(f) != "index.rst"]
    es_files = [f for f in es_files if os.path.basename(f) != "index.rst"]

    # Enforce UTF-8 for international character support
    with open("ideas/en/index.rst", "w", encoding="utf-8") as f:
        f.write(generate_index_content("English Disclosures", en_files))

    with open("ideas/es/index.rst", "w", encoding="utf-8") as f:
        f.write(generate_index_content("Divulgaciones en Español", es_files))

    root_content = """============================
Defensive Disclosure Archive
============================

.. toctree::
   :maxdepth: 2
   :caption: Jurisdictions:

   ideas/en/index
   ideas/es/index
"""
    with open("index.rst", "w", encoding="utf-8") as f:
        f.write(root_content)

    print("Indices rebuilt successfully (UTF-8).")


if __name__ == "__main__":
    rebuild_indices()
