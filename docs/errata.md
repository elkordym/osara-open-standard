# OSARA Errata Register

> Public register of substantive errata against published OSARA Standards Family documents, modelled on the W3C errata process and the IETF errata system.

---

## Purpose

The errata register identifies clarifications, corrections, and editorial fixes applied to published versions of OSARA Standards Family documents. Errata do **not** introduce new normative requirements; substantive normative changes are handled through the public RFC process and result in a new versioned release.

Each erratum has a unique identifier, an applicable document and version, a classification, the reported text, the corrected interpretation, and a disposition.

## Classifications

| Class | Meaning |
| --- | --- |
| **Editorial** | Typographical, formatting, or clarity fix that does not change meaning. |
| **Substantive (clarification)** | Resolves an ambiguity; the corrected interpretation is consistent with the most reasonable reading of the original text. |
| **Substantive (correction)** | Corrects a genuine error; the corrected interpretation differs from a plausible reading of the original. Implementations relying on the original reading may need to update. |
| **Future amendment** | Cannot be corrected in the current version; recorded here as input to the next revision. |

## Disposition States

| State | Meaning |
| --- | --- |
| **Reported** | Filed publicly; not yet reviewed by editors. |
| **Acknowledged** | Editors confirm the issue is real and have classified it. |
| **Resolved** | A correction has been published. The published current.md and the relevant errata note both record the correction. |
| **Rejected** | Editors have determined the report does not reflect an error or ambiguity. Rationale is recorded. |
| **Deferred** | Recorded for inclusion in the next revision. |

## Filing an Erratum

Errata are filed through the repository:

1. Open an issue using the **"Spec change"** template at `.github/ISSUE_TEMPLATE/spec-change.md` (or its GitLab equivalent post-migration), with the label `errata`.
2. State the document, the version, the section, the original text, the issue, and your proposed correction.
3. Editors triage within the regular OSC editorial cycle.

For urgent errata affecting deployed implementations, mark the issue `errata-priority`.

## Register

### Active Errata

| ID | Document | Version | Section | Class | Disposition | Summary |
| --- | --- | --- | --- | --- | --- | --- |
| ERR-0001 | AI Bill of Rights | v1.1-draft.1 | Annex A header | Editorial | Acknowledged | Header text says "v0.3" cross-reference; should read "v0.4". Annex A table entries already use v0.4 section numbers post-restructuring. |
| ERR-0002 | OSARA | v0.4-draft.1 | §1 / §16 | Editorial | Acknowledged | The §8 of the AI Bill of Rights is cited as "§4.7" in AHC-07; clarify cross-reference target as "AI Bill of Rights §4.7". |

### Resolved Errata

*(None yet.)*

### Deferred to Next Revision

*(None yet.)*

---

## Versioning Convention for Errata Updates

When an erratum is resolved in the editable current.md (e.g., `specs/osara/current.md`), the change is also recorded in the [CHANGELOG](CHANGELOG.md). Immutable release snapshots in `releases/` are **never modified**; errata are tracked in this register instead. The next versioned release supersedes the prior release including any accumulated errata.

---

*Errata Register — Open Source United — CC BY 4.0 — March 2026*
