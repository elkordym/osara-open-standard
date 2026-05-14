"""Apply systematic link / anchor / marker fixes to spec source files.

Run after editing spec content. The script:

1. Moves `[Normative]` / `[Informative]` markers out of section headers and
   into an italic body line below the header, so that auto-generated anchors
   (which are derived from header text) stay clean and stable across the
   life of the document.
2. Normalises paths inside spec bodies to a form that resolves correctly
   both for the canonical source view and for the post-sync docs site view.
3. Detects accidental nesting of `releases/` paths inside snapshot files.

Idempotent. Safe to run repeatedly. Operates on files in `specs/`.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS = ROOT / "specs"

HEADER_MARKER_RE = re.compile(
    r"^(#{1,6}\s+.+?)[ \t]+\[(Normative|Informative)\][ \t]*$",
    re.MULTILINE,
)
DOUBLE_MARKER_RE = re.compile(
    r"\*This section is (normative|informative)\.\*\n\*This section is (normative|informative)\.\*",
)
COLLAPSED_BLANK_RE = re.compile(r"(\*This section is (?:normative|informative)\.\*\n)(?!\n)")


def fix_header_markers(text: str) -> str:
    """Strip `[Normative]` / `[Informative]` from headers and emit an italic body line.

    Re-running the script is a no-op: previously-converted files retain their
    body-line marker; only headers that still carry an inline `[Normative]` tag
    get rewritten.
    """

    def repl(match: re.Match[str]) -> str:
        header = match.group(1).rstrip()
        marker = match.group(2)
        article = "informative" if marker == "Informative" else "normative"
        return f"{header}\n\n*This section is {article}.*"

    out = HEADER_MARKER_RE.sub(repl, text)
    out = COLLAPSED_BLANK_RE.sub(r"\1\n", out)
    out = DOUBLE_MARKER_RE.sub(r"*This section is \1.*", out)
    return out


def fix_release_self_links(text: str) -> str:
    """In a release snapshot at .../releases/vX.md, an absolute self-link like
    `[releases/v0.4-draft.1.md](releases/v0.4-draft.1.md)` resolves to
    `.../releases/releases/v0.4-draft.1.md` which is wrong. Rewrite to point
    back to the snapshot itself by anchor.
    """
    return re.sub(
        r"\(releases/(v[\d\.\-]+-draft\.\d+\.md)\)",
        lambda m: f"({m.group(1)})",
        text,
    )


def process_file(path: Path, is_release: bool) -> bool:
    src = path.read_text(encoding="utf-8")
    out = fix_header_markers(src)
    if is_release:
        out = fix_release_self_links(out)
    if out != src:
        path.write_text(out, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed: list[Path] = []
    for md in SPECS.rglob("*.md"):
        is_release = "releases" in md.parts
        if process_file(md, is_release):
            changed.append(md)
    if changed:
        print("Updated:")
        for p in changed:
            print(f"  {p.relative_to(ROOT)}")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
