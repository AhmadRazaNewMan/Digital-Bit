#!/usr/bin/env python3
"""
Autopilot maintenance runner for Digital-Bit.

Purpose:
- Run without manual interaction.
- Produce legitimate, varied repository updates.
- Commit only when there are real file changes.

Task rotation:
1) content-note: generate one new module note via daily_post.py
2) module-metrics: refresh aggregate metrics JSON from existing markdown corpus
3) highlights: refresh markdown digest of newest posts per module
"""
from __future__ import annotations

import json
import os
import random
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "modules"
AUTOMATION = ROOT / "content" / "automation"
METRICS_PATH = AUTOMATION / "module-metrics.json"
HIGHLIGHTS_PATH = AUTOMATION / "recent-highlights.md"
MODULE_CATALOG_PATH = ROOT / "web" / "src" / "lib" / "moduleCatalog.ts"

INTERVIEW_BLOCK_HEADER = "## Senior interview checkpoint"
INTERVIEW_PROMPTS: dict[str, list[str]] = {
    "dsa-algorithms": [
        "Design an approach for top-K frequent items in a streaming system with memory limits.",
        "Compare monotonic queue vs heap for sliding-window max under high-throughput constraints.",
    ],
    "frontend-basics": [
        "Audit a page for accessibility regressions after a redesign; list highest-risk fixes first.",
        "Explain hydration mismatch root causes and debugging strategy in SSR apps.",
    ],
    "javascript-typescript": [
        "Refactor an API client to discriminated unions; show how this prevents runtime bugs.",
        "Design cancellation-safe async flow with AbortController for chained requests.",
    ],
    "backend": [
        "Design idempotent retry handling for a payment callback endpoint.",
        "Explain how to debug p95 latency spikes in a Node API under burst traffic.",
    ],
    "system-design": [
        "Design a rate limiter that supports both global and per-user quotas.",
        "Explain cache invalidation strategy for hot keys with high write rates.",
    ],
    "devops": [
        "Draft a rollback plan for failed blue-green deployment with partial data migrations.",
        "Design CI guardrails to prevent secret leaks and oversized images.",
    ],
    "dbms": [
        "Choose indexes for a high-cardinality filter + sort query and justify tradeoffs.",
        "Explain how isolation level affects deadlocks in write-heavy workloads.",
    ],
}

TAGLINE_ALTS: dict[str, list[str]] = {
    "dsa-algorithms": [
        "Complexity, patterns, interview readiness",
        "Problem-solving drills and performance tradeoffs",
    ],
    "frontend-basics": [
        "UI structure, accessibility, and rendering speed",
        "Readable interfaces with resilient UX",
    ],
    "javascript-typescript": [
        "Type-safe apps, async control, cleaner abstractions",
        "Runtime safety with practical TypeScript patterns",
    ],
    "backend": [
        "APIs, auth, reliability, and service boundaries",
        "Production-grade endpoints and failure handling",
    ],
    "system-design": [
        "Scale, tradeoffs, and architecture judgement",
        "Design choices for growth, latency, and reliability",
    ],
    "devops": [
        "Build, release, observe, and recover confidently",
        "CI/CD discipline and operational excellence",
    ],
    "dbms": [
        "Queries, indexes, transactions, data correctness",
        "Storage design and performance tuning fundamentals",
    ],
}


@dataclass(frozen=True)
class Post:
    module: str
    path: Path
    date_prefix: str
    stem: str


def _iter_posts() -> list[Post]:
    posts: list[Post] = []
    if not CONTENT.is_dir():
        return posts
    for mod_dir in sorted(CONTENT.iterdir()):
        if not mod_dir.is_dir():
            continue
        module = mod_dir.name
        for md in sorted(mod_dir.glob("*.md")):
            stem = md.stem
            parts = stem.split("-", 3)
            date_prefix = "-".join(parts[:3]) if len(parts) >= 3 else ""
            posts.append(Post(module=module, path=md, date_prefix=date_prefix, stem=stem))
    return posts


def _pick_mode() -> str:
    forced = (os.environ.get("AUTOPILOT_MODE") or "").strip().lower()
    allowed = {"content-note", "module-metrics", "highlights", "legacy-upgrade", "ui-polish", "combo"}
    if forced in allowed:
        return forced

    allow_new_content = (os.environ.get("AUTOPILOT_ALLOW_NEW_CONTENT") or "1").strip().lower()
    allow_content_note = allow_new_content not in {"0", "false", "no", "off"}

    # Weighted, so most commits improve existing content/code (not always new files).
    run = (os.environ.get("GITHUB_RUN_NUMBER") or "").strip()
    modes = ["legacy-upgrade", "ui-polish", "module-metrics", "highlights"]
    if allow_content_note:
        modes.append("content-note")
    if run.isdigit():
        idx = int(run) % len(modes)
    else:
        idx = datetime.now(timezone.utc).timetuple().tm_yday % len(modes)
    return modes[idx]


def _run_daily_post() -> list[Path]:
    cmd = [sys.executable, str(ROOT / "scripts" / "daily_post.py")]
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if proc.stderr:
        print(proc.stderr.rstrip(), file=sys.stderr)
    if proc.returncode != 0:
        raise RuntimeError(f"daily_post.py failed (exit={proc.returncode})")

    rel = (proc.stdout or "").strip().splitlines()
    if not rel:
        return []
    out = ROOT / rel[0].strip()
    return [out] if out.exists() else []


def _refresh_metrics(posts: list[Post]) -> list[Path]:
    AUTOMATION.mkdir(parents=True, exist_ok=True)

    by_module: dict[str, list[Post]] = {}
    for p in posts:
        by_module.setdefault(p.module, []).append(p)

    modules: dict[str, object] = {}
    for module in sorted(by_module):
        rows = sorted(by_module[module], key=lambda p: p.path.name)
        modules[module] = {
            "count": len(rows),
            "latestFile": rows[-1].path.relative_to(ROOT).as_posix() if rows else "",
            "latestDatePrefix": rows[-1].date_prefix if rows else "",
        }

    payload = {
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "totalPosts": len(posts),
        "moduleCount": len(modules),
        "modules": modules,
    }
    text = json.dumps(payload, indent=2) + "\n"
    old = METRICS_PATH.read_text(encoding="utf-8") if METRICS_PATH.exists() else ""
    if old == text:
        return []
    METRICS_PATH.write_text(text, encoding="utf-8")
    return [METRICS_PATH]


def _refresh_highlights(posts: list[Post]) -> list[Path]:
    AUTOMATION.mkdir(parents=True, exist_ok=True)
    by_module: dict[str, list[Post]] = {}
    for p in posts:
        by_module.setdefault(p.module, []).append(p)

    lines: list[str] = [
        "# Recent Highlights",
        "",
        "Auto-generated snapshot of the newest module notes.",
        "",
        f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}_",
        "",
    ]
    for module in sorted(by_module):
        lines.append(f"## {module}")
        rows = sorted(by_module[module], key=lambda p: p.path.name, reverse=True)[:5]
        for p in rows:
            rel = p.path.relative_to(ROOT).as_posix()
            label = p.stem.replace("-", " ")
            lines.append(f"- [{label}]({rel})")
        lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    old = HIGHLIGHTS_PATH.read_text(encoding="utf-8") if HIGHLIGHTS_PATH.exists() else ""
    if old == text:
        return []
    HIGHLIGHTS_PATH.write_text(text, encoding="utf-8")
    return [HIGHLIGHTS_PATH]


def _upgrade_existing_module(posts: list[Post]) -> list[Path]:
    if not posts:
        return []
    ranked = sorted(posts, key=lambda p: p.path.name)
    target = random.choice(ranked[: max(1, len(ranked) // 2)])
    src = target.path.read_text(encoding="utf-8")
    if INTERVIEW_BLOCK_HEADER in src:
        # Find first file without the section to avoid no-op commits.
        for p in ranked:
            text = p.path.read_text(encoding="utf-8")
            if INTERVIEW_BLOCK_HEADER not in text:
                target = p
                src = text
                break
        else:
            return []

    bank = INTERVIEW_PROMPTS.get(target.module) or INTERVIEW_PROMPTS["backend"]
    prompt = random.choice(bank)
    patch = (
        f"\n{INTERVIEW_BLOCK_HEADER}\n\n"
        f"**Prompt:** {prompt}\n\n"
        "**What a senior answer should include**\n\n"
        "- Constraints first (traffic, latency, reliability, ownership boundaries).\n"
        "- Tradeoffs with at least two viable alternatives.\n"
        "- Failure modes, observability signals, and rollback plan.\n"
        "- A measurable success criterion after rollout.\n"
    )
    out = src.rstrip() + "\n" + patch
    target.path.write_text(out, encoding="utf-8")
    return [target.path]


def _ui_polish_module_catalog() -> list[Path]:
    if not MODULE_CATALOG_PATH.exists():
        return []
    src = MODULE_CATALOG_PATH.read_text(encoding="utf-8")
    ids = sorted(TAGLINE_ALTS.keys())
    if not ids:
        return []
    ridx = datetime.now(timezone.utc).timetuple().tm_yday % len(ids)
    module_id = ids[ridx]
    tagline = random.choice(TAGLINE_ALTS[module_id])
    hue = 20 + ((datetime.now(timezone.utc).toordinal() * 37 + ridx * 11) % 320)

    block_re = re.compile(rf'(\{{\s*id:\s*"{re.escape(module_id)}",.*?\n\s*\}})', re.S)
    match = block_re.search(src)
    if not match:
        return []
    block = match.group(1)
    new_block = re.sub(r'tagline:\s*"[^"]*",', f'tagline: "{tagline}",', block, count=1)
    new_block = re.sub(r"hue:\s*\d+,", f"hue: {hue},", new_block, count=1)
    if new_block == block:
        return []
    out = src[: match.start(1)] + new_block + src[match.end(1) :]
    MODULE_CATALOG_PATH.write_text(out, encoding="utf-8")
    return [MODULE_CATALOG_PATH]


def main() -> int:
    mode = _pick_mode()
    changed: list[Path] = []

    if mode in {"content-note", "combo"}:
        changed.extend(_run_daily_post())

    posts = _iter_posts()
    if mode in {"legacy-upgrade", "combo"}:
        changed.extend(_upgrade_existing_module(posts))
    if mode in {"ui-polish", "combo"}:
        changed.extend(_ui_polish_module_catalog())
    if mode in {"module-metrics", "combo"}:
        changed.extend(_refresh_metrics(posts))
    if mode in {"highlights", "combo"}:
        changed.extend(_refresh_highlights(posts))

    rel = sorted({p.relative_to(ROOT).as_posix() for p in changed if p.exists()})
    out = {
        "mode": mode,
        "changedFiles": rel,
        "changedCount": len(rel),
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
