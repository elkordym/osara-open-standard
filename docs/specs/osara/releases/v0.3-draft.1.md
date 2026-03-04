# OSARA v0.3 Draft

> Source: OSARA_v0.3_Specification.docx

OSARA

Open Sovereign Agent Reference Architecture

A Community of Practice of the United Nations

Mandatory Component Specification for Open Source AI Agents
Personal  \|  Enterprise  \|  Government

Published by Open Source United

Version 0.3 — Draft for Public Comment

March 2026

Copyright © 2026 Open Source United — Released under CC BY 4.0 International License

Principal Author acknowledged in Section 16

## 1. Purpose and Scope

OSARA defines the mandatory components, encryption requirements, identity standards, port specifications, skill integrity rules, portability requirements, and certification criteria that any compliant Open Source AI Agent must implement — regardless of its tier (Personal, Enterprise, or Government).

OSARA is published and stewarded by Open Source United, a Community of Practice of the United Nations. It is an open specification — anyone may implement it freely under CC BY 4.0, provided they credit Open Source United as the origin.

What OSARA Is NOT
OSARA does not mandate which AI model powers an agent, nor how agents are built internally. Agents may be powered by frontier AI models via secure API, local open source models, or a combination of both. OSARA mandates only the structural components, identity, encryption, portability, and audit requirements needed to participate in the certified ecosystem.

## 2. The Three-Tier Agent Model

OSARA defines three sovereign agent tiers. Each tier has its own ownership boundary, government-anchored identity, mandatory components, and portability requirements.

| Tier | Ownership & Identity Anchor | Trust Level & Hosting Responsibility |
| --- | --- | --- |
| Personal Agent (P-Agent) | Owned by an individual. Identity is cryptographically anchored to a government-recognized identity credential, the specific form of which is determined by the owner's national jurisdiction. | Lowest privilege. Owner bears full responsibility for hosting, updates, and health. Must run in PaaS or local modality — never SaaS. Community Agent Hosts (non-profit PaaS) are a permitted alternative for individuals without technical infrastructure. |
| Enterprise Agent (E-Agent) | Owned by a registered legal entity. Identity is anchored to the entity's government-issued tax or registration identifier (EIN, VAT ID, Company Registration Number, or jurisdictional equivalent). | Mid-level privilege. Can interact with P-Agents and G-Agents under licensed scope. Owner responsible for all sub-agents it initiates. |
| Government Agent (G-Agent) | Owned by a recognized government or regulatory body. Identity is anchored to the official government entity registration identifier per constitutional or statutory authority. | Highest privilege. Issues GIACs. Defines audit rules. Responsible for all sub-agents it initiates. |

## 3. Architecture Diagram

The diagram below illustrates the full three-tier agent ecosystem — how P-Agents, E-Agents, and G-Agents are structured, how they communicate, and how identity is established and verified at every interaction.

Figure 1 — OSARA Agent Ecosystem: Communication Flows and Authentication Chain

![OSARA Agent Ecosystem Diagram](/assets/diagrams/osara-agent-ecosystem.png)

## 3.1 Diagram Key

| Arrow Type | Meaning |
| --- | --- |
| Solid dark lines | Direct GIAC issuance from the Government Certificate Authority to agents |
| Dashed gold lines | Delegated certificate flows — GCA issues to E-Agents and P-Agents via Registration Authority |
| Solid blue lines | Enterprise-to-enterprise communications over mutual TLS 1.3 on port :4401 |
| Solid light blue lines | P-Agent initiated interactions toward E-Agents (consent token required) |
| Dashed purple lines | Audit and certification flows between agents and the OSARA Audit Body (OAB) |
| Dashed gray lines | Certificate verification lookups against the Public Certificate Ledger (PCL) |
| Dashed green lines | Skill signature and catalog flows |
| Teal lines | Portable Memory Store migration and access flows |

## 3.2 Authentication Flow — Step by Step

| Step | Description |
| --- | --- |
| Step 1 — Present GIAC | Connecting agent presents its GIAC on AIM port :4400. The certificate encodes tier, scope, jurisdiction-specific identity anchor hash, and GCA signature. |
| Step 2 — Verify Signature | Receiving agent fetches the GIAC and cryptographically verifies the GCA signature. |
| Step 3 — Check PCL & CRL | Receiving agent checks the PCL and Certificate Revocation List to confirm the certificate has not been revoked. |
| Step 4 — Enforce Tier Rules | Tier interaction rules are validated: scope authorization, consent tokens, and licensing checked. |
| Step 5 — Physical Auth if Inspection | If the session is an inspection, the owner physically authorizes connection via biometric or hardware security token (BOC). |
| Step 6 — mTLS Handshake | Mutual TLS 1.3 handshake on port :4401 with Perfect Forward Secrecy. |
| Step 7 — Double Encryption | Payloads double-encrypted: outer TLS + inner AES-256-GCM keyed to recipient AIM public key. |
| Step 8 — Synchronized Audit Log | Transaction written to ALL parties' ALE within a ±500ms tolerance window referencing a common NTP/GPS time source. Excess drift triggers transaction review flag. |

## 4. Government-Anchored Identity

Every OSARA agent must be cryptographically bound to a government-recognized identity anchor. The specific form of this anchor is determined by the owner's national jurisdiction — OSARA does not mandate a specific identifier type globally. National implementations of OSARA define which government credentials are acceptable within their jurisdiction.

## 4.1 Identity Anchors by Tier

| Agent Tier | Identity Anchor (Jurisdiction-Defined) | Implementation Rule |
| --- | --- | --- |
| P-Agent (Personal) | A government-recognized personal identity credential as defined by the owner's national jurisdiction. Examples include: national identity card, digital ID wallet, passport identifier, or equivalent credential accepted by the national OSARA Registration Authority. | The identifier is hashed using SHA-3-256 with a government-issued salt and embedded in the GIAC. The raw identifier is NEVER stored, transmitted, or logged. National implementations specify which credentials qualify. |
| E-Agent (Enterprise) | Government-issued entity identifier used for tax or registration purposes (EIN, VAT ID, Company Registration Number, or jurisdictional equivalent). | The entity ID hash is embedded in the GIAC. The GCA validates the entity is in good legal standing before issuance. |
| G-Agent (Government) | Official government entity registration identifier per constitutional or statutory authority. | Cross-border G-Agent interactions require bilateral OSARA treaty validation of identity anchors. |

### Jurisdiction Flexibility

OSARA deliberately does not mandate a specific government ID type (such as a Social Security Number). Each country's national OSARA implementation authority determines which government-recognized credentials are acceptable identity anchors within their jurisdiction. This allows democracies, federal systems, and countries with different ID frameworks to implement OSARA without being forced into a single identity model.

### Privacy Protection

The raw identity credential is NEVER stored in the GIAC, in any log, or transmitted in any message. Only a one-way SHA-3-256 hash combined with a government-issued salt is embedded. The original credential cannot be reverse-engineered from the hash.

## 4.2 Physical Owner Authorization — Tamper-Proof Access Control

Every agent of all tiers must implement a Physical Owner Authorization (POA) module — a mandatory tamper-proof component that gates inspection access and administrative actions behind real-time physical authorization by the owner. This replaces the earlier 'biometric-only' requirement to ensure accessibility for all individuals.

| Requirement ID | Requirement |
| --- | --- |
| POA-01 | The agent must expose a dedicated Inspection Clearance Endpoint (ICE) that is closed by default and requires explicit physical owner authorization to open |
| POA-02 | Physical authorization must use at minimum ONE of the following, of equal standing: (a) biometric verification — fingerprint, facial recognition, or iris scan; OR (b) hardware security token physically held by the owner (FIDO2/WebAuthn compliant). Both methods are fully equivalent — neither is a lesser fallback. |
| POA-03 | Individuals who cannot use biometric methods due to disability, medical condition, or religious objection must be accommodated via the hardware security token path without any reduction in rights or functionality |
| POA-04 | ICE access grants a time-limited session (maximum 4 hours) to the authorized inspection entity. Session automatically closes on expiry. |
| POA-05 | Every ICE access event must be logged in the ALE with: authorization method used, inspector identity hash, session duration, and actions performed |
| POA-06 | The POA module must be tamper-evident: any tampering attempt triggers an immediate owner alert and locks the agent into restricted mode |
| POA-07 | No remote override of physical authorization is permitted — not by cloud providers, AI model providers, or any government entity without a court-ordered physical access procedure under applicable national law |
| POA-08 | For inspection entities to connect to the ICE, the owner must be physically present and authorize the connection in real time using their chosen POA method |

## 5. Mandatory Components

Every OSARA-compliant agent must implement ALL of the following components. Absence of any single component disqualifies the agent from certification.

## 5.1 Agent Identity Module (AIM)

| Requirement ID | Requirement |
| --- | --- |
| AIM-01 | Must hold a valid GIAC containing the owner's hashed jurisdiction-defined identity anchor |
| AIM-02 | Must generate and store a unique Agent Key Pair (Ed25519 preferred or RSA-4096 minimum) |
| AIM-03 | Private keys must be stored in a hardware-backed secure enclave or HSM-equivalent vault |
| AIM-04 | Must support zero-downtime certificate rotation |
| AIM-05 | Must expose a read-only public identity endpoint on AIM port :4400 |
| AIM-06 | Must include agent tier (P/E/G), jurisdiction, and hashed identity anchor in the certificate |

## 5.2 Encrypted Communication Layer (ECL)

| Requirement ID | Requirement |
| --- | --- |
| ECL-01 | All external communication MUST use TLS 1.3 or higher |
| ECL-02 | Agent-to-agent payloads MUST use double-envelope encryption (TLS + AES-256-GCM keyed to recipient AIM public key) |
| ECL-03 | Must implement Perfect Forward Secrecy (PFS) via ephemeral Diffie-Hellman key exchange |
| ECL-04 | All payloads must include a sender signature (AIM private key) to prevent spoofing |
| ECL-05 | API communications to external AI frontier model providers must use TLS 1.3 with certificate pinning |

## 5.3 Audit and Logging Engine (ALE)

| Requirement ID | Requirement |
| --- | --- |
| ALE-01 | Must log every inbound and outbound interaction: timestamp, identity hash, action type, outcome |
| ALE-02 | Must log every skill acquisition, skill build event, and skill use invocation |
| ALE-03 | Must log every handshake with any agent, regardless of protocol (GIAC-native, MCP, A2A) |
| ALE-04 | Must log every purchase or licensing transaction |
| ALE-05 | Logs must be cryptographically chained (hash of previous entry in each record) |
| ALE-06 | Log retention: 16 months for ALL agent types, mandatory |
| ALE-07 | For MCP and A2A handshakes: all parties must record the transaction within a ±500ms tolerance window referencing a common NTP/GPS time source. Drift beyond tolerance triggers a transaction review flag (not automatic rejection) pending owner review. |
| ALE-08 | Logs exportable in JSON-LD or CBOR format to authorized auditors |
| ALE-09 | Must expose authenticated read-only ALE endpoint on port :4402 |

## 5.4 Delegation and Authorization Engine (DAE)

| Requirement ID | Requirement |
| --- | --- |
| DAE-01 | Scoped permission model: each delegated action must specify resource, action type, and time-bound expiry |
| DAE-02 | Delegation tokens must be dual-signed by delegating and receiving agents |
| DAE-03 | Must support delegation chain traversal for authorization verification |
| DAE-04 | Sub-agents initiated by a P-Agent are controlled exclusively by that P-Agent. No external entity may direct, modify, or terminate a sub-agent without explicit P-Agent authorization. |
| DAE-05 | Same exclusive control principle applies to sub-agents of E-Agents and G-Agents |
| DAE-06 | Revocation propagates to all active sessions within 60 seconds |

## 5.5 Health and Status Beacon (HSB)

| Requirement ID | Requirement |
| --- | --- |
| HSB-01 | Must broadcast a signed health beacon at minimum every 60 seconds on port :4403 |
| HSB-02 | Beacon payload: agent ID hash, certificate validity status, operational status, software version hash, Health Certificate status |
| HSB-03 | Beacon must be signed with the agent's AIM private key |
| HSB-04 | Agent must enter restricted mode if Health Certificate lapses beyond the 30-day grace period |

## 5.6 Interoperability Gateway (IG)

| Requirement ID | Requirement |
| --- | --- |
| IG-01 | Must support MCP (Model Context Protocol) and A2A (Agent-to-Agent) as inbound/outbound formats |
| IG-02 | Must validate GIAC of any connecting agent before accepting inbound connection |
| IG-03 | Must enforce tier-appropriate interaction and consent rules |
| IG-04 | Must support rate limiting and circuit breaking per agent identity |
| IG-05 | All MCP and A2A sessions must produce synchronized transaction logs across all parties within the ±500ms tolerance window referencing a common time source |

## 5.7 Portable Memory Store (PMS)

The Portable Memory Store holds the agent's knowledge about its owner, learned context, preferences, and accumulated intelligence. It is fully owned by the agent owner and must be architecturally independent from the agent runtime.

| Requirement ID | Requirement |
| --- | --- |
| PMS-01 | The memory store MUST be architecturally decoupled from the agent runtime: migration to a different cloud provider or local machine must require no modification to agent behavior |
| PMS-02 | Memory is encrypted at rest using AES-256-GCM with a key derived from the owner's AIM private key. No cloud provider or third party can read the memory without the owner's key. |
| PMS-03 | Memory must be exportable in a standardized portable format (JSON-LD or encrypted binary bundle) at any time on owner request |
| PMS-04 | Memory migration must complete with full integrity verification via SHA-3-256 hash comparison of exported and imported bundles |
| PMS-05 | Memory store must maintain a versioned changelog so the owner can audit what the agent has learned and when |
| PMS-06 | No third party — including AI model providers and cloud hosts — may access, train on, or replicate the agent's memory without explicit, revocable owner consent encoded as a signed DAE token |

### Portability Guarantee

An OSARA-compliant P-Agent must be runnable on the owner's local machine, any OSARA-compatible PaaS provider, or a Community Agent Host — and migrated between them with zero loss of identity, memory, or skills. Agent behavior must be identical regardless of where it runs.

## 5.8 Physical Owner Authorization Module (POA)

Defined in Section 4.2. The POA module is a mandatory tamper-proof component in every agent of all tiers. It gates all inspection access and administrative actions behind real-time physical authorization by the owner, using either biometric verification or a hardware security token.

## 6. Skill Integrity, Ownership, and Portability

Skills are the functional capabilities an agent acquires, builds, or is licensed to use. OSARA treats skills as first-class assets with cryptographic identity, ownership attribution, and tamper-evident signatures.

## 6.1 Skill Signature and Binding

| Requirement ID | Requirement |
| --- | --- |
| SKL-01 | Every skill acquired by an agent must be signed by the acquiring agent's AIM private key at the moment of acquisition. This signature is the record of ownership within the OSARA ecosystem. |
| SKL-02 | The agent's signature is permanently embedded in the skill's metadata header. A skill signed by Agent A cannot be silently executed by Agent B — the signature mismatch causes execution to abort unless an explicit transfer grant exists (see SKL-07). |
| SKL-03 | Skills developed through the agent are attributed to the owner for traceability and licensing purposes within the OSARA ecosystem. Intellectual property rights over agent-assisted outputs are governed by applicable national law and are not determined by this specification. |
| SKL-04 | Every skill invocation must be logged in the ALE with: skill ID, invocation timestamp, calling agent identity hash, and outcome |
| SKL-05 | If an external agent attempts to execute a skill without authorization, the attempt must be rejected and logged in the ALE of the rejecting agent |
| SKL-06 | Skill signatures must be verifiable by any party holding the owning agent's public key |
| SKL-07 | An owner may explicitly grant execution rights for a signed skill to another agent via a signed DAE delegation token specifying: recipient agent ID, permitted invocation scope, and expiry. This enables legitimate skill sharing, licensing, and collaboration without silent copying. |

### On Skill Ownership and Law

OSARA's skill signature mechanism establishes attribution and traceability within the ecosystem. It does not constitute a legal IP ownership declaration. Intellectual property rights over AI-assisted outputs vary by jurisdiction and are determined by applicable national and international law. Owners should seek legal advice in their jurisdiction regarding IP rights over agent-developed outputs.

## 6.2 Skill Inventory

Every OSARA agent must maintain a Skill Inventory (SI) — a structured, readable, and verifiable catalog of all skills the agent holds.

| Requirement ID | Requirement |
| --- | --- |
| SI-01 | The Skill Inventory must be machine-readable (JSON-LD format) and human-readable (rendered summary available on request) |
| SI-02 | Each skill entry must contain: Skill ID, name, version, acquisition date, acquisition method (built/purchased/licensed), owner signature hash, attribution record, license reference (if applicable), and current status |
| SI-03 | The Skill Inventory as a whole must be cryptographically signed by the agent, enabling third parties to verify its integrity and completeness |
| SI-04 | Skills built by the agent are marked as 'Owner Attribution' in the inventory. Skills licensed from external sources must reference the license identifier and expiry. |
| SI-05 | The Skill Inventory is accessible to authorized auditors via a dedicated endpoint during POA-authorized inspection sessions only |

## 6.3 Skill Catalog and Public Services

Each agent type must publish a Skill Catalog describing its available skills, public services, and any required skills that interacting agents must possess to access those services.

| Catalog Type | Requirement |
| --- | --- |
| E-Agent Skill Catalog | Lists: available public services, required P-Agent skills to access each service, and downloadable signed skill files that P-Agents can inspect and install to gain compatibility |
| P-Agent Skill Catalog | Lists the agent's available skills so E-Agents and G-Agents can verify compatibility before initiating a service interaction |
| G-Agent Skill Catalog | Lists government services available, required agent skills for access, and any government-certified skill packages available for download |
| Signed Skill Files | Downloadable skill files must be signed by the publishing agent's AIM key. Installing agents must verify the signature before execution. Signature failure blocks installation. |
| Skill File Inspection | Any agent may inspect a downloaded skill file's signature, attribution record, and permission requirements before installation. Installation is a deliberate, logged owner action. |

## 7. Hosting, Portability, and AI Model Policy

## 7.1 Hosting Modality Rules

| Hosting Rule | Requirement |
| --- | --- |
| P-Agent — PaaS or Local Only | A P-Agent may ONLY be hosted in Platform-as-a-Service (PaaS) modality, locally on the owner's own hardware, or on a certified Community Agent Host. SaaS hosting of a P-Agent is prohibited. The agent's data, health, and updates are the sole responsibility of the owner. |
| Community Agent Host | A non-profit or cooperative PaaS provider, OSARA-certified, that individuals may use when they lack the technical infrastructure to self-host. The Community Agent Host is contractually prohibited from accessing agent data, memory, or skills. It provides infrastructure only. |
| E-Agent — PaaS or Dedicated | E-Agents may run on PaaS, dedicated cloud, or on-premises. SaaS hosting is not permitted for the agent core. Supporting microservices may use SaaS where they do not touch agent identity or memory. |
| G-Agent — Sovereign Infrastructure | G-Agents must run on government-sovereign or government-approved infrastructure. Cross-border hosting requires bilateral treaty agreement. |
| Cloud Provider Requirements | Cloud providers hosting OSARA agents must be OSARA-Infrastructure Certified. They may not access, read, train on, or replicate agent memory or skills without explicit signed owner consent. |
| Local Execution | Every OSARA agent must be executable on a local machine without any cloud dependency, using a local open source AI model. Cloud connectivity is optional. |

## 7.2 AI Model Policy

| Policy Area | Requirement |
| --- | --- |
| Model Freedom | An OSARA agent may be powered by any combination of: frontier AI models via secure API, locally hosted open source models, or hybrid combinations of both. No model type is mandated. |
| API Security | All communications to external AI model APIs must use TLS 1.3 with certificate pinning. The model provider may not receive the agent's raw memory or skill inventory without explicit signed owner consent. |
| Local Model Support | Every OSARA agent must be capable of operating in a local-model-only mode with full structural functionality (reduced capability is acceptable, zero functionality is not) |
| Model Logging | Every invocation of an AI model must be logged in the ALE with: model identifier, invocation timestamp, and token count. Message content is NOT logged. |
| No Model Lock-in | The agent must not be architecturally locked to a single AI model provider. Switching models must not require re-certification or loss of identity, memory, or skills. |

## 7.3 Sub-Agent Control

Any sub-agent initiated by a P-Agent, E-Agent, or G-Agent is exclusively controlled by the initiating agent and its owner. This principle cannot be overridden by any third party.

| Rule | Requirement |
| --- | --- |
| Exclusive Control | No external entity — including cloud providers, AI model providers, or government bodies — may direct, modify, or terminate a sub-agent without explicit initiating agent authorization |
| Sub-Agent Identity | Sub-agents hold their own GIAC, sponsored by the initiating agent and co-signed by the GCA |
| Sub-Agent Logging | All sub-agent activity is logged in both the initiating agent's ALE and the sub-agent's own ALE |
| Sub-Agent Termination | Only the initiating agent (and its owner) may terminate a sub-agent. Unauthorized termination attempts must be logged and reported to the owner |

## 8. Annual Health Certificate and Digital Inspection Card

Every OSARA agent must hold a valid Annual Health Certificate (AHC) — a digitally signed operational clearance issued by a certified inspection entity. An agent without a valid AHC must enter restricted mode after a 30-day grace period. Inspection entities may be government bodies or accredited private sector organizations — both are fully equal pathways.

Protection Against Misuse
No government entity may deny, revoke, or withhold a Health Certificate on any grounds other than demonstrable technical non-compliance with the OSARA specification. Health Certificates are a technical compliance instrument, not a tool of political, regulatory, or discretionary control. Appeals against improper denial are governed by the OSARA Appeals Process administered by Open Source United.

## 8.1 Health Certificate Requirements

| Requirement ID | Requirement |
| --- | --- |
| AHC-01 | Must be renewed annually. Expiry triggers restricted mode after a 30-day grace period. |
| AHC-02 | May be issued by EITHER: (a) a government-certified inspection body, OR (b) an accredited private sector inspection authority recognized in the OSARA Inspection Entity Registry (IER). Both pathways are fully equal. |
| AHC-03 | The AHC is a digitally signed document embedding: agent ID hash, inspection date, inspector entity ID, inspection scope, pass/fail result, and expiry date |
| AHC-04 | The AHC is uploaded to the agent's AIM module and broadcast in the HSB health beacon |
| AHC-05 | The AHC is publicly verifiable by any party using the inspecting entity's public key |
| AHC-06 | The list of certified inspection entities is maintained in the OSARA Inspection Entity Registry (IER) by Open Source United |

## 8.2 Inspection Process

For a Health Certificate to be issued, the inspection entity must connect to the agent's Inspection Clearance Endpoint (ICE) via a POA-authorized session opened by the owner in real time. The owner must be physically present and authorize the connection.

Owner schedules an inspection with a certified inspection entity (government or accredited private sector)

Inspection entity presents its own valid GIAC and OAB credentials to the owner for verification

Owner physically authorizes the ICE connection using their chosen POA method (biometric or hardware token) in real time

A time-limited, tamper-evident inspection session is opened on port :4406

Inspector runs the OSARA Automated Conformance Test Suite (ACTS) against the agent

Inspector reviews: Skill Inventory, ALE log integrity, Health Beacon, encryption compliance, PMS portability

Inspector issues a signed Annual Health Certificate and uploads it to the agent's AIM

AHC is published to the OSARA Public Certificate Ledger (PCL)

## 9. Encryption Standards

| Component | Standard | Purpose |
| --- | --- | --- |
| Key Pairs | Ed25519 (preferred) or RSA-4096 | AIM identity signing, skill signatures |
| Transport | TLS 1.3 | All agent-to-agent and agent-to-service communication |
| Payload Encryption | AES-256-GCM | Message body within double-envelope; memory at rest |
| Key Exchange | ECDH with X25519 | Ephemeral session key establishment (PFS) |
| Hashing | SHA-3-256 or BLAKE3 | Audit log chaining, identity anchor hashing, certificate fingerprints |
| Certificate Format | X.509 v3 with OSARA extensions | GIAC and Annual Health Certificates |
| Token Format | JWT (signed) or CBOR Web Token | Delegation and authorization tokens |
| Skill Signatures | Ed25519 over skill binary + metadata | Embedded skill attribution proof |
| Memory Encryption | AES-256-GCM, key from owner AIM | Portable Memory Store at rest |
| Time Synchronization | NTP stratum 1 or GPS time source | ALE timestamp alignment (±500ms tolerance) |

Post-Quantum Roadmap
OSARA v0.3 mandates classical encryption. OSARA v1.0 (target 2027) will require CRYSTALS-Kyber (key encapsulation) and CRYSTALS-Dilithium (signatures) per NIST PQC standards. A 12-month migration overlap will be provided.

## 10. Government-Issued Agent Certificate (GIAC)

Every agent must hold a valid GIAC. The GIAC binds the agent's cryptographic identity to a government-verified owner identity anchor and defines the agent's permitted operational scope.

## 10.1 GIAC X.509 Mandatory Extensions

| Extension Field | Description |
| --- | --- |
| osara.tier | Agent tier: P (Personal), E (Enterprise), or G (Government) |
| osara.identityAnchorHash | SHA-3-256 hash of the owner's jurisdiction-defined identity credential + government-issued salt |
| osara.jurisdiction | ISO 3166-1 alpha-2 country code of issuing government authority |
| osara.scope | Permitted action categories (comma-separated) |
| osara.ownerDID | Decentralized Identifier (DID) of the legal owner |
| osara.auditEndpoint | URL of the agent's authenticated ALE endpoint |
| osara.healthEndpoint | URL of the agent's Health Beacon endpoint |
| osara.inspectionEndpoint | URL of the agent's ICE (POA-gated, closed by default) |
| osara.healthCertStatus | Current Annual Health Certificate status and expiry |
| osara.schemaVersion | OSARA schema version |

## 10.2 Certificate Validity and Revocation

| Certificate Type | Policy |
| --- | --- |
| P-Agent GIAC | Maximum 12 months. Must renew 30 days before expiry. |
| E-Agent GIAC | Maximum 24 months. Must renew 60 days before expiry. |
| G-Agent GIAC | Maximum 36 months. Renewal via inter-governmental agreement. |
| Standard Revocation | Published to CRL within 1 hour. |
| Emergency Revocation | Effective within 5 minutes via the OSARA Emergency Revocation Protocol (ERP). Emergency revocation may only be issued for demonstrable security breaches, not policy or political disagreement. |

## 11. Mandatory Port Specifications

| Port | Name | Security Requirement |
| --- | --- | --- |
| 4400/TCP | AIM Identity Port | Read-only. Serves GIAC and public key. TLS required. |
| 4401/TCP | Interoperability Gateway | Agent-to-agent messaging. TLS 1.3 + mutual GIAC auth. |
| 4402/TCP | Audit Log Port | Authenticated read-only. Authorized auditors with valid delegation token only. |
| 4403/UDP | Health Beacon Port | Outbound broadcast. Signed beacon with AHC status every 60s minimum. |
| 4404/TCP | Delegation Token Exchange | DAE token issuance and validation. Mutual TLS required. |
| 4405/TCP | Administrative Port | Localhost only (127.0.0.1). Never exposed externally under any circumstances. |
| 4406/TCP | Inspection Clearance Endpoint | POA-gated. Closed by default. Opens only on real-time owner physical authorization. Inspector access for AHC issuance only. |

Firewall Requirement
Ports 4400–4406 are the only permitted externally exposed ports. Port 4405 must never leave localhost. Port 4406 must remain closed at all times except during an active, owner-authorized inspection session.

## 12. Cross-Tier Interaction Rules

| Interaction | Status | Conditions |
| --- | --- | --- |
| P-Agent → E-Agent | Allowed | P-Agent initiates. E-Agent must present valid OSARA-S badge and Skill Catalog. Consent token required for data access. |
| E-Agent → P-Agent | Conditional | E-Agent must hold a P-Agent consent token. Unsolicited contact is prohibited. |
| P-Agent → G-Agent | Not Permitted Directly | P-Agents access government services via E-Agent intermediaries or designated G-Agent public endpoints only. |
| E-Agent → G-Agent | Allowed under license | E-Agent must hold a G-Agent Interaction License in its GIAC scope. All interactions logged both sides. |
| G-Agent → E-Agent | Allowed | Permitted for regulatory, audit, or service delivery. Must be logged. |
| G-Agent → G-Agent | Allowed under treaty | Requires bilateral OSARA treaty encoded in both GIACs. |
| MCP/A2A Sessions | Allowed (all tiers) | GIAC validation required before any MCP or A2A session. All parties must produce synchronized ALE entries within the ±500ms tolerance window. |

## 13. OSARA Compliance Badge and Certification

## 13.1 Badge Tiers

| Badge Level | Requirements |
| --- | --- |
| OSARA-C (Conformant) | Passes automated port and component verification. Minimum for ecosystem participation. |
| OSARA-A (Audited) | Passes OSARA-C plus manual audit of encryption, key storage, memory portability, skill inventory integrity, and POA module. |
| OSARA-S (Sovereign) | Passes OSARA-A plus government identity verification and full GIAC issuance. Required for cross-tier G-Agent interactions. |

## 13.2 Certification Process

Developer submits an OSARA Certification Application to an accredited OAB

OAB runs the OSARA Automated Conformance Test Suite (ACTS) against all mandatory ports

For OSARA-A or OSARA-S: owner physically authorizes a POA inspection session on port :4406

OAB auditor reviews: encryption implementation, key storage, ALE integrity, PMS portability, Skill Inventory, POA module

For OSARA-S: OAB coordinates GIAC issuance with the relevant government Registration Authority

OAB issues a signed Compliance Attestation Document (CAD)

Badge credential (JSON-LD Verifiable Credential) published to the OSARA Public Badge Registry (PBR)

Badge valid 12 months. Must be renewed annually alongside the Annual Health Certificate.

## 14. Governance and Versioning

| Governance Area | Policy |
| --- | --- |
| Specification Owner | Open Source United — a Community of Practice of the United Nations |
| Governing Body | OSARA Steering Committee (OSC) — open multi-stakeholder membership under Open Source United charter |
| Change Process | Public RFCs. 60-day public comment period. Supermajority OSC vote required for changes to mandatory requirements. |
| Version Cadence | Minor (0.x): every 6 months. Major (x.0): every 2 years. |
| Backward Compatibility | Minor versions backward compatible. Major versions allow breaking changes with a 12-month migration period. |
| Reference Implementation | Open source reference agent maintained under Open Source United's OSARA GitHub organization. Apache 2.0 licensed. |
| Inspection Entity Registry | Maintained by Open Source United. Lists all government-certified and privately accredited inspection bodies authorized to issue Annual Health Certificates. |
| Appeals Process | Disputes over certificate denial, badge revocation, or inspection conduct are handled by the OSARA Appeals Board under Open Source United, with final arbitration by the OSC. |

## 15. Glossary

| Term | Definition |
| --- | --- |
| AHC | Annual Health Certificate — mandatory yearly operational clearance for all agents |
| AIM | Agent Identity Module |
| ALE | Audit and Logging Engine |
| ACTS | Automated Conformance Test Suite |
| CAH | Community Agent Host — OSARA-certified non-profit PaaS provider for individuals |
| CAD | Compliance Attestation Document |
| DAE | Delegation and Authorization Engine |
| E-Agent | Enterprise Agent |
| ECL | Encrypted Communication Layer |
| G-Agent | Government Agent |
| GCA | Government Certificate Authority |
| GIAC | Government-Issued Agent Certificate |
| GTF | Government Trust Framework |
| HSB | Health and Status Beacon |
| ICE | Inspection Clearance Endpoint — POA-gated inspection port :4406 |
| IER | Inspection Entity Registry — maintained by Open Source United |
| IG | Interoperability Gateway |
| OAB | OSARA Audit Body |
| OSC | OSARA Steering Committee |
| OSU | Open Source United — specification owner |
| P-Agent | Personal Agent |
| PBR | Public Badge Registry |
| PCL | Public Certificate Ledger |
| PMS | Portable Memory Store |
| POA | Physical Owner Authorization module |
| SI | Skill Inventory |

## 16. Acknowledgements

OSARA was conceived and principally authored by the founder of Open Source United, whose vision for sovereign, interoperable, and human-centered AI agent infrastructure formed the intellectual foundation of this specification.

The specification has been developed under the governance of Open Source United, a Community of Practice of the United Nations, and reflects input from the global open source, privacy, and digital identity communities.

### Contributing

OSARA is a living specification. Contributions, corrections, and proposals are welcome via public RFC on the OSARA Gitlab repository opensource.unicc.org maintained by Open Source United. All contributors are acknowledged in the repository changelog.

OSARA v0.3 — Copyright © 2026 Open Source United — CC BY 4.0 — March 2026
