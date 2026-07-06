#!/usr/bin/env python3
"""Refresh this standalone repo's skill copy from the source collection.

Runs in CI (see .github/workflows/sync-skill.yml). Clones the public source
collection, copies the `study` skill into `skill/`, and rebuilds `study.skill`.
The landing page (index.html, demo/, README) is owned by THIS repo and is left
untouched - only the mirrored skill is refreshed.

No credentials needed: the source collection is public (clone is anonymous) and
the workflow commits back with the default GITHUB_TOKEN.
"""
from __future__ import annotations

import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

SOURCE_REPO = "https://github.com/flownrt/skills.git"  # the collection (source of truth)
SKILL_PATH = "general-SKILLS/study"                    # the skill within the collection
REPO = Path(__file__).resolve().parents[1]             # standalone repo root (tools/sync.py -> root)


def is_clean(rel: Path) -> bool:
    if any(p.startswith(".") for p in rel.parts):
        return False
    if "__pycache__" in rel.parts or rel.suffix == ".pyc":
        return False
    return True


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["git", "clone", "--depth", "1", SOURCE_REPO, tmp], check=True)
        src = Path(tmp) / SKILL_PATH
        if not (src / "SKILL.md").is_file():
            raise SystemExit(f"skill not found at {SKILL_PATH} in {SOURCE_REPO}")

        # refresh skill/
        dst = REPO / "skill"
        if dst.exists():
            shutil.rmtree(dst)
        n = 0
        for f in sorted(src.rglob("*")):
            if f.is_dir():
                continue
            rel = f.relative_to(src)
            if not is_clean(rel):
                continue
            (dst / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dst / rel)
            n += 1

        # rebuild study.skill (top-level dir "study/")
        with zipfile.ZipFile(REPO / "study.skill", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(src.rglob("*")):
                if f.is_dir():
                    continue
                rel = f.relative_to(src)
                if not is_clean(rel):
                    continue
                z.write(f, (Path("study") / rel).as_posix())

    print(f"refreshed skill/ ({n} files) and study.skill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
