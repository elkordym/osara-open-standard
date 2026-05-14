# Contributing Guide

## Ways to Contribute

- Open an issue for bugs, ambiguities, or conflicts in text
- Propose normative or editorial pull requests
- Participate in public consultation rounds
- Submit implementation feedback from pilots

## Contribution Rules

- Keep proposed changes focused and scoped
- Distinguish normative text from explanatory text
- Include rationale for any requirement change (`MUST`, `SHALL`, etc.)
- For rights changes, include legal and technical impact notes

## Pull Request Checklist

- [ ] Clear problem statement
- [ ] Proposed text changes are explicit
- [ ] Compatibility impact explained
- [ ] References to related sections included
- [ ] Changelog entry added if applicable

## Commit Message Convention

Use one of:

- `docs:` documentation-only updates
- `spec:` normative standard changes
- `governance:` governance/process changes
- `chore:` repository maintenance

## Branch and PR Targeting

- Open feature branches from `prerelease`.
- Target all normal pull requests to `prerelease`.
- Only release PRs should target `main`.

## Public Comment Workflow

1. Label issue as `public-comment`
2. Keep issue open for the announced window
3. Summarize accepted/rejected points at closure
4. Link decisions to pull requests and release notes

## Local Documentation Build (Contributors Only)

If you are editing specification or governance text and want to preview the rendered site before opening a pull request, follow the instructions in [`docs/SITE_BUILD.md`](../docs/SITE_BUILD.md) (contributor-only build notes).
