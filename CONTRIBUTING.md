# Contributing

## Release Process

We use [python-semantic-release] to automate version bumps, changelog generation, Git tagging,
and GitHub Release creation on every push to `main`. To contribute:

1. **Follow Conventional Commits**
   Commit messages must start with one of: `feat:`, `fix:`, `chore:`, `docs:`, etc.

2. **Open a PR**
   Target the `main` branch. Ensure all CI checks pass and you have at least one approving review.

3. **Merging to Main**
   Once merged, the **Release** workflow will:
   - Determine next version from your commit messages
   - Update the `__version__` variable in `src/playground/__init__.py`
   - Append release notes under the new version in `CHANGELOG.md`
   - Create a Git tag `vX.Y.Z`
   - Draft a GitHub Release

4. **Local testing**
   You can preview the next version locally (no changes pushed) with:

   ```bash
   semantic-release --noop version
