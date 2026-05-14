# Getting Started

This page tells you which document to read first, depending on what you want to do.

## For Readers New to OSARA

1. Read [`specs/osara-overview/current.md`](specs/osara-overview/current.md) — short, non-normative overview of the OSARA Standards Family.
2. Read [`specs/ai-bill-of-rights/current.md`](specs/ai-bill-of-rights/current.md) — the rights framework.
3. Skim [`specs/osara/current.md`](specs/osara/current.md) — the normative technical specification. The [Glossary §19](specs/osara/current.md#19-glossary) is a useful map of the standard's vocabulary.

## For Implementers

1. Read the [OSARA Specification](specs/osara/current.md) end-to-end. Pay special attention to:
    - §4.3 Owner Authorization Device (OAD) — the hardware-isolated key custody model.
    - §5 Mandatory Components — every component is required.
    - §9 Migration and Integrity Protocol — the cryptographic basis of portability.
    - §10–§12 Integrity Measurement Architecture, Lock State Protocol, Incident Reporting Specification — the agent's self-defense layer.
2. Treat **MUST**, **SHALL**, **REQUIRED**, **MUST NOT** statements as normative per [RFC 2119 / RFC 8174](https://www.rfc-editor.org/info/bcp14).
3. Treat explanatory passages and informative sections as context, not as conformance criteria.
4. Read the [Threat Model](specs/osara-threat-model/current.md) and [Privacy Considerations](specs/osara-privacy/current.md) to understand what your implementation is supposed to protect against and which residual risks the specification explicitly accepts.
5. When you have a working implementation, submit an [Implementation Report](governance/IMPLEMENTATION_REPORT_TEMPLATE.md).
6. Adopters of mandatory components must comply with the [IPR Policy](governance/IPR_POLICY.md) and the open source requirement in [AI Bill of Rights §4.7](specs/ai-bill-of-rights/current.md#article-iv-interoperability-portability-and-open-standards).

## For Auditors, Inspection Entities, and Regulators

1. Read the [OSARA Specification](specs/osara/current.md) (especially §8 Annual Health Certificate and §17 Compliance Badge and Certification).
2. Read the [Threat Model](specs/osara-threat-model/current.md) for the mitigation matrix and residual-risk register.
3. Read the [Privacy Considerations](specs/osara-privacy/current.md), especially §3 Data Flows and §4 Linkability.
4. Track Family-wide governance through the [Errata Register](errata.md), [Public Comments Register](comments-register.md), and [Liaisons](governance/LIAISONS.md).

## For Contributors

1. Read the [Contributing guide](community/CONTRIBUTING.md) and the [Code of Conduct](community/CODE_OF_CONDUCT.md).
2. Read the [IPR Policy](governance/IPR_POLICY.md) — every contribution accepts it.
3. Open an issue using the **Public Comment** or **Spec Change** template. Use the section/requirement ID you are commenting on (e.g., `OSARA §4.3 OAD-04`).
4. For substantive normative proposals, follow the public RFC process described in the [Release Process](RELEASE_PROCESS.md).

## For National Implementation Authorities

The OSARA Standards Family is published under CC BY 4.0 and is designed to be adapted into national implementations. The adaptation must credit Open Source United and may not introduce requirements that weaken the rights established in the AI Bill of Rights. National implementations define which government credentials qualify as identity anchors (OSARA §4.1), which body operates the GIAC Registration Authority (§4.5), and the competent authority for incident reports (§12). For coordination, see the [Liaisons register](governance/LIAISONS.md).
