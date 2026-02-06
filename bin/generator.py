import json
import os
import sys
import re
from datetime import datetime
from openai import OpenAI

# ANSI Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"{RED}Error loading {path}: {e}{RESET}")
        sys.exit(1)


def sanitize_slug(slug):
    # CWE-22 Fix: Remove directory separators and non-alphanumeric chars (except - and _)
    return re.sub(r"[^a-zA-Z0-9_-]", "", slug)


def generate_disclosure():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print(f"{RED}Error: OPENAI_API_KEY environment variable not set.{RESET}")
        sys.exit(1)

    model = os.getenv("OPENAI_MODEL", "gpt-4-turbo")
    author = os.getenv("DISCLOSURE_AUTHOR", "EVALinux Contributor")

    client = OpenAI(api_key=api_key)

    if not os.path.exists("ideas.json"):
        print(f"{RED}Error: ideas.json not found.{RESET}")
        sys.exit(1)

    try:
        ideas = json.loads(load_file("ideas.json"))
    except json.JSONDecodeError:
        print(f"{RED}Error: ideas.json contains invalid JSON.{RESET}")
        sys.exit(1)

    # Cache templates and system prompt
    system_prompt = load_file("instructions.rst")
    template_en = load_file("templates/TEMPLATE_EN.rst").replace(
        "[AUTHOR_NAME]", author
    )
    template_es = load_file("templates/TEMPLATE_ES.rst").replace(
        "[AUTHOR_NAME]", author
    )

    year = datetime.now().year

    for idea in ideas:
        raw_slug = idea.get("slug", "unnamed-idea")
        slug = sanitize_slug(raw_slug)
        title = idea.get("title", "Untitled Idea")
        concept = idea.get("raw_concept", "")

        path_en = os.path.abspath(f"ideas/en/{year}-{slug}.rst")
        path_es = os.path.abspath(f"ideas/es/{year}-{slug}.rst")

        if os.path.exists(path_en) and os.path.exists(path_es):
            print(f"{YELLOW}Skipping {slug}: Files already exist.{RESET}")
            continue

        print(f"Generating disclosure for: {GREEN}{title}{RESET} using {model}...")

        configs = [
            ("EN", "USPTO (USA)", template_en, path_en),
            ("ES", "IMPI (Mexico)", template_es, path_es),
        ]

        for lang, jurisdiction, template, output_path in configs:
            prompt = f"Title: {title}\nConcept: {concept}\nJurisdiction: {jurisdiction}\n\nApply template:\n{template}"

            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                )
                content = response.choices[0].message.content
            except Exception as e:
                print(f"{RED}OpenAI API Error ({lang}): {e}{RESET}")
                continue

            # Harden safety check with regex (CWE-Compliance)
            if re.search(r"\.\.\s+warning::", content, re.IGNORECASE):
                print(
                    f"{RED}[CRITICAL ALERT] Legal Weakness Detected in {lang} output for {slug}!{RESET}"
                )

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"  - {lang} version saved.")


if __name__ == "__main__":
    generate_disclosure()
