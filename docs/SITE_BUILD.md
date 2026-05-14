---
audience: contributors
---

# Local Documentation Build (Contributors Only)

> This page is for contributors who want to preview the rendered documentation site locally before opening a pull request. It is not part of the OSARA Standards Family and is not a publication of Open Source United.

## Prerequisites

- Python 3.10 or later
- `pip`

## One-time setup

```bash
pip install mkdocs mkdocs-material python-docx
```

## Build and preview

From the repository root:

```bash
python scripts/sync_specs.py
mkdocs serve
```

Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a browser. The site rebuilds automatically as you edit files under `specs/`, `governance/`, `community/`, or `docs/`.

To run the same strict build that CI runs:

```bash
python scripts/sync_specs.py
mkdocs build --strict
```

## What gets synced

`scripts/sync_specs.py` copies the canonical sources (`specs/`, `governance/`, `community/`, `assets/diagrams/`, and `CHANGELOG.md`) into the `docs/` build tree and rewrites cross-document links so they resolve at every depth. The synced copies inside `docs/` are build artifacts and are excluded from version control — do not commit them.

## Converting `.docx` source drafts

When the authoring team supplies a new draft of a specification as a `.docx` file, convert it to Markdown with:

```bash
python scripts/docx_to_md.py path/to/source.docx path/to/output.md
```

Then merge the converted text into the appropriate `specs/<doc>/current.md`.

## Editor's draft preview

The published site is built from `main` (release) and `prerelease` (editor's draft). Refer to the project README for the published URL. To preview an editor's draft without merging, run the build locally or open the changes on the corresponding pull request.
