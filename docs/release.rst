Release Process
===============

Semantic-release automates:

- Version bump (from `src/playground/__init__.py`)
- Changelog update (`CHANGELOG.md`)
- Git tag & GitHub Release

Dry-run locally:

.. code-block:: bash

   semantic-release --noop version

.. mermaid::

   sequenceDiagram
     participant Dev as Developer
     participant GH as GitHub
     participant CI as CI Runner
     participant SR as semantic-release

     Dev->>GH: Push commits (Conventional Commits)
     GH->>CI: Trigger ci.yml (lint, test, docs)
     CI-->>Dev: Report status checks
     Dev->>GH: Merge PR to main
     GH->>CI: Trigger release.yml
     CI->>SR: semantic-release publish
     SR->>GH: Create tag & GitHub Release
