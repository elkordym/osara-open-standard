# OSARA Open Standard Repository

This repository manages the public draft lifecycle for:

- `specs/osara/current.md`
- `specs/ai-bill-of-rights/current.md`

The goal is to run this as an open, transparent, community-driven standard project with clear governance, versioning, public consultation, and reproducible publication to the web.

## Vision

We believe the next era of AI must belong to people, not platforms. OSARA and the AI Bill of Rights together define a future where every individual, enterprise, and government can operate trusted AI agents that are sovereign, portable, interoperable, and accountable by design.

Our vision is to make this the global open standard for human-centered AI: a world where innovation moves fast without sacrificing dignity, privacy, labor rights, safety, or democratic control. We are building the technical and governance foundation for an AI ecosystem that is open, auditable, and fair for everyone.

This is bigger than software. It is a shared mission to ensure AI amplifies human freedom and human potential at planetary scale.

The time to define these rules is now, before private-sector defaults become the global rules of the game for everyone. Your help, contributions, and participation directly accelerate adoption of this open standard. The faster OSARA and the AI Bill of Rights are adopted, the stronger the expectation and obligation for major platforms and providers to comply with these principles.

## Leadership

- **Primary Author / Lead Maintainer**: `@elkordym`
- **Chair, Open Source United (UN Open Source Community of Practice)**: `@elkordym`
- **Future contributors**: Open Source United community members (see `AUTHORS.md`)

## Documentation Website

- Source branch for publishing: `main`
- Auto-deploy workflow: `.github/workflows/pages.yml`
- Expected URL: [https://elkordym.github.io/osara-open-standard](https://elkordym.github.io/osara-open-standard)
- Spec source of truth: `specs/` (synced into `docs/specs/` during docs build)

## Repository Structure

- `specs/` canonical draft texts and released versions
- `governance/` charter, decision records, and policy docs
- `community/` participation guidance, issue templates, and discussion rules
- `docs/` website content (overview, roadmap, process pages)
- `website/` static site and publishing configuration
- `.github/` GitHub automation templates and workflows

## Current Drafts

- OSARA current draft (`specs/osara/current.md`)
- AI Bill of Rights current draft (`specs/ai-bill-of-rights/current.md`)

## Project Principles

- Open standards process
- Open participation with clear moderation
- Traceable change history
- Publicly documented decisions
- Neutral, vendor-independent governance

## Branching Model

- `main`: stable, release-only branch
- `prerelease`: integration/staging branch for all merged pull requests
- Feature branches: short-lived branches that target `prerelease`

Release flow: feature branch -> `prerelease` -> release PR to `main`.
