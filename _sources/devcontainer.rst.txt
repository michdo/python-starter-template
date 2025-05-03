DevContainer
============

Our Dockerfile (in `.devcontainer/`) is based on the official Python 3.12 image.
It installs:

- `uv` for dependency management
- Node.js & commitlint (for pre-commit)
- All dev extras (`--group dev`)

**Extensions** auto-installed:

- ms-python.python
- msk-vscode-ruff
- Docker, GitLens, Jupyter, etc.

Customize in `.devcontainer/devcontainer.json`.
