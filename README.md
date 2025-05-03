# Python Starter Template

[![CI](https://github.com/michdo/python-starter-template/actions/workflows/ci.yml/badge.svg)](https://github.com/michdo/python-starter-template/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-python--starter--template-blue)](https://michdo.github.io/python-starter-template/)

A ready-to-use Python project template with DevContainer setup, GitHub integration, and modern tooling.

## Features

- 📦 **uv** for fast dependency management
- 🧹 **ruff** for code linting
- 🧪 **pytest** for testing
- 📚 **Sphinx** with **Mermaid** diagrams for documentation
- ⚙️ **VSCode DevContainer** ready
- 📝 **Pre-configured GitHub repository**

## Requirements

- Docker
- VSCode with Dev Containers extension
- Git

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-starter-template.git
   cd python-starter-template

## How Releases Work

1. Merge your PRs to main using Conventional Commits.
2. On each push to main, CI’s Release workflow runs semantic-release:
   - It bumps __version__ in your package
   - It updates CHANGELOG.md
   - It tags the repo and creates a GitHub Release

3. You don’t need to manually tag or draft releases—just push commits.

# Scaffold a new project
   ```bash
   pip install cookiecutter           # if you don’t have it
   cookiecutter https://github.com/michdo/python-starter-template
