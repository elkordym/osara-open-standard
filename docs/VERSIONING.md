# Versioning

## Document Versions

- Draft: `vX.Y-draft.N`
- Release candidate: `vX.Y-rc.N`
- Stable: `vX.Y`
- Clarification-only patch: `vX.Y.Z`

## File Layout

- Working drafts live at:
  - `specs/osara/current.md`
  - `specs/ai-bill-of-rights/current.md`
- Immutable published snapshots live at:
  - `specs/<document>/releases/<version>.md`
- Git tags mirror release snapshots and are the authoritative release markers.

## Change Types

- **Normative**: changes compliance or rights obligations
- **Editorial**: wording clarity without behavior change
- **Process**: governance/release workflow only

Normative changes require explicit rationale and public traceability.
