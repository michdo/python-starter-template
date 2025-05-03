# -- Project information -----------------------------------------------------
project = "Python Starter Template"
author = "Your Name"
release = "0.1.0"
version = release  # display version in the theme

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_panels",
    "sphinx_tabs.tabs",
]

autosummary_generate = True

templates_path = ["_templates"]
exclude_patterns: list[str] = []

# -- HTML output --------------------------------------------------------------
html_theme = "furo"
html_title = project
html_static_path = ["_static"]

html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo-light.svg",
    "dark_logo": "logo-dark.svg",
    "source_repository": "https://github.com/michdo/python-starter-template",
    "source_branch": "main",
    "source_directory": "docs/",
    "versions": [
        ("main", "Latest"),
        (release, release),
    ],
}

html_context = {
    "display_github": True,
    "github_user": "michdo",
    "github_repo": "python-starter-template",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
