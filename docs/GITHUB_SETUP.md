# GitHub Setup Guide

## 1) Create the GitHub repository

- Name suggestion: `osara-open-standard`
- Visibility: Public
- Do not initialize with README (you already have one locally)

## 2) Push local repository

```bash
git init
git checkout -b main
git add .
git commit -m "chore: bootstrap OSARA open standard repository"
git remote add origin https://github.com/<your-username>/osara-open-standard.git
git push -u origin main
git checkout -b prerelease
git push -u origin prerelease
```

## 3) Enable collaboration features

- Turn on **Issues**
- Turn on **Discussions**
- Add labels: `spec-change`, `public-comment`, `governance`, `release`
- Protect `main` branch with PR-required merges
- Protect `prerelease` branch with PR-required merges
- Set pull requests to target `prerelease` by default

## 4) Publish documentation site

Two options:

- **Simple**: use GitHub Actions workflow in `.github/workflows/docs.yml` (already included)
- **Advanced**: use Material theme and deploy to GitHub Pages

## 5) Release process

- Create milestones by draft/release target
- Tag versions like `v0.3-draft.1`, `v0.4-rc.1`, `v1.0`
- Publish release notes with key normative changes
- Promote by release PR from `prerelease` -> `main`
