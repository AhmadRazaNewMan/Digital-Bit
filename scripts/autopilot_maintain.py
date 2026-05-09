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
    allowed = {"content-note", "module-metrics", "highlights", "combo"}
    if forced in allowed:
        return forced

    run = (os.environ.get("GITHUB_RUN_NUMBER") or "").strip()
    if run.isdigit():
        idx = int(run) % 3
    else:
        idx = datetime.now(timezone.utc).timetuple().tm_yday % 3
    return ["content-note", "module-metrics", "highlights"][idx]


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


def main() -> int:
    mode = _pick_mode()
    changed: list[Path] = []

    if mode in {"content-note", "combo"}:
        changed.extend(_run_daily_post())

    posts = _iter_posts()
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
