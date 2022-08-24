# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Blades'
copyright = '2022, Blades Team'
author = 'Blades Team'



intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
    'numba': ('https://numba.readthedocs.io/en/stable', None),
    'torch': ('https://pytorch.org/docs/stable', None),
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
napoleon_use_param = True

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.doctest',
              'sphinx.ext.extlinks',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinx_gallery.gen_gallery',
              # 'sphinx.ext.linkcode',
              'sphinx_copybutton',
              'sphinx.ext.viewcode',
#               'sphinx_autodoc_typehints',
#               # 'myst_parser',
              "nbsphinx",
              'sphinx_gallery.load_style',
#               'sphinx_rtd_theme',
              'm2r2',
              # 'sphinx.ext.pngmath',
              ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_logo = '_static/blades_logo.png'
# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/favicon.ico'

sphinx_gallery_conf = {
    'line_numbers': False,
    'ignore_pattern': '/todo_',
    'examples_dirs': '../../src/blades/examples',   # path to your example scripts
    'gallery_dirs': 'examples',  # path to where to save gallery generated output
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
# Add any paths that contain custom static files (such as style sheets) here,
html_theme = 'pydata_sphinx_theme'
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will override the builtin "default.css".
html_static_path = ['_static']


html_theme_options = {
    'navigation_depth': 5,
    'collapse_navigation': False,
    "icon_links": [
            {
                "name": "GitHub",
                "url": "https://github.com/bladesteam/blades",
                "icon": "fab fa-github-square",
            },
        ],
}

import os
import sys

sys.path.insert(0, os.path.abspath('/Users/sheli564/Desktop/blades/src/blades'))
sys.path.insert(0, os.path.abspath('/Users/sheli564/Desktop/blades/'))
