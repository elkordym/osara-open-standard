# Release Process

## Release Types

- **Draft release**: public working text (`vX.Y-draft.N`)
- **Release candidate**: stabilization (`vX.Y-rc.N`)
- **Stable release**: normative baseline (`vX.Y`)

## Steps

1. Freeze target milestone issues.
2. Update spec files in `specs/` and changelog.
3. Create a release pull request.
4. Merge pull requests into `prerelease`.
5. Create release PR from `prerelease` to `main`.
6. Run review and final approval on the release PR.
7. Tag and publish GitHub release from `main`.

## Required Artifacts

- Updated markdown in `specs/`
- Changelog entry
- Decision records for significant normative changes
- Public release notes
