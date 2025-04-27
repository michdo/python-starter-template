import os

# -- Project information -----------------------------------------------------

project = 'Python Starter Template'
copyright = '2025, Michael Dold'
author = 'Michael Dold'

release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.mermaid',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output --------------------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Mermaid configuration ---------------------------------------------------

if os.getenv("GITHUB_ACTIONS") == "true":
    # Running in GitHub Actions — prevent sphinxcontrib-mermaid from installing
    mermaid_output_format = "raw"
    html_js_files = [
        'js/mermaid.min.js',
    ]
else:
    # Running locally — allow automatic management
    mermaid_output_format = "png"
