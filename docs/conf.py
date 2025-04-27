# Configuration file for the Sphinx documentation builder.

project = 'Python Starter Template'
copyright = '2025, Michael Dold'
author = 'Michael Dold'

release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.mermaid'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# Mermaid configuration (optional tweak)
mermaid_version = "9.1.3"
