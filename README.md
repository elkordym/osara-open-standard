# OSARA Open Standard

> **OSARA — Open Sovereign Agent Reference Architecture** — the open standard for sovereign, portable, interoperable, and accountable AI agents, published by **Open Source United**, a Community of Practice of the United Nations.

This repository hosts the canonical text and governance machinery for the **OSARA Standards Family**:

| Document | Role | Current Version |
| --- | --- | --- |
| [OSARA Overview & Concepts](specs/osara-overview/current.md) | Informative — introduction for executives, policymakers, journalists, civil society | `v0.4-draft.1` |
| [OSARA Specification](specs/osara/current.md) | Normative — mandatory requirements for compliant implementations | `v0.4-draft.1` |
| [AI Bill of Rights](specs/ai-bill-of-rights/current.md) | Policy — rights framework, companion to OSARA | `v1.1-draft.1` |
| [OSARA Threat Model](specs/osara-threat-model/current.md) | Informative — adversary model, threats, mitigations, residual risks | `v0.4-draft.1` |
| [OSARA Privacy Considerations](specs/osara-privacy/current.md) | Informative — data flows, identifiers, privacy properties | `v0.4-draft.1` |

## Vision

We believe the next era of AI must belong to people, not platforms. OSARA and the AI Bill of Rights together define a future where every individual, enterprise, and government can operate trusted AI agents that are sovereign, portable, interoperable, and accountable by design.

Our vision is to make this the global open standard for human-centered AI — a world where innovation moves fast without sacrificing dignity, privacy, labor rights, safety, or democratic control. We are building the technical and governance foundation for an AI ecosystem that is open, auditable, and fair for everyone.

This is bigger than software. It is a shared mission to ensure AI amplifies human freedom and human potential at planetary scale.

The time to define these rules is now, before private-sector defaults become the global rules of the game for everyone. Your help, contributions, and participation directly accelerate adoption of this open standard. The faster OSARA and the AI Bill of Rights are adopted, the stronger the expectation and obligation for major platforms and providers to comply with these principles.

## Leadership

- **Primary Author / Lead Maintainer**: Mostafa M. Elkordy (`@elkordym`)
- **Co-Chair, Open Source United (UN Open Source Community of Practice)**: Mostafa M. Elkordy (`@elkordym`)
- **Contributors**: see [`AUTHORS.md`](AUTHORS.md) and the OSU public RFC process

## Repository Structure

```
specs/         The OSARA Standards Family (read this first)
  osara-overview/      Informative — overview & concepts
  osara/               Normative — the OSARA Specification
  osara-threat-model/  Informative — adversary model and mitigations
  osara-privacy/       Informative — data flows, identifiers, privacy properties
  ai-bill-of-rights/   Policy — rights framework, companion document

governance/    Charter, IPR Policy, Maintainers, Liaisons, templates
community/     Code of Conduct, Contributing guide, RFC participation
docs/          Site content (overview, roadmap, process, errata, comments register)
```

## Documentation Website

- Published release URL: [https://elkordym.github.io/osara-open-standard](https://elkordym.github.io/osara-open-standard)
- Future canonical URL: [https://opensource.unicc.org](https://opensource.unicc.org) — the OSU publication target post-migration
- Single source of truth for all specifications: the [`specs/`](specs/) directory

## Project Principles

- Open standards process — public RFCs, public comment periods, public dispositions
- Open participation with clear moderation
- Traceable change history — every release is an immutable snapshot under `releases/`
- Publicly documented decisions — see [`governance/DECISION_RECORD_TEMPLATE.md`](governance/DECISION_RECORD_TEMPLATE.md)
- Neutral, vendor-independent governance
- Royalty-free implementation — see [`governance/IPR_POLICY.md`](governance/IPR_POLICY.md)
- Mandatory open source components — see [AI Bill of Rights §4.7](specs/ai-bill-of-rights/current.md#article-iv--interoperability-portability-and-open-standards-normative)

## Branching Model

- `main`: stable, release-only branch
- `prerelease`: integration/staging branch for all merged pull requests
- Feature branches: short-lived branches that target `prerelease`

Release flow: feature branch → `prerelease` → release PR to `main`. See [`docs/BRANCHING_STRATEGY.md`](docs/BRANCHING_STRATEGY.md).

## Get Started

- New to OSARA? Start with [OSARA Overview & Concepts](specs/osara-overview/current.md).
- Implementing? Read the [OSARA Specification](specs/osara/current.md) and submit an [Implementation Report](governance/IMPLEMENTATION_REPORT_TEMPLATE.md).
- Auditing? Read the [Threat Model](specs/osara-threat-model/current.md) and [Privacy Considerations](specs/osara-privacy/current.md).
- Contributing? Read the [Contributing guide](community/CONTRIBUTING.md), the [IPR Policy](governance/IPR_POLICY.md), and the [Release Process](docs/RELEASE_PROCESS.md).
- Filing an erratum? Use the [Errata Register](docs/errata.md).
- Filing a public comment? Use the [Public Comments Register](docs/comments-register.md).
