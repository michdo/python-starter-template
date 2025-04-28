# Use the official devcontainers Python 3.12 image (includes Python and common tools)
FROM mcr.microsoft.com/devcontainers/python:3.12

# Switch to root to install global tools
USER root

# Install uv globally
RUN pip install --upgrade pip \
    && pip install uv

# Copy only pyproject.toml to leverage Docker caching
COPY pyproject.toml .

# Create a virtual environment manually
RUN uv venv .venv

# Install main and dev dependencies from pyproject.toml
RUN uv pip install -r pyproject.toml --group dev

# Switch back to non-root user
USER vscode
