"""Sync canonical source trees into the docs build folder.

Source layout (canonical):

- specs/                (every subfolder is an independent specification)
- governance/           (governance / policy documents)
- community/            (CoC, Contributing)
- assets/diagrams/      (canonical diagrams referenced from specs)
- assets/branding/      (canonical OSARA logos, icons, and brand assets)
- CHANGELOG.md          (repo-root changelog)

Sync targets (gitignored build artifacts under docs/):

- docs/specs/
- docs/governance/
- docs/community/
- docs/assets/diagrams/
- docs/assets/branding/
- docs/CHANGELOG.md

After copying, this script applies path rewrites to synced files so that
relative links inside specs and the changelog resolve correctly under the
post-sync docs/ tree. The rewrite is content-only — it never modifies the
canonical source.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DIR_PAIRS = [
    (ROOT / "specs", ROOT / "docs" / "specs"),
    (ROOT / "governance", ROOT / "docs" / "governance"),
    (ROOT / "community", ROOT / "docs" / "community"),
    (ROOT / "assets" / "diagrams", ROOT / "docs" / "assets" / "diagrams"),
    (ROOT / "assets" / "branding", ROOT / "docs" / "assets" / "branding"),
]
FILE_PAIRS = [
    (ROOT / "CHANGELOG.md", ROOT / "docs" / "CHANGELOG.md"),
]


def sync_tree(src: Path, dst: Path) -> None:
    if not src.exists():
        print(f"SKIP: {src} does not exist")
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"synced {src.relative_to(ROOT)}/ -> {dst.relative_to(ROOT)}/")


def sync_file(src: Path, dst: Path) -> None:
    if not src.exists():
        print(f"SKIP: {src} does not exist")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    print(f"synced {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")


CURRENT_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(\.\./\.\./docs/"), "](../../"),
]

RELEASE_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(\.\./\.\./docs/"), "](../../../"),
    (re.compile(r"\]\(\.\./\.\./assets/"), "](../../../assets/"),
    (re.compile(r"\]\(\.\./\.\./governance/"), "](../../../governance/"),
    (re.compile(r"\]\(\.\./\.\./community/"), "](../../../community/"),
    (re.compile(r"\]\(\.\./\.\./CHANGELOG\.md"), "](../../../CHANGELOG.md"),
    (re.compile(r"\]\(\.\./([a-z][a-z0-9\-]+)/"), r"](../../\1/"),
    (re.compile(r"\]\(releases/(v[\d\.\-]+-draft\.\d+\.md)\)"), "](#)"),
]

SPECS_README_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(\.\./docs/"), "](../"),
]

CHANGELOG_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(docs/"), "]("),
]

COMMUNITY_REWRITES: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\]\(\.\./docs/"), "](../"),
]


def apply_rewrites(path: Path, rewrites: list[tuple[re.Pattern[str], str]]) -> None:
    text = path.read_text(encoding="utf-8")
    new = text
    for pattern, replacement in rewrites:
        new = pattern.sub(replacement, new)
    if new != text:
        path.write_text(new, encoding="utf-8")


def rewrite_synced_files() -> None:
    docs_specs = ROOT / "docs" / "specs"
    if docs_specs.exists():
        for md in docs_specs.rglob("*.md"):
            rel = md.relative_to(docs_specs)
            parts = rel.parts
            if len(parts) >= 3 and parts[1] == "releases":
                apply_rewrites(md, RELEASE_REWRITES)
            elif rel == Path("README.md"):
                apply_rewrites(md, SPECS_README_REWRITES)
            else:
                apply_rewrites(md, CURRENT_REWRITES)

    docs_community = ROOT / "docs" / "community"
    if docs_community.exists():
        for md in docs_community.rglob("*.md"):
            apply_rewrites(md, COMMUNITY_REWRITES)

    changelog = ROOT / "docs" / "CHANGELOG.md"
    if changelog.exists():
        apply_rewrites(changelog, CHANGELOG_REWRITES)


def main() -> None:
    for src, dst in DIR_PAIRS:
        sync_tree(src, dst)
    for src, dst in FILE_PAIRS:
        sync_file(src, dst)
    rewrite_synced_files()
    print("post-sync link rewrites applied")


if __name__ == "__main__":
    main()
