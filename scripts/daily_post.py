#!/usr/bin/env python3
"""
Creates one markdown post per day under content/modules/<module>/.
Optional: set GROQ_API_KEY for Groq Cloud (console.groq.com) — not xAI Grok.
Also OPENAI_API_KEY + OPENAI_BASE_URL for OpenAI-compatible APIs.
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


def _load_dotenv() -> None:
    """Load ROOT/.env into os.environ (no extra packages).

    Fills missing vars. For API keys, also replaces empty shell values so
    `export GROQ_API_KEY=` does not block `.env`.
    """
    path = ROOT / ".env"
    if not path.is_file():
        return
    fill_if_empty = frozenset({"GROQ_API_KEY", "OPENAI_API_KEY", "LLM_MODEL", "LLM_MAX_TOKENS"})
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].strip()
        if "=" not in line:
            continue
        key, _, val = line.partition("=")
        key = key.strip()
        val = val.strip().strip("\ufeff").strip("'").strip('"')
        if not key:
            continue
        if key in fill_if_empty:
            cur = (os.environ.get(key) or "").strip()
            if not cur:
                os.environ[key] = val
        elif key not in os.environ:
            os.environ[key] = val

MODULES = [
    "frontend-basics",
    "javascript-typescript",
    "dsa-algorithms",
    "system-design",
    "devops",
    "dbms",
]

# Picked at random each run so repeated DSA days don’t all become “Dijkstra again”.
TOPIC_SPINS: dict[str, list[str]] = {
    "dsa-algorithms": [
        "topological sort (Kahn and DFS variants)",
        "union-find / disjoint-set with path compression",
        "binary indexed tree (Fenwick) vs segment tree — when to use which",
        "sliding window maximum / monotone deque",
        "two pointers on sorted arrays and duplicates",
        "binary search on answer (min feasible / max capacity patterns)",
        "meet-in-the-middle for subset sums (small n)",
        "bit manipulation tricks for subsets and XOR paths",
        "greedy exchange argument — proving correctness",
        "interval scheduling / merging overlapping intervals",
        "heap applications: median stream, k-way merge",
        "trie for prefix search and autocomplete-style queries",
        "rolling hash / Rabin–Karp for substring search",
        "LCS / LIS intuition (DP states, not full code dump)",
        "BFS vs DFS for grids and implicit graphs",
        "shortest path with constraints (0–1 BFS idea)",
        "strongly connected components — conceptual use cases",
        "reservoir sampling for streaming data",
        "counting inversions with merge sort pattern",
        "backtracking with pruning — template and pitfalls",
    ],
    "frontend-basics": [
        "semantic landmark regions and heading outline",
        "form accessibility: labels, errors, focus management",
        "CSS containment and layout thrashing basics",
        "responsive typography with clamp()",
        "critical rendering path — what blocks first paint",
    ],
    "javascript-typescript": [
        "structural typing vs nominal — practical gotchas",
        "narrowing with discriminated unions",
        "async cancellation with AbortController",
        "module resolution ESM vs CJS interop",
        "generics for reusable API wrappers",
    ],
    "system-design": [
        "idempotency keys for payments and retries",
        "rate limiting: token bucket vs leaky bucket",
        "cache stampede and probabilistic early expiration",
        "CQRS — read vs write scaling tradeoffs",
        "backpressure between services",
    ],
    "devops": [
        "immutable artifacts vs mutable servers",
        "health checks: liveness vs readiness",
        "rolling deploys and failure budgets",
        "structured logs vs metrics vs traces — when each",
        "secrets rotation without downtime",
    ],
    "dbms": [
        "B-tree vs LSM — intuition for OLTP vs heavy writes",
        "transaction isolation anomalies (dirty read, phantom)",
        "covering indexes and index-only scans",
        "EXPLAIN basics — sequential scan vs index scan",
        "normalization vs denormalization tradeoffs",
    ],
}


def _random_spin(module: str) -> str:
    opts = TOPIC_SPINS.get(module)
    if not opts:
        return "pick one concrete subtopic appropriate to this module"
    return random.choice(opts)


def _slug(s: str) -> str:
    return "-".join(s.lower().replace("/", "-").split())


def _pick_module() -> str:
    # Stable per UTC day: same module for all reruns same day; advances each calendar day.
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    seed = int(day.replace("-", ""))
    return MODULES[seed % len(MODULES)]


def _chat_complete(url: str, key: str, model: str, module: str, title_hint: str) -> str | None:
    body = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You write concise technical blog notes. Markdown only, no fenced code language mistakes, under 900 words. "
                    "Vary the concrete topic each time; do not default to Dijkstra or generic shortest-path unless the user focus explicitly asks for it."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Module: {module}. Topic hint: {title_hint}. "
                    "Your H1 title must reflect TODAY'S FOCUS below—not a generic famous algorithm unless the focus demands it. "
                    "Write: short title line as H1, then sections What / Why / How / One exercise or command / Further reading (bullets)."
                ),
            },
        ],
        "temperature": 0.82,
        "max_tokens": int(os.environ.get("LLM_MAX_TOKENS", "2000")),
    }
    # Groq sits behind Cloudflare; default Python-urllib User-Agent often gets 403.
    ua = os.environ.get(
        "HTTP_USER_AGENT",
        "Digital-Bit-daily-post/1.0 (+https://github.com/AhmadRazaNewMan/Digital-Bit)",
    )
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
            "User-Agent": ua,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read().decode())
        text = data["choices"][0]["message"]["content"].strip()
        host = "Groq Cloud" if "groq.com" in url else "LLM"
        print(f"OK: {host} returned content (model={model!r}).", file=sys.stderr)
        return text
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode(errors="replace")[:1200]
        except Exception:
            pass
        print(f"LLM HTTPError ({model}): {e}" + (f" | {detail}" if detail else ""), file=sys.stderr)
        return None
    except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
        print(f"LLM error ({model}): {e}", file=sys.stderr)
        return None


def _llm_generate(module: str, title_hint: str) -> str | None:
    gkey = (os.environ.get("GROQ_API_KEY") or "").strip()
    if gkey:
        base = "https://api.groq.com/openai/v1/chat/completions"
        preferred = (os.environ.get("LLM_MODEL") or "").strip()
        fallbacks = [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "openai/gpt-oss-20b",
        ]
        tried: list[str] = []
        if preferred:
            tried.append(preferred)
        for m in fallbacks:
            if m not in tried:
                tried.append(m)
        for model in tried:
            out = _chat_complete(base, gkey, model, module, title_hint)
            if out:
                return out
            print(f"Groq: retrying next model after {model!r} failed…", file=sys.stderr)
        return None

    okey = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if okey:
        base = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        url = base + "/chat/completions"
        model = (os.environ.get("LLM_MODEL") or "gpt-4o-mini").strip()
        return _chat_complete(url, okey, model, module, title_hint)

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
    _load_dotenv()
    CONTENT.mkdir(parents=True, exist_ok=True)
    module = _pick_module()
    (CONTENT / module).mkdir(parents=True, exist_ok=True)

    day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    spin = _random_spin(module)
    title_hint = (
        f"{module.replace('-', ' ').title()} — daily note {day}. "
        f"Today's focus (stick to this): {spin}"
    )
    title = title_hint

    body = _llm_generate(module, title_hint)
    if body:
        first = body.splitlines()[0].strip()
        if first.startswith("# "):
            title = first[2:].strip()
    else:
        body = _stub_body(module, title)
        print(
            "NOTE: Wrote placeholder (stub) note — not LLM text. "
            "Use Groq Cloud API key in secret GROQ_API_KEY (groq.com / console.groq.com — not xAI Grok). "
            "See stderr above for HTTP errors.",
            file=sys.stderr,
        )

    base = f"{day}-{_slug(module)}"
    path = CONTENT / module / f"{base}.md"
    if path.exists():
        path = CONTENT / module / f"{base}-{suffix}.md"

    path.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    print(path.relative_to(ROOT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
