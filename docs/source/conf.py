# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# import sphinx_rtd_theme


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "protein-folding-qc"
copyright = "2024, CCF & IBM Team"
author = "CCF & IBM Team"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = [
#     "sphinx.ext.autodoc",
#     "sphinx.ext.napoleon",
#     # 'sphinx_autodoc_typehints',
#     "sphinx_toolbox.more_autodoc.typehints",
#     "sphinx.ext.todo",
#     "sphinx.ext.mathjax",
#     "sphinx.ext.viewcode",
#     "sphinx_rtd_theme",
# ]

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "matplotlib.sphinxext.plot_directive",
    "qiskit_sphinx_theme",
]


templates_path = ["_templates"]
exclude_patterns = []
numfig = True
numfig_format = {"table": "Table %s"}
language = "en"
pygments_style = "colorful"
add_module_names = False
modindex_common_prefix = ["qufold."]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "qiskit-ecosystem"
html_static_path = ["_static"]
html_theme_options = {
    "disable_ecosystem_logo": True,
}

# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# autodoc/autosummary options
autosummary_generate = True
autosummary_generate_overwrite = False
autoclass_content = "both"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Show docstring under __init__ method
autoclass_content = "both"

# autodoc_typehints = "description"
typehints_use_rtype = False
