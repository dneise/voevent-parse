from __future__ import print_function
import sys, os
import voeventparse

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'nbsphinx',
              'IPython.sphinxext.ipython_console_highlighting',
              ]

RUNNING_UNDER_TOX_CI = os.environ.get('TOX_DOCS', False)

nbsphinx_execute = 'always'
# nbsphinx_execute = 'never'
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# if RUNNING_UNDER_TOX_CI=="TRUE":
#     suppress_warnings = ['ref.doc']
#     print("Suppressing some sphinx warnings cf"
#           "https://github.com/spatialaudio/nbsphinx/issues/130")
# else:
#     print(
#         "\n**************************************************************\n"
#         "ACHTUNG!\n"
#         "You may need to disable the 'error on warning flag' to build "
#           "docs locally, "
#           "cf https://github.com/spatialaudio/nbsphinx/issues/130\n"
#         "(See Makefile:SPHINXOPTS)"
#         "\n**************************************************************\n")


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'voevent-parse'
copyright = u'2013-2016 Tim Staley'

# The short X.Y version.
version = voeventparse.__version__
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# otherwise, readthedocs.org uses their theme by default, so no need to specify it

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
# Output file base name for HTML help builder.
htmlhelp_basename = 'VOEvent-parsedoc'

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

# -- Custom options ----------------------
autodoc_member_order = 'bysource'
todo_include_todos = True

nitpicky = True
nitpick_ignore = [
    ("py:obj", "lxml.etree.DocumentInvalid"),
    ("py:obj", "lxml.etree"),
    ("py:class", "bytes"),
    ("py:obj", "bytes"),

]
