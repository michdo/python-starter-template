Continuous Integration
======================

There are three workflows under `.github/workflows/`:

1. **ci.yml**
   - Lint with `ruff`
   - Run `pytest`
   - Build & upload docs
2. **release.yml**
   - On push to `main`
   - Runs `semantic-release publish`
3. **package-build.yml**
   - Builds `sdist` & `wheel`
   - Uploads as artifacts

Each uses `uv venv` + `uv pip install --group dev`.

.. mermaid::

   flowchart TD
     A[Push to main / PR] --> B{CI Workflows}
     B --> |ci.yml| C[Linter → ruff]
     B --> |ci.yml| D[Test → pytest]
     B --> |ci.yml| E[Docs → Sphinx build]
     B --> |package-build.yml| F[Package → sdist & wheel]
     B --> |release.yml| G[semantic-release publish]
     C & D & E & F --> H[Upload Artifacts]
     G --> I[GitHub Release & Tag]
