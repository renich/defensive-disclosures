import json
import os
import sys
import re
import urllib.request
import urllib.error
from datetime import datetime

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


def chat_completion(messages, model, base_url, api_key):
    """Standard lib HTTP request to local AI server."""
    url = f"{base_url.rstrip('/')}/chat/completions"
    payload = {"model": model, "messages": messages, "temperature": 0.2}
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    try:
        req = urllib.request.Request(
            url, data=json.dumps(payload).encode("utf-8"), headers=headers
        )
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        print(f"{RED}HTTP Error: {e.code} - {e.reason}{RESET}")
        try:
            print(f"{RED}Server Response: {e.read().decode()}{RESET}")
        except:
            pass
        return None
    except urllib.error.URLError as e:
        print(f"{RED}API Connection Error: {e.reason}{RESET}")
        return None
    except Exception as e:
        print(f"{RED}Unexpected Error: {e}{RESET}")
        return None


def generate_disclosure():
    api_key = os.getenv("OPENAI_API_KEY", "sk-antigravity")
    base_url = os.getenv("OPENAI_BASE_URL", "http://localhost:11434/v1")
    model = os.getenv("OPENAI_MODEL", "google/gemini-3-flash-preview")
    author = os.getenv("DISCLOSURE_AUTHOR", "René Bon Ćirić")

    if not os.path.exists("instructions.rst"):
        print(f"{RED}Error: instructions.rst missing.{RESET}")
        sys.exit(1)

    ideas = json.loads(load_file("ideas.jsonc"))
    system_prompt = load_file("instructions.rst")
    template_en = load_file("templates/TEMPLATE_EN.rst").replace(
        "[AUTHOR_NAME]", author
    )
    template_es = load_file("templates/TEMPLATE_ES.rst").replace(
        "[AUTHOR_NAME]", author
    )
    year = datetime.now().year

    for idea in ideas:
        slug = re.sub(r"[^a-zA-Z0-9_-]", "", idea.get("slug", "idea"))
        path_en = os.path.abspath(f"ideas/en/{year}-{slug}.rst")
        path_es = os.path.abspath(f"ideas/es/{year}-{slug}.rst")

        if os.path.exists(path_en) and os.path.exists(path_es):
            print(f"{YELLOW}Skipping {slug}: Files exist.{RESET}")
            continue

        print(f"Generating: {GREEN}{idea['title']}{RESET}...")

        for lang, tmpl, path, jur in [
            ("EN", template_en, path_en, "USPTO"),
            ("ES", template_es, path_es, "IMPI"),
        ]:
            if os.path.exists(path):
                continue

            prompt = f"Title: {idea['title']}\nConcept: {idea['raw_concept']}\nJurisdiction: {jur}\n\nTemplate:\n{tmpl}"
            content = chat_completion(
                [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt},
                ],
                model,
                base_url,
                api_key,
            )
            if content:
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"  - {lang} saved.")


if __name__ == "__main__":
    generate_disclosure()
