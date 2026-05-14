# Roadmap

This roadmap reflects the published state of the OSARA Standards Family as of `v0.4-draft.1` / `v1.1-draft.1` (March 2026). It is a living document and is updated at every release boundary.

## Phase 1 — Repository Foundation

- [x] Create open-standard repository structure
- [x] Convert source drafts to markdown
- [x] Add governance and participation documents
- [x] Adopt branching, release, and versioning policies

## Phase 2 — First Public Draft (`v0.3` / `v1.0`)

- [x] Publish OSARA `v0.3-draft.1` and AI Bill of Rights `v1.0-draft.1`
- [x] Convert source drafts to markdown
- [x] Establish public comment process

## Phase 3 — Second Public Draft (`v0.4` / `v1.1`) — **current**

- [x] Publish OSARA `v0.4-draft.1` and AI Bill of Rights `v1.1-draft.1`
- [x] Introduce Owner Authorization Device (OAD), Integrity Measurement Architecture, Lock State Protocol, Incident Reporting Specification, Migration & Integrity Protocol
- [x] Restructure as a 3-document Standards Family (Overview, Specification, Bill of Rights) plus 2 informative companions (Threat Model, Privacy Considerations)
- [x] Adopt RFC 2119 / RFC 8174 conformance keyword convention
- [x] Add Status of This Document, Conformance Classes, Normative / Informative section markers, References sections
- [x] Add IPR Policy, Implementation Report Template, Liaisons register, Errata Register, Public Comments Register
- [ ] Open 60-day public comment window
- [ ] Collect implementation feedback from pilot adopters
- [ ] First disposition cycle of public comments

## Phase 4 — Release Candidate (`v0.4-rc.1` / `v1.1-rc.1`)

- [ ] Resolve open normative issues raised in public comment
- [ ] Second disposition cycle of public comments
- [ ] Freeze text for release candidate
- [ ] At least two independent implementations report against `v0.4-draft.1` per the [Implementation Report Template](governance/IMPLEMENTATION_REPORT_TEMPLATE.md)
- [ ] Publish `v0.4-rc.1` (OSARA) and `v1.1-rc.1` (Bill)

## Phase 5 — First Stable Release (`v1.0` / `v1.x`)

- [ ] Publish signed release artifacts
- [ ] Tag and announce stable versions
- [ ] Archive comment period outcomes
- [ ] **Post-quantum cryptography migration**: CRYSTALS-Kyber + CRYSTALS-Dilithium become mandatory; 12-month overlap window opens
- [ ] **Standards Family split**: at `v1.0`, the normative OSARA Specification will be split into a family of focused profiles in line with the publication practice of W3C, IETF, NIST, and ISO/IEC:
    - **OSARA-OV** Overview & Concepts (informative — exists today)
    - **OSARA-ARCH** Reference Architecture (informative — split out from current spec)
    - **OSARA-CORE** Core Specification (normative — mandatory components, audit, badges)
    - **OSARA-IDENT** Identity & Certificate Profile (normative — GIAC, OAD, jurisdiction)
    - **OSARA-NET** Network & Port Profile (normative — TLS, ports, encryption standards)
    - **OSARA-CONF** Conformance & Certification (normative — ACTS, badge tiers, AHC process)
- [ ] Migrate hosting from GitHub to GitLab (`opensource.unicc.org`) with full preservation of issue / RFC history
- [ ] Establish formal liaisons with ISO/IEC JTC 1/SC 42, NIST, ENISA, ITU-T, FIDO, W3C, IETF, OASIS
- [ ] Publish OSARA Trademark Policy and brand assets

## Phase 6 — Adoption and National Implementation

- [ ] National OSARA implementations: pilot in 3+ jurisdictions
- [ ] Community Agent Host certification programme launched
- [ ] Inspection Entity Registry operational with substantiated-complaint records
- [ ] Public Certificate Ledger and Public Badge Registry operational at production scale
- [ ] Annual OSARA Conformance Test Suite (ACTS) releases
- [ ] Triennial Bill of Rights public review per §9

---

*Roadmap last updated at OSARA `v0.4-draft.1` / AI Bill of Rights `v1.1-draft.1` publication (March 2026).*
