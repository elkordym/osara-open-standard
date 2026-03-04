# Branching Strategy

## Branch Roles

- `main`: stable published baseline and tagged releases only
- `prerelease`: integration/staging branch for approved pull requests
- `feature/*`: short-lived working branches

## Default Flow

1. Create `feature/*` from `prerelease`.
2. Open PR from `feature/*` -> `prerelease`.
3. Validate and merge into `prerelease`.
4. Cut a release PR from `prerelease` -> `main`.
5. Tag and publish release from `main`.

## Why this model

This keeps `main` clean and release-focused while allowing active drafting and companion-document updates in `prerelease`.
