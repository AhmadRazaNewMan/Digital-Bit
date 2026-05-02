#!/usr/bin/env python3
"""
Creates one markdown post per day under content/modules/<module>/.
Optional: set GROQ_API_KEY (or OPENAI_API_KEY + OPENAI_BASE_URL) for LLM body.
"""
from __future__ import annotations

import json
import os
import random
import string
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "modules"

MODULES = [
    "frontend-basics",
    "javascript-typescript",
    "dsa-algorithms",
    "system-design",
    "devops",
    "dbms",
]


def _slug(s: str) -> str:
    return "-".join(s.lower().replace("/", "-").split())


def _pick_module() -> str:
    # Stable per UTC day: same module for all reruns same day; advances each calendar day.
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    seed = int(day.replace("-", ""))
    return MODULES[seed % len(MODULES)]


def _llm_generate(module: str, title_hint: str) -> str | None:
    if os.environ.get("GROQ_API_KEY"):
        key = os.environ["GROQ_API_KEY"]
        base = "https://api.groq.com/openai/v1"
        model = os.environ.get("LLM_MODEL", "llama-3.3-70b-versatile")
    elif os.environ.get("OPENAI_API_KEY"):
        key = os.environ["OPENAI_API_KEY"]
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        model = os.environ.get("LLM_MODEL", "gpt-4o-mini")
    else:
        return None
    url = base.rstrip("/") + "/chat/completions"
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You write concise technical blog notes. Markdown only, no fenced code language mistakes, under 900 words.",
            },
            {
                "role": "user",
                "content": f"Module: {module}. Topic hint: {title_hint}. "
                "Write: short title line as H1, then sections What / Why / How / One exercise or command / Further reading (bullets).",
            },
        ],
        "temperature": 0.65,
        "max_tokens": 2000,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
        return data["choices"][0]["message"]["content"].strip()
    except (urllib.error.HTTPError, urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
        print(f"LLM skipped: {e}", file=sys.stderr)
        return None


def _stub_body(module: str, title: str) -> str:
    return f"""# {title}

**Module:** `{module}`  
**Generated:** {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} (automated daily note)

## What

Add your angle here after the first LLM-backed run, or edit in GitHub.

## Why it matters

One sentence on job interviews or real systems.

## How (sketch)

1. …
2. …

## Mini exercise

Try one small task and timebox 15 minutes.

## Further reading

- Official docs for this stack
- One reputable article or RFC
"""


def main() -> int:
    CONTENT.mkdir(parents=True, exist_ok=True)
    module = _pick_module()
    (CONTENT / module).mkdir(parents=True, exist_ok=True)

    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    title_hint = f"{module.replace('-', ' ').title()} — daily topic {day}"
    title = title_hint

    body = _llm_generate(module, title_hint)
    if body:
        first = body.splitlines()[0].strip()
        if first.startswith("# "):
            title = first[2:].strip()
    else:
        body = _stub_body(module, title)

    base = f"{day}-{_slug(module)}"
    path = CONTENT / module / f"{base}.md"
    if path.exists():
        path = CONTENT / module / f"{base}-{suffix}.md"

    path.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
