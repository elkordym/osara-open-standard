# Specification Layout and Naming

This folder is the single source of truth for the canonical text of the OSARA Standards Family.

## Family Layout

| Folder | Document | Role |
| --- | --- | --- |
| `osara-overview/` | OSARA Overview & Concepts | Informative — start here for newcomers |
| `osara/` | OSARA Specification | Normative — mandatory requirements |
| `osara-threat-model/` | OSARA Threat Model | Informative — adversaries, threats, mitigations |
| `osara-privacy/` | OSARA Privacy Considerations | Informative — data flows, identifiers, privacy properties |
| `ai-bill-of-rights/` | AI Bill of Rights | Policy — rights framework, companion to OSARA |

## Per-Document Layout

Each folder follows the same pattern:

```
<doc-name>/
  current.md            <- editable working draft
  releases/
    v<X>.<Y>-<stage>.md <- immutable snapshot
```

## Version File Naming

`v<major>.<minor>-<stage>.<n>.md`

Examples:

- `v0.4-draft.1.md`
- `v0.4-rc.1.md`
- `v1.0.md`

Rules:

- `current.md` is the editable working draft. It is the version the docs site renders as "Current".
- Files under `releases/` are immutable snapshots — once written, they are not modified. Errata against a published snapshot are recorded in the [Errata Register](../errata.md), not by editing the snapshot file.
- Snapshot file names are stable identifiers. External documents (RFCs, court filings, audit reports, procurement specifications) can cite them by path.

## Cross-Document References

All references between documents in the Family use repository-relative Markdown links so that they resolve both in the source tree and on the published site. For example, OSARA cross-references the AI Bill of Rights as `[AI Bill of Rights §4.7](../ai-bill-of-rights/current.md#article-iv--interoperability-portability-and-open-standards-normative)`.
