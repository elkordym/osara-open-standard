# Changelog

All notable changes to the OSARA Standards Family are recorded here. The Family follows semantic versioning per document; release cadence and compatibility rules are defined in [`docs/VERSIONING.md`](docs/VERSIONING.md) and the Governance Charter.

## Unreleased

- *(no changes since `v0.4-draft.1` / `v1.1-draft.1` publication)*

## `OSARA v0.4-draft.1` and `AI Bill of Rights v1.1-draft.1` — March 2026

This release introduces the OSARA Standards Family layout, adopts standards-grade publication practice (RFC 2119 keywords, Status of This Document, Conformance Classes, Normative References), and adds substantive new technical content centered on the Owner Authorization Device and the agent's self-defense and migration architecture.

### Repository structure

- Restructured `specs/` as a 5-document Standards Family:
    - `specs/osara-overview/` (new) — informative overview & concepts.
    - `specs/osara/` — normative OSARA Specification (now v0.4-draft.1).
    - `specs/osara-threat-model/` (new) — informative threat model.
    - `specs/osara-privacy/` (new) — informative privacy considerations.
    - `specs/ai-bill-of-rights/` — policy / rights framework (now v1.1-draft.1).
- Consolidated all diagram sources under `assets/diagrams/` as their canonical location.
- Centralised the community files (`CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`) under `community/`; the root copies now point to them.

### Governance and process

- Added [IPR Policy](governance/IPR_POLICY.md) (royalty-free patent non-assertion, defensive suspension, CC BY 4.0 copyright treatment).
- Added [Implementation Report Template](governance/IMPLEMENTATION_REPORT_TEMPLATE.md).
- Added [Liaisons Register](governance/LIAISONS.md).
- Added [Errata Register](docs/errata.md).
- Added [Public Comments Register](docs/comments-register.md).

### Substantive — OSARA Specification (`v0.3-draft.1` → `v0.4-draft.1`)

- **Unified GIAC**: P, E, and G agents all use a single certificate name (GIAC) distinguished by the `osara.tier` profile field. Replaces the per-tier certificate naming used in v0.3.
- **New §4.3 Owner Authorization Device (OAD)**: defines hardware trust tiers (A / B / C), action authorization tiers (Tier 1 routine / Tier 2 consequential / Tier 3 high-stakes), and the OAD interface requirements (OAD-01 through OAD-06).
- **New §4.4 Agent Runtime / OAD architectural separation**: the agent is two separately deployable components communicating exclusively via the ECL.
- **New §4.5 GIAC Provisioning Protocol**: defines the cryptographic process and three transports (NFC, USB HSM, Secured Network API).
- **New §9 Agent Migration and Integrity Protocol (MIP)**: 11 new requirements (MIG-01..11) for cryptographically verifiable agent container transfer.
- **New §10 Integrity Measurement Architecture (IMA)**: 8 new requirements (IMA-01..08) for boot-time and runtime self-verification, TPM sealing, 30-second heartbeat.
- **New §11 Lock State Protocol (LSP)**: graduated YELLOW / ORANGE / RED self-defense response.
- **New §12 Incident Reporting Specification (IRS)**: 8 new requirements (IRS-01..08) bounding what is automatically reported to authorities and what is owner-only.
- **AIM-03** updated: private keys must live in the OAD's hardware secure element; the AIM holds the certificate only.
- **ALE-10** added: log every OAD authorization event.
- **ECL-06** added: ECL is the exclusive OAD ↔ runtime channel.
- **HSB-05** added: missed heartbeat triggers YELLOW state.
- **AHC-07** added: inspection scope must verify IMA reference hash integrity and open source compliance.
- **§7.1 CAH** expanded with CAH-01..05 — cryptographic isolation, GIAC provisioning transport, MIP support, alternative identity verification, ECL non-interception.
- **§8 Protection Against Misuse** rewritten: appeals against improper AHC denial go through the competent national authority. Open Source United maintains the IER but does not adjudicate disputes.
- **§13 Encryption Standards**: added TPM Sealing row.
- **§18 Governance / Appeals**: clarified that OSU does not adjudicate certificate disputes.
- **§19 Glossary** updated with EAC, GRA, IMA, IRS, LSP, MIP, OAD, and updated GIAC to reflect unification.
- Section numbering rebased: §9..§16 in v0.3 are now §13..§20 in v0.4 (encryption, GIAC, ports, cross-tier, badge, governance, glossary, acknowledgements all shift).

### Substantive — AI Bill of Rights (`v1.0-draft.1` → `v1.1-draft.1`)

- Companion reference updated from OSARA v0.3 to OSARA v0.4.
- **§2.9** expanded to explicitly designate the OAD (OSARA §4.3) as the technical instrument through which a designated handler exercises authority.
- **§3.8 (new)**: right to an agent that actively defends its own integrity, referencing OSARA §10 (IMA), §11 (LSP), and bounding automatic authority reporting to §12.1.
- **§4.2** expanded to require transfers to be executed using the new OSARA §9 Migration and Integrity Protocol.
- **Annex A** cross-references updated to point at the v0.4 section numbers (e.g., revocation moved from §10.2 to §14.2; encryption moved from §9 to §13). The new §3.8 row is added.

### Editorial — both documents

- Adopted **RFC 2119 / RFC 8174** keyword convention. All normative MUST / MUST NOT / SHALL / etc. now carry their formal meaning.
- Added explicit **`[Normative]` / `[Informative]`** markers on every top-level section header.
- Added **Status of This Document** section to each spec with stable identifier, editor's draft URL, snapshot URL, maturity level, public comment period status, and errata pointer.
- Added **Conformance Classes** table to the OSARA Specification.
- Added **Annex A — Normative References** and **Annex B — Informative References** to the OSARA Specification.
- Pull-quote and call-out blocks converted to proper Markdown blockquote callouts (rather than 1-cell tables).
- Cross-references between OSARA and the Bill of Rights are now hyperlinks, not free text.

## Earlier Releases

- `v0.3-draft.1` (OSARA) and `v1.0-draft.1` (AI Bill of Rights) — first public draft. Repository baseline established. See `specs/osara/releases/v0.3-draft.1.md` and `specs/ai-bill-of-rights/releases/v1.0-draft.1.md`.
