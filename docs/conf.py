# Add at top if missing

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxcontrib.mermaid",
]

# -- HTML output --------------------------------------------------------------
html_theme = "furo"
html_title = "project"

# Enable version switcher on the top bar
html_theme_options = {
    "sidebar_hide_name": True,
    "light_logo": "logo-light.svg",  # optional: your logos under _static
    "dark_logo": "logo-dark.svg",
    "source_repository": "https://github.com/michdo/python-starter-template/",
    "source_branch": "main",
    "source_directory": "docs/",
}

# Add “Edit on GitHub” button
html_context = {
    "display_github": True,
    "github_user": "michdo",
    "github_repo": "python-starter-template",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

# Add version selector
html_theme_options.update(
    {
        "versions": [
            ("main", "Latest"),
            ("v0.1.0", "v0.1.0"),
        ]
    }
)

# Static paths
html_static_path = ["_static"]
