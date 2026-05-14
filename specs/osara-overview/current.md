# OSARA — Overview & Concepts

> A short, non-normative companion to the OSARA technical specification, written for executives, policymakers, journalists, civil society, and newcomers to the standard.
>
> Published by **Open Source United**, a Community of Practice of the United Nations.
>
> **Version 0.4 — Draft for Public Comment — March 2026**
>
> Copyright © 2026 Open Source United — Released under CC BY 4.0 International License.

---

## Status of This Document

This is the current editable working draft of the **OSARA Overview & Concepts** document, version `v0.4-draft.1`. It is published as the introductory, **informative** companion to the [OSARA technical specification](../osara/current.md) and the [AI Bill of Rights](../ai-bill-of-rights/current.md).

- **Stable identifier**: `urn:osu:osara-overview:v0.4-draft.1`
- **Editor's draft**: this file (`specs/osara-overview/current.md`)
- **Immutable snapshot**: [`specs/osara-overview/releases/v0.4-draft.1.md`](releases/v0.4-draft.1.md)
- **Maturity level**: Informative — no normative requirements appear in this document.

For the binding technical requirements, refer to the [OSARA Specification](../osara/current.md).
For the rights framework, refer to the [AI Bill of Rights](../ai-bill-of-rights/current.md).

---

# 1. What OSARA Is

**OSARA** stands for **Open Sovereign Agent Reference Architecture**. It is an open standard, published by Open Source United (a UN Community of Practice), that defines what it takes for an Open Source AI Agent to be considered trustworthy, portable, auditable, and accountable — regardless of who built it, who hosts it, or which AI model powers it.

OSARA's promise is simple: any agent that conforms to the standard can be trusted, anywhere, by anyone, with the same level of confidence we already place in vehicles that have passed inspection, food that has been certified for sale, or banks that hold a regulator's licence.

# 2. The Problem OSARA Solves

AI agents are about to become the most consequential technology platform of the next two decades. Without an open standard:

- **Lock-in by default.** Each platform creates its own agent format. Switching costs become prohibitive.
- **No accountability.** When an agent acts on a person's behalf and something goes wrong, no one can verify what it did or who authorized it.
- **No portability.** A person's accumulated agent knowledge and skills become hostage to whichever provider holds the data.
- **No sovereignty.** Governments lose the ability to enforce their own laws on agents operating within their jurisdiction.
- **No human centre.** Agents that should serve the user end up serving the platform that hosts them.

OSARA is the technical foundation that makes the alternative possible: AI agents that are interoperable across providers, auditable by independent inspectors, portable across hosting environments, and bound to the human or legal entity that owns them.

# 3. The Three Audiences for the OSARA Family

OSARA is published as a small family of documents because no single document can serve everyone equally well. The family is intentionally short and focused.

| Audience | What you should read |
| --- | --- |
| **Executives, policymakers, journalists, civil society** | This document (Overview & Concepts) and the [AI Bill of Rights](../ai-bill-of-rights/current.md) |
| **Implementers, integrators, security engineers** | The [OSARA Specification](../osara/current.md) — normative requirements with MUST/SHALL keywords |
| **Auditors, regulators, inspection entities** | The OSARA Specification, the [Threat Model](../osara-threat-model/current.md), and the [Privacy Considerations](../osara-privacy/current.md) |
| **National implementation authorities** | All of the above, plus relevant national law on identity, signature, and data protection |

A future major release (planned for v1.0 in 2027) will split the technical specification into a larger family of focused profiles — Core, Identity, Network, and Conformance — in line with the publication practice of W3C, IETF, NIST, and ISO/IEC.

# 4. The Three Agent Tiers

OSARA recognises three sovereign tiers of agent. Every agent in the OSARA ecosystem belongs to exactly one tier, encoded into its certificate.

| Tier | Owner | Example |
| --- | --- | --- |
| **Personal Agent (P-Agent)** | An individual person | Your personal assistant, hired with you when you take a job |
| **Enterprise Agent (E-Agent)** | A registered legal entity | A company's customer service agent, supplier agent, or HR agent |
| **Government Agent (G-Agent)** | A recognized government or regulatory body | A national tax authority's filing agent, a benefits administration agent |

The model is not a hierarchy of power — it is a model of **scope and accountability**. P-Agents have the lowest privilege; G-Agents have the highest. But every tier is subject to the same identity, audit, and inspection requirements. No tier escapes accountability.

# 5. The Person-and-Agent Employment Model

OSARA and the AI Bill of Rights together propose a new model of employment for the era of agentic AI: **the person and their agent are hired together as a single unit**. This is one of the most important ideas in the standard.

- When you take a job, you bring your personal agent with you.
- Your agent works on your behalf inside the organization, under the delegation scopes you authorize.
- You — the human — remain fully accountable for everything your agent does in your name.
- The organization manages outputs and gives direction to you. It does not manage your agent.
- When you leave the job, your agent's memory, skills, and identity leave with you. Nothing stays behind.

This model is the alternative to the unacceptable outcome where organizations replace humans with fleets of unaccountable automated agents. It keeps people in the economy. It keeps people accountable. It keeps people in charge.

# 6. The Core Technical Idea — Sovereignty by Cryptography

OSARA's central technical claim is that **sovereignty cannot be granted by terms of service — it must be enforced by cryptography**. The specification turns four classical principles into hard technical guarantees:

| Principle | OSARA mechanism |
| --- | --- |
| **You own your agent's identity.** | The agent's private key lives in your Owner Authorization Device (OAD) — your phone, smart card, or hardware key. It never leaves the hardware. No platform, employer, or government can sign on your behalf. |
| **You own your agent's memory.** | The Portable Memory Store is encrypted at rest with a key derived from your OAD. No host can read it. You can export it any time, in an open format, in 30 days or less. |
| **No one can lie about what your agent did.** | Every action your agent takes is recorded in a cryptographically chained audit log. Tampering breaks the chain and is detected immediately by the continuous Integrity Measurement Architecture. |
| **No one can secretly modify your agent.** | Any change to the agent that doesn't go through your OAD authentication is detected as tampering. The agent locks itself down. The forensic snapshot is sealed. |

These four guarantees are independent of any individual product, provider, or country. They are the bedrock of the OSARA promise.

# 7. The Open Source Requirement

The mandatory components of every OSARA-certified agent — identity, audit, encryption, gateway, and physical authorization — **must** be built on open source software under an OSI-approved licence.

This is not ideology. It is a security requirement. An agent that cannot be audited cannot be trusted. The rights established in the AI Bill of Rights — that an agent serves its owner, that logs cannot be falsified, that no hidden instructions work against the owner — are unverifiable in a closed system. Open source mandatory components are the technical guarantee that sovereignty is real and not merely claimed.

Proprietary code is fully welcome — in skill implementations, AI model integrations, workflow logic, and business layers — provided it does not override, wrap, replace, or obscure any mandatory open source component.

# 8. Health Certificates, Inspection, and Badges

OSARA borrows from a long-established model in physical engineering: **periodic, certified inspection**.

- Every agent must pass an **Annual Health Certificate** inspection — equivalent in nature to a vehicle roadworthiness test.
- Inspections can be issued by either a government-certified inspection body **or** an accredited private sector inspection authority. Both pathways are fully equal.
- Inspections are technical, not political. A Health Certificate may not be denied for any reason other than demonstrable technical non-compliance with the OSARA specification.
- Conformance is expressed through three badge levels: **OSARA-C (Conformant)**, **OSARA-A (Audited)**, and **OSARA-S (Sovereign)**. Each builds on the prior level.

# 9. How OSARA Relates to the AI Bill of Rights

The two documents are companions, designed to be read and implemented together.

- The **AI Bill of Rights** establishes **what** rights people, workers, communities, and governments hold in relation to AI agents.
- **OSARA** defines **how** those rights are enforced technically — at the level of certificates, keys, ports, audit logs, and inspection procedures.

Where the Bill says *"every person has the right to transfer their agent to another provider without penalty"* (§4.2), OSARA defines the Agent Migration and Integrity Protocol (§9) that makes the transfer cryptographically verifiable. Where the Bill says *"every person has the right to an agent that actively defends its own integrity"* (§3.8), OSARA defines the Integrity Measurement Architecture (§10), the Lock State Protocol (§11), and the Incident Reporting Specification (§12) that operationalize that right.

The Bill of Rights' Annex A is a complete cross-reference table mapping every right to the specific OSARA technical mechanism that enforces it.

# 10. Governance — Why Open Source United

OSARA and the Bill of Rights are not produced by a vendor, a startup, or a single national regulator. They are produced by **Open Source United (OSU)**, a Community of Practice of the United Nations. OSU's role is to be the neutral, vendor-independent steward of the standard — running the public RFC process, maintaining the registries (PCL, PBR, IER), and convening the multi-stakeholder OSARA Steering Committee.

OSU does **not** adjudicate disputes between owners, inspection entities, governments, or platforms. Those disputes are resolved by the competent administrative or regulatory authority in the relevant jurisdiction under applicable national law. OSU's authority is technical and procedural — it does not displace national institutions.

# 11. Where We Are in the Standard's Lifecycle

| Phase | Status |
| --- | --- |
| Repository foundation | Complete |
| First public draft (v0.3 / v1.0) | Published March 2026 |
| **Second public draft (v0.4 / v1.1)** | **You are here.** Public comment open. |
| Release candidate (v0.4-rc.1 / v1.1-rc.1) | Planned 2026 |
| First stable release (v1.0 / v1.x) | Target 2027 — includes post-quantum cryptography migration |
| Document family split | Target 2027 — split spec into Core / Identity / Network / Conformance / Architecture profiles |

See the [Roadmap](../../docs/ROADMAP.md) for the current detailed plan.

# 12. How to Participate

OSARA is built in the open. Anyone may contribute.

- **Read** the [OSARA Specification](../osara/current.md) and the [AI Bill of Rights](../ai-bill-of-rights/current.md).
- **Comment** through the public RFC process — see the [Community Communication guide](../../docs/COMMUNITY_COMMUNICATION.md).
- **File errata** for clarifications and corrections via the [Errata Register](../../docs/errata.md).
- **Implement** the standard — implementations are tracked via the [Implementation Report Template](../../governance/IMPLEMENTATION_REPORT_TEMPLATE.md).
- **Adapt** the standard for national implementation — the documents are CC BY 4.0 licensed; you only need to credit Open Source United as the origin.

---

*OSARA Overview & Concepts v0.4-draft.1 — Copyright © 2026 Open Source United — CC BY 4.0 — March 2026*
