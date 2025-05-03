Project Structure
=================

.. code-block:: text

   .
   ├── .devcontainer/          # VSCode & Dockerfile
   ├── .github/
   │   └── workflows/         # CI pipelines
   ├── docs/
   │   ├── _static/           # logos, CSS, JS
   │   ├── _templates/        # Sphinx templates
   │   ├── *.rst              # manual pages
   │   └── conf.py            # Sphinx config
   ├── src/
   │   └── playground/        # Python package
   ├── tests/                 # pytest tests
   ├── cookiecutter.json      # scaffold params
   ├── pyproject.toml         # metadata & deps
   ├── pre-commit-config.yaml # hooks
   └── README.md

.. mermaid::

   graph TB
     root["📁 (project root)"]
     root --> devc["📁 .devcontainer/"]
     root --> gha["📁 .github/workflows/"]
     root --> docs["📁 docs/"]
     docs --> conf["conf.py"]
     docs --> pages["*.rst"]
     docs --> static["_static/"]
     root --> src["📁 src/"]
     src --> pkg["playground/"]
     root --> tests["📁 tests/"]
     root --> pyproj["pyproject.toml"]
     root --> gitignore[".gitignore"]
     root --> readme["README.md"]
