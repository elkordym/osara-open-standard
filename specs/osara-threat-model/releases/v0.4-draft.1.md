# OSARA — Threat Model

> An informative companion to the OSARA technical specification, enumerating the threats the specification is designed to mitigate, the residual risks it accepts, and the assumptions on which its guarantees rest.
>
> Published by **Open Source United**, a Community of Practice of the United Nations.
>
> **Version 0.4 — Draft for Public Comment — March 2026**
>
> Copyright © 2026 Open Source United — Released under CC BY 4.0 International License.

---

## Status of This Document

This is the current editable working draft of the **OSARA Threat Model**, version `v0.4-draft.1`. This document is **informative**. It contains no normative requirements; it explains why the normative requirements in the [OSARA Specification](../osara/current.md) exist and what they protect against.

- **Stable identifier**: `urn:osu:osara-threat-model:v0.4-draft.1`
- **Editor's draft**: this file (`specs/osara-threat-model/current.md`)
- **Immutable snapshot**: [`specs/osara-threat-model/releases/v0.4-draft.1.md`](releases/v0.4-draft.1.md)
- **Maturity level**: Informative

This is a living document. Threat models evolve as adversary capability evolves and as deployments reveal new attack surfaces. Updates will accompany each substantive revision of the OSARA Specification.

---

# 1. Scope and Method

This threat model covers the **agent runtime, the Owner Authorization Device (OAD), the audit chain, the certificate lifecycle, the migration protocol, the integrity measurement layer, and the inter-agent communication channel**. It does not attempt to model threats against the underlying AI models, against the user's general computing environment, or against systemic risks (e.g., mass unemployment) — those are addressed elsewhere.

We use the STRIDE taxonomy (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) augmented with two categories that matter specifically for agentic AI: **Sovereignty Loss** (control or instructions reaching the agent that bypass the owner) and **Coercion** (legitimate access to the owner used to force agent action against the owner's interest).

# 2. Assets the Standard Protects

The OSARA specification's security properties are designed to protect the following assets, in descending order of value:

| Rank | Asset | Why It Matters |
| --- | --- | --- |
| 1 | **GIAC private key** | Compromise allows complete impersonation of the agent (and by extension, of the owner) until revocation propagates. The key never leaves the OAD hardware. |
| 2 | **Audit log chain (ALE)** | Compromise destroys the legal evidence that an action was authorized. Chained logs make selective tampering detectable. |
| 3 | **Portable Memory Store (PMS)** | Contains accumulated knowledge of the owner. Disclosure is a privacy harm; loss is a sovereignty harm. |
| 4 | **Skills and skill signatures** | Skills are economic and operational capability. Forged signatures allow unauthorized capability transfer. |
| 5 | **Owner's identity anchor (raw form)** | Never stored — only the SHA-3-256 hash is. Disclosure of the raw value enables identity theft outside OSARA. |
| 6 | **Health certificate** | Falsified AHC could allow a non-compliant agent into the ecosystem. |
| 7 | **Health beacon (HSB) stream** | Used to advertise validity. Tampering enables denial-of-service against legitimate agents. |

# 3. Adversary Model

We assume adversaries can take any of the following forms, often simultaneously.

| Adversary | Capability | Example Goal |
| --- | --- | --- |
| **Curious cloud provider** | Full physical access to the host. Cannot read OAD hardware. Cannot read memory canaries without tripping IMA. | Read agent memory, train on user data, gain competitive intelligence. |
| **Malicious employer** | Legitimate scope of employment-level delegation. Can issue instructions to the employee. | Compel the agent to act against the owner's interest; harvest the agent's memory before separation. |
| **State adversary (foreign)** | Network-level interception. Cannot break TLS 1.3 within session lifetime. Can compel a foreign host. | Surveillance of cross-border interactions; identification of individuals across jurisdictions. |
| **State adversary (domestic, abusive)** | Legitimate court authority. Cannot extract OAD key without physical access. | Force log access or agent seizure without due process. |
| **Coerced owner** | Possesses OAD and can authenticate. May be acting under duress (extortion, abuse, kidnap). | Force the agent to act against owner's interest; force migration to attacker-controlled host. |
| **Compromised supply chain** | Can modify component binaries before deployment. | Insert backdoor that survives initial provisioning. |
| **Compromised CA** | Can issue forged GIACs. | Spoof legitimate agents; enable man-in-the-middle. |
| **Quantum-equipped adversary (future)** | Can break ECC and RSA in feasible time. Cannot break post-quantum primitives. | Decrypt historical traffic; forge classical signatures. |

# 4. Threats and Mitigations — by Component

## 4.1 Agent Identity Module (AIM) and GIAC

| Threat | OSARA Mitigation |
| --- | --- |
| **Spoofing**: attacker presents a forged certificate | All GIACs chain to a Government Certificate Authority. Verification against the PCL and CRL is mandatory before any session. |
| **Tampering**: attacker modifies the certificate in flight | X.509 v3 signature. Any modification breaks the signature. TLS 1.3 transport adds in-flight integrity. |
| **Key extraction**: attacker extracts the private key | The private key never leaves the OAD hardware secure element. Extraction requires defeating Tier A tamper-response (smart-card-grade or higher). |
| **CA compromise**: an issuing CA is breached | Standard revocation reaches all parties within 1 hour. Emergency Revocation Protocol acts within 5 minutes. Quantum-resistant CA roots roll over in v1.0. |
| **Replay**: attacker replays a captured certificate | Certificate validity windows are short (12 / 24 / 36 months). PCL/CRL checks must be live. Session establishment uses ephemeral key exchange (PFS). |

## 4.2 Owner Authorization Device (OAD)

| Threat | OSARA Mitigation |
| --- | --- |
| **Loss or theft of OAD** | OAD-06: owners must be able to register a secondary OAD in advance. Recovery via in-person re-provisioning at a government registration office. |
| **Coerced authentication** | High-stakes Tier 3 actions are restricted to Tier A hardware. Some jurisdictions may add additional out-of-band confirmation for irreversible actions. Mitigation is inherently partial — see §6. |
| **Cloned OAD** | Hardware secure element key extraction is the only way to clone. Tier A cryptographic key isolation makes this infeasible without physical destruction of the chip. |
| **Compromised OAD firmware** | OAD firmware is open source and reproducible. Tampering must be detected by the OAD vendor's secure update path. Compromise of an entire OAD vendor is an unmitigated systemic risk. |
| **Side-channel attack on OAD** | Hardware secure elements implement timing-channel and power-analysis countermeasures per the OAD certification standard. |

## 4.3 Audit and Logging Engine (ALE)

| Threat | OSARA Mitigation |
| --- | --- |
| **Selective entry deletion** | Each entry contains the hash of the prior entry. Any deletion breaks the chain and is detected on every IMA heartbeat (every 30 s). |
| **Backdated entries** | Entries carry an NTP/GPS-anchored timestamp. Drift beyond ±500 ms triggers a transaction review flag. |
| **Forged entries** | Each entry is signed at write time. The signature anchors to the agent's identity. |
| **Log destruction by host** | The host can destroy the log, but the destruction is itself detectable on the next inspection because the chain genesis hash is publicly registered. |

## 4.4 Encrypted Communication Layer (ECL)

| Threat | OSARA Mitigation |
| --- | --- |
| **Eavesdropping** | TLS 1.3 with Perfect Forward Secrecy. Compromise of a long-term key does not decrypt prior sessions. |
| **Man-in-the-middle** | Mutual TLS using GIAC client certificates. Certificate pinning required for model API calls. |
| **Sender repudiation** | Every payload is signed with the sender's AIM key (via OAD remote signing). |
| **Replay** | Session-bound nonces. Ephemeral session keys. |
| **Post-quantum threat** | v1.0 mandates CRYSTALS-Kyber + CRYSTALS-Dilithium. Historical session traffic captured today is at risk; PFS limits exposure to per-session keys, not long-term identity keys. |

## 4.5 Portable Memory Store (PMS)

| Threat | OSARA Mitigation |
| --- | --- |
| **Host reads memory** | Memory is encrypted at rest with AES-256-GCM under a key derived from the OAD private key. The host has no path to the plaintext. |
| **Host trains AI on memory** | Same mitigation. Additionally, the cloud provider must be OSARA-Infrastructure Certified and contractually prohibited from training. |
| **Modification at rest** | AES-256-GCM is authenticated encryption. Any modification produces an authentication failure on next read. |
| **Lock-in (export refusal)** | PMS-03: owner-initiated export must complete in JSON-LD or encrypted binary bundle. AI Bill of Rights §4.2 obliges providers to complete transfer in 30 days. |

## 4.6 Agent Migration and Integrity Protocol (MIP)

| Threat | OSARA Mitigation |
| --- | --- |
| **Source-side tamper before export** | MIG-05: owner signs the container hash on their OAD. Any source-side modification after signing is detected on import (MIG-08). |
| **Network corruption / modification** | Manifest hash detects any change. The destination must verify before any further action. |
| **Destination-side tamper before run** | MIG-07/08/09/10 all run before the agent starts. The agent only resumes if every check passes. |
| **Manifest replay** | Each manifest is bound to a specific destination identifier. |

## 4.7 Integrity Measurement Architecture (IMA) and Lock State Protocol (LSP)

| Threat | OSARA Mitigation |
| --- | --- |
| **Boot-time tampering** | Secure Boot chain; TPM 2.0 sealed reference hashes. Any pre-boot modification prevents startup. |
| **Runtime component substitution** | 30-second heartbeat re-hashes all mandatory components against TPM-sealed values. ORANGE lock state on mismatch. |
| **Memory injection** | Memory canaries detect read or write to instrumented locations. ORANGE state on trip. |
| **ALE tamper** | Chain hash verified on every heartbeat. Broken chain → ORANGE. |
| **GIAC private-key extraction attempt** | RED state. Automatic forensic snapshot. Automatic competent-authority notification (limited per IRS to this case and two others). |

## 4.8 Skill Subsystem

| Threat | OSARA Mitigation |
| --- | --- |
| **Silent skill copy** | Skill metadata includes acquirer signature. A copied skill fails signature check on a different agent unless an explicit transfer grant (SKL-07) exists. |
| **Forged skill provenance** | Signatures are verifiable by any party. Skill catalogs are signed. |
| **Malicious skill execution** | Skills must be invoked through DAE-scoped delegation. ALE records every invocation. |

## 4.9 Inspection Clearance Endpoint (ICE) and Health Certificate

| Threat | OSARA Mitigation |
| --- | --- |
| **Remote inspection without owner consent** | ICE is closed by default. POA requires real-time physical owner authorization via OAD. POA-07: no remote override is permitted. |
| **Coerced inspection** | The inspection record itself preserves the OAD identity and the physical authorization method. Coerced inspections are post-hoc detectable but not pre-emptively preventable. |
| **Fraudulent AHC issuance** | AHC is signed by the inspecting entity. Inspecting entities are themselves registered in the IER and subject to substantiated-complaint records. |
| **Politically motivated AHC denial** | §8 Protection Against Misuse: denial is unlawful on any ground other than demonstrable technical non-compliance. Appeals via the competent national authority. |

# 5. Cross-Cutting Threats

## 5.1 Coerced Owner

This is the threat for which OSARA's mitigations are the weakest, by design — and necessarily so. An owner who possesses the OAD and can authenticate on it can authorize any action within their action tier. OSARA cannot distinguish a free-will authorization from a coerced one. Mitigations are partial:

- **Tier 3 (high-stakes) action gating**: forces a deliberate, recorded authorization event for the most consequential actions, including irreversible financial moves and legal signings. This creates a moment of friction and a recorded audit trail that downstream actors (banks, courts, regulators) can use.
- **Action authorization logging**: every Tier 2 and Tier 3 action records the OAD tier, the timestamp, and the action description. Patterns consistent with coercion (e.g., a long series of high-stakes actions outside normal hours) can be detected by downstream services.
- **Out-of-band confirmation (jurisdiction-defined)**: some national OSARA implementations may require a second-channel confirmation for certain action categories, beyond what the base specification mandates.

Eliminating coercion is a problem of physical safety and legal protection. The OSARA specification's role is to make the act of coercion visible after the fact and to provide cryptographic evidence for prosecution. This is consistent with the position taken by the financial sector and identity sector in general.

## 5.2 Supply-Chain Compromise

OSARA requires that all mandatory components be open source and reproducibly built. The reference hashes sealed in the TPM during IMA provisioning must be reproducible from the published source. This forces an attacker who wants to insert a backdoor to also corrupt the public release process — a much higher bar than corrupting a single binary distribution.

National OSARA implementations are expected to maintain an attestation registry of approved reproducible builds. Inspection entities verify against this registry as part of the IMA inspection scope.

## 5.3 Compromised Government Certificate Authority

A breached GCA can issue forged GIACs. Mitigations:

- **CRL within 1 hour, ERP within 5 minutes** for known compromises.
- **Cross-border G-Agent interactions require bilateral treaty validation** — a single breached CA does not unilaterally compromise cross-border trust.
- **Publicly auditable PCL**: anomalies in issuance volume are publicly detectable.
- **Open source CA reference implementation**: makes implementation flaws community-auditable rather than proprietary.

The OSARA specification does **not** assume any single GCA is trustworthy. It assumes the federation of GCAs collectively maintains integrity through revocation, audit, and treaty.

## 5.4 Post-Quantum Transition

A sufficiently capable quantum adversary breaks ECC (X25519, Ed25519) and RSA. OSARA v0.4 mandates classical primitives. OSARA v1.0 (target 2027) will require:

- **CRYSTALS-Kyber** for key encapsulation.
- **CRYSTALS-Dilithium** for signatures.

The 12-month overlap period in v1.0 allows agents to hold both classical and PQ keys. Historical traffic captured before the transition remains at risk; Perfect Forward Secrecy in ECL limits exposure to short-lived session keys, but long-term identity keys (GIAC) become breakable retrospectively. Owners who require long-term confidentiality should re-provision PQ GIACs as soon as v1.0 is available.

## 5.5 Cross-Jurisdiction Conflict

Where the owner's jurisdiction and the host's jurisdiction conflict — for example, a local law that compels the host to provide access in violation of the owner's rights — OSARA's technical mechanisms (OAD-isolated keys, encrypted PMS, sealed ALE) maintain confidentiality and integrity against the host. The host cannot comply with such an order because it does not hold the keys. Legal conflict is then resolved at the diplomatic and treaty level, not the technical level. The agent simply cannot be made to act against its owner.

# 6. Residual Risks Accepted by the Specification

OSARA explicitly does not mitigate:

- **Owner-level coercion** beyond the partial measures in §5.1.
- **Loss of OAD with no registered secondary** — recovery requires physical re-provisioning, and the agent is unavailable during that window.
- **Catastrophic failure of an OAD vendor's update infrastructure** affecting an entire vendor's installed base.
- **Future cryptanalytic breakthroughs against AES-256, SHA-3, or post-quantum primitives** beyond what the published research base predicts.
- **Adversaries with sustained physical access to a Tier A hardware secure element and unlimited budget** — only commercially feasible attacks are within the model.
- **Risks arising from the underlying AI model**, including model-level prompt injection, training data poisoning, and emergent behaviour. These are addressed in the AI model's own governance, not in OSARA.

Accepting these residual risks is part of how the specification stays implementable. They are documented so that adopters, regulators, and inspectors can make informed decisions about additional jurisdiction- or sector-specific mitigations.

# 7. Open Threat Modelling Questions

These are explicitly open and tracked for community input as part of the v0.4 public comment period:

1. **Multi-OAD M-of-N for high-stakes individual actions** — is it desirable, or does it create a worse user-experience trade-off?
2. **Cooperative coercion detection** between an owner's OAD and their bank / law-enforcement out-of-band channel — feasible and acceptable, or an unacceptable surveillance vector?
3. **Threat from OAD vendor consolidation** — if 3 vendors hold 90 % of OADs globally, do they become a systemic-risk concentration point requiring regulation similar to systemically important financial institutions?
4. **Time-locked actions** — should some action categories (e.g., transfers above a threshold) be subject to a mandatory delay during which the owner can revoke via OAD?
5. **Sovereign cloud guarantees** — what cryptographic constructions are sufficient to assure a state that an OSARA agent it hosts on cloud cannot leak information to the cloud provider's home jurisdiction?

Comments on any of these are welcome via the public RFC process.

---

*OSARA Threat Model v0.4-draft.1 — Copyright © 2026 Open Source United — CC BY 4.0 — March 2026*
