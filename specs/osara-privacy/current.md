# OSARA — Privacy Considerations

> An informative companion to the OSARA technical specification, identifying the privacy properties of the standard, the data flows it permits, the data flows it prohibits, and the residual privacy risks adopters must consider in deployment.
>
> Published by **Open Source United**, a Community of Practice of the United Nations.
>
> **Version 0.4 — Draft for Public Comment — March 2026**
>
> Copyright © 2026 Open Source United — Released under CC BY 4.0 International License.

---

## Status of This Document

This is the current editable working draft of the **OSARA Privacy Considerations** document, version `v0.4-draft.1`. This document is **informative**. It contains no normative requirements; it explains how the normative requirements in the [OSARA Specification](../osara/current.md) and the [AI Bill of Rights](../ai-bill-of-rights/current.md) deliver privacy properties, and where deployment-level decisions are still required.

- **Stable identifier**: `urn:osu:osara-privacy:v0.4-draft.1`
- **Editor's draft**: this file (`specs/osara-privacy/current.md`)
- **Immutable snapshot**: [`specs/osara-privacy/releases/v0.4-draft.1.md`](releases/v0.4-draft.1.md)
- **Maturity level**: Informative

This document follows the spirit of [RFC 6973 — Privacy Considerations for Internet Protocols](https://www.rfc-editor.org/rfc/rfc6973). It is intended to be reviewed alongside applicable national and regional data protection law (GDPR, CCPA, LGPD, PIPL, the EU AI Act, and equivalents).

---

# 1. Privacy Principles in the OSARA Family

OSARA and the AI Bill of Rights together embody seven privacy principles, adapted from the IETF privacy framework, the GDPR, and the OECD Privacy Guidelines:

| Principle | How OSARA realises it |
| --- | --- |
| **Minimisation** | Raw identity credentials are never stored — only one-way hashes. Audit logs record metadata only (timestamps, identities, action types), never message content. |
| **Owner control** | The agent's private key is held in the owner's OAD. The agent's memory is encrypted under that key. No third party can decrypt without the owner. |
| **Purpose binding** | Every delegation is scoped to a specific resource, action type, and expiry. Cross-context information re-use is prohibited (Bill of Rights §4.6). |
| **Transparency** | The agent maintains a versioned changelog of what it has learned. Every interaction is logged for the owner. Audit logs are exportable. |
| **Auditability** | Logs are cryptographically chained. Inspection entities verify integrity. Tampering is detectable on every IMA heartbeat. |
| **Portability** | Memory is exportable in an open format at any time. Migration cannot be blocked, delayed, or penalized. |
| **Proportional disclosure** | Different parties see different data. Audit log access is restricted by warrant. Skill inventory is gated by POA. Memory is gated by OAD key. |

These properties are technical, not contractual. They survive any change in terms of service, ownership of the host, or regime change of the jurisdiction.

# 2. What Is and Is Not Considered Personal Data

This section classifies the data types OSARA introduces. Adopters must apply their jurisdiction-specific data-protection definitions in addition.

| Data Type | Personal data? | Stored where | Notes |
| --- | --- | --- | --- |
| Owner's raw national identity credential | Yes — and highly sensitive | **Nowhere in OSARA** | OSARA never stores, transmits, or logs the raw credential. Hashing is done at the GRA before issuance. |
| `osara.identityAnchorHash` (SHA-3-256 hash + salt) | Pseudonymous identifier | GIAC certificate | One-way; cannot be reversed without the salt. Treated as personal data under most regimes until proven otherwise. |
| Owner's GIAC certificate (public part) | Personal data — pseudonymous | AIM, PCL | Includes jurisdiction, tier, scope, and DID. The PCL is public. |
| Owner's DID (`osara.ownerDID`) | Personal data | GIAC certificate | The DID resolves to a controller document chosen by the owner. |
| Audit log entries (ALE) | Personal data — operational | Agent's ALE storage | Metadata only; never message content. Retained 16 months. |
| Skill inventory | Personal data — economic | SI endpoint | Accessible only via POA-authorized inspection. |
| Portable Memory Store (PMS) | Personal data — content | Encrypted in PMS storage | Encrypted under OAD-derived key. Provider cannot read. |
| Health beacon contents | Operational metadata | Broadcast on `:4403` | No personal content; designed for public observability. |
| Health Certificate (AHC) | Operational metadata | AIM, PCL | Publicly verifiable; no personal content. |
| Forensic snapshot (RED state report) | Operational forensic data | Sealed; reported to authority | Contains component hashes, ALE state, lock log, TPM measurements. **Never contains** memory, skills, conversation history, or personal data. |
| Inspection event entries | Personal data — operational | ALE | Contains inspector identity hash, session duration, authorization method. |

# 3. Data Flows and Their Constraints

## 3.1 Owner ↔ Agent Runtime

| Flow | Channel | Constraint |
| --- | --- | --- |
| Owner authorizes an action | OAD → Runtime via ECL | Signed by OAD private key; bound to specific session; logged in ALE |
| Runtime requests a signature | Runtime → OAD via ECL | Only the data-to-sign crosses the channel; the private key never does |
| Owner reads ALE | OAD → ALE port `:4402` | Authenticated; read-only |

## 3.2 Agent ↔ Other Agents (cross-tier)

| Flow | Channel | Constraint |
| --- | --- | --- |
| GIAC presentation | Port `:4400` | Public — GIAC is a public certificate |
| Agent-to-agent payload | Port `:4401` mTLS 1.3 | Double-envelope (TLS outer + AES-256-GCM inner). Recipient cannot replay or forward without further owner consent. |
| Delegation token issuance | Port `:4404` mTLS 1.3 | Dual-signed; scope and expiry encoded; recorded in both ALEs |

## 3.3 Agent ↔ AI Model Provider

| Flow | Channel | Constraint |
| --- | --- | --- |
| Inference call | TLS 1.3 + certificate pinning | The model provider receives the prompt for inference. **The provider may not receive the agent's raw memory or skill inventory without explicit signed owner consent.** Message content is not logged in the ALE. |
| Logged metadata | Recorded in ALE | model identifier, invocation timestamp, token count only |

> **Implication for adopters**: an OSARA-compliant agent powered by a closed frontier API still discloses prompt content to that provider on each invocation. The Bill of Rights §3.3 prohibits the *provider* from using that content for mass-surveillance, behavioural profiling, or training without explicit consent — but enforcement is at the provider's contractual layer, not OSARA's technical layer. Owners concerned about prompt-content disclosure should run a local open-source model under §7.2 "Local Execution".

## 3.4 Agent ↔ Cloud Host (CAH or commercial provider)

| Flow | Channel | Constraint |
| --- | --- | --- |
| Container compute | Host kernel ↔ container | The host provides CPU, RAM, storage. It has no access to AIM private key (OAD-isolated), encrypted PMS (OAD-derived key), or sealed ALE. |
| ECL traffic in transit | Host network stack | Host sees encrypted bytes; cannot decrypt. |
| Persisted PMS at rest | Host storage | Encrypted at rest under OAD-derived key. Host cannot decrypt. |

The host **does** see container start/stop, resource utilization, and external network destinations (at the IP level). These are operational data that adopters in privacy-sensitive sectors (healthcare, legal, journalism, opposition politics) should consider.

## 3.5 Agent ↔ Inspection Entity

| Flow | Channel | Constraint |
| --- | --- | --- |
| ICE session | Port `:4406`, POA-gated | Owner physically authorizes per session. Maximum 4-hour session. Logged in ALE. |
| Inspector accesses Skill Inventory | SI endpoint via ICE | Only during POA-authorized session; logged. |
| Inspector reviews ALE | ALE endpoint via ICE | Only during POA-authorized session; logged. Inspector signs AHC; AHC is published to PCL. |

## 3.6 Agent ↔ Law Enforcement

This is governed by Bill of Rights §3.2 and OSARA POA-06/POA-07. Law enforcement access requires a valid court warrant (unless the owner gives explicit consent, which may be refused). Access is limited strictly to audit logs; memory, skills, configuration, and content require a separate, specific warrant. All access is recorded in a tamper-proof log and the owner is notified as required by applicable law unless notification is lawfully delayed.

## 3.7 Agent ↔ Competent Authority (RED State)

Automatic reporting is restricted to the three triggers in OSARA §12.1 (GIAC key extraction attempt, GIAC forgery attempt, ALE tamper). The report contains only:

- IRS trigger type
- Timestamp
- Hash of sealed forensic snapshot
- Hashed GIAC identifier
- OSARA runtime version

**It does not contain** agent memory, skills, conversation history, owner personal data, or GIAC private key material (OSARA §12.2 / IRS-04, IRS-05).

# 4. Privacy-Relevant Identifier Linkability

A small number of identifiers in OSARA are stable across an agent's life. Adopters should be aware of the linkability properties:

| Identifier | Stability | Public? | Linkability concern |
| --- | --- | --- | --- |
| GIAC serial number | Stable until renewal | Yes (PCL) | A single GIAC binds all the agent's interactions across its 12 / 24 / 36-month validity to a single pseudonym. Tracking parties can correlate interactions. |
| `osara.identityAnchorHash` | Stable across renewals (same identity + salt) | Yes (in GIAC) | More problematic — two agents owned by the same person across different sessions and certificates can be correlated by their anchor hash. **Adopters who require unlinkability across renewals must request a fresh salt at renewal time.** This is permitted by the specification but not the default; jurisdictions may differ. |
| `osara.ownerDID` | Stable across multiple agents owned by the same person | Yes | Designed for cross-agent attribution of work performed by the same human. Provides linkability by design. |
| Container outbound IPs | Visible to the host network | Network-observable | Tor-style mix-net hosting is not part of OSARA but is compatible with it. |

> **Recommendation**: where unlinkability across renewals is required (e.g., for users in adversarial jurisdictions), national OSARA implementations should provide an option for fresh-salt renewal that produces a non-correlatable `identityAnchorHash`. The trade-off is that legal-evidence continuity across renewals becomes harder; this must be a deliberate jurisdictional choice.

# 5. Specific Privacy Properties of the Standard

## 5.1 Confidentiality of Memory

The PMS is encrypted at rest under a key derived from the GIAC private key held in the OAD. The host has no path to plaintext memory. This is the strongest privacy guarantee in the standard and is the technical realization of the Bill of Rights §2.10 (an agent must serve its owner exclusively).

## 5.2 No Content Logging

ALE records *that* an event happened and *who* was involved (by pseudonym hash). It does not record *what was said*. This is a deliberate design choice that limits the surveillance value of agent logs while preserving the audit trail value.

Adopters in regulated industries (healthcare, legal, financial advice) where regulator-mandated content retention applies must implement that retention at the application or skill layer, not at the OSARA ALE layer.

## 5.3 No Persistent Conversation Memory at AI Model Provider

OSARA does not directly control AI model providers, but its ALE-logged metadata makes it possible to detect non-compliant providers — those who retain conversation content beyond a session, or who use it for training without consent. The Bill of Rights §3.3 prohibits these uses. National implementations should require contractual terms with model providers that align with the Bill.

## 5.4 Owner Visibility Into Own Agent

Every action the agent takes is visible to the owner via the OAD (Bill of Rights §3.5 and OSARA §5.3 ALE). This is a privacy-positive property: the owner is never surveilled by their own agent without their knowledge.

## 5.5 No Pre-emptive Reporting

The standard explicitly forbids automatic reporting to any authority outside the three IRS-01/02/03 triggers (OSARA §12.1, Bill of Rights §3.8). This blocks legitimate-sounding extensions ("automatically report when the agent draws certain inferences", "automatically share with public-health authorities") that would convert OSARA into a surveillance platform. Expanding the trigger set requires a public RFC and 60-day comment period.

# 6. Privacy in Cross-Border Operation

Where an agent owner is in one jurisdiction and a host or counterparty is in another, the relevant privacy regimes can conflict. The standard's design choices make several aspects more tractable:

- **Memory cannot be lawfully demanded by a host's jurisdiction**, because the host does not hold the key. A demand for memory must be directed to the owner, in the owner's jurisdiction, under that jurisdiction's law.
- **Identity anchor hash** is jurisdiction-tagged (`osara.jurisdiction`), making it explicit which national regime defines the meaning of the underlying credential.
- **Cross-border G-Agent operation** requires bilateral OSARA treaty validation — this is intentionally a high bar to prevent unilateral overreach.
- **Where local law conflicts with Bill of Rights provisions** (e.g., §3.2 on log access), §3.2 explicitly defers to local law. National implementations should publish the operational consequences of this deferral.

# 7. Open Privacy Questions for v0.4 Public Comment

These are explicitly open for community input as part of the v0.4 public comment period:

1. **Default salt-rotation policy** at GIAC renewal — should it be opt-in or opt-out by default, and at what jurisdictional level is the choice made?
2. **Tor-style mix-net hosting compatibility** — should the spec provide an explicit profile, or remain agnostic?
3. **Aggregate transparency reporting** by Community Agent Hosts — what is the minimum publishable set (number of agents, jurisdictions, warrants received) that does not compromise individual owners?
4. **Standardised model-provider contract template** — should OSU publish a recommended terms-of-service template aligned with Bill of Rights §3.3 for model providers used by certified agents?
5. **Inspection-entity privacy obligations** — beyond the prohibition on raw-identity disclosure, what additional confidentiality obligations should the IER impose on inspecting entities?
6. **Memory-store key escrow for digital estate (§6.3)** — what mechanism balances inheritance rights with confidentiality of the deceased owner's memory from non-designated parties?

Comments on any of these are welcome via the public RFC process.

# 8. Implementer Checklist (Non-Normative)

Adopters building OSARA-compliant infrastructure should at minimum verify the following privacy properties of their deployment:

- [ ] Raw identity credentials never appear in any log, container image, backup, or telemetry pipeline.
- [ ] PMS encryption key is provably derived only from the OAD-held GIAC private key.
- [ ] Host operator personnel have no administrative path to read the PMS plaintext.
- [ ] ALE never contains message content, prompts, or AI model outputs.
- [ ] Forensic snapshots emitted under RED state are content-free.
- [ ] AI model providers used by the agent are bound by contractual terms aligned with Bill of Rights §3.3.
- [ ] Salt rotation at GIAC renewal is offered as an option to the owner.
- [ ] Cross-border data flows are documented and aligned with the owner's domicile law.
- [ ] CAH operators publish their inspection-entity, warrant, and transparency-report obligations.

---

*OSARA Privacy Considerations v0.4-draft.1 — Copyright © 2026 Open Source United — CC BY 4.0 — March 2026*
