# -*- coding: utf-8 -*-
#
# uthcode documentation build configuration file, created by
# sphinx-quickstart on Sat Oct 24 18:08:47 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
# At the top.
#import sphinx_bootstrap_theme

# ...

# Activate the theme.
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',
              'sphinx.ext.todo', 'sphinx.ext.coverage',
              'sphinx.ext.extlinks', 'sphinx.ext.pngmath',
              'sphinxcontrib.runcode', 'sphinx_git']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'uthcode'
copyright = u'2014, Senthil Kumaran'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d %b of %y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Links for edit

# :c-suggest-improve:`name.c`
# :c-better-explain:`name.rst`
# :python-suggest-improve:`name.py`
# :python-better-explain:`name.rst`

extlinks = {'c-suggest-improve':
    ('https://github.com/uthcode/uthcode/blob/version1/languages/cprogs/%s',
    "Suggest a Code Improvement: "),
            'c-better-explain':
    ('https://github.com/uthcode/uthcode/tree/version1/source/cprogramming/%s',
    "Suggest a better explanation for "),
            'python-suggest-improve':
    ("https://github.com/uthcode/uthcode/blob/version1/languages/python/%s",
        "Suggest a Code Improvement:"),
             'python-better-explain':
    ("https://github.com/uthcode/uthcode/blob/version1/source/python/%s",
        "Suggest a better explanation for "),
            'ruby-suggest-improve':
    ("https://github.com/uthcode/uthcode/blob/version1/languages/ruby/%s",
        "Suggest a Code Improvement:"),
             'ruby-better-explain':
    ("https://github.com/uthcode/uthcode/blob/version1/source/ruby/%s",
        "Suggest a better explanation for "),
            'java-suggest-improve':
    ("https://github.com/uthcode/uthcode/blob/version1/languages/java/%s",
        "Suggest a Code Improvement:"),
             'java-better-explain':
    ("https://github.com/uthcode/uthcode/blob/version1/source/java/%s",
        "Suggest a better explanation for "),
            'scala-suggest-improve':
    ("https://github.com/uthcode/uthcode/blob/version1/languages/scala/%s",
        "Suggest a Code Improvement:"),
             'scala-better-explain':
    ("https://github.com/uthcode/uthcode/blob/version1/source/scala/%s",
        "Suggest a better explanation for "),
            'go-suggest-improve':
    ("https://github.com/uthcode/uthcode/blob/version1/languages/go/%s",
        "Suggest a Code Improvement:"),
             'go-better-explain':
    ("https://github.com/uthcode/uthcode/blob/version1/source/go/%s",
        "Suggest a better explanation for "),
              'use-local-compiler':
    ('http://www.seas.upenn.edu/cets/answers/%s.html',
              'Please use a local c compiler to run this program.'),
}




# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {'headerbg':'white','footerbg':'white'}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'uthcode'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'uthcode'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = '_static/uthcode.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%d %b, %y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {'index': ['indexsidebar.html', 'searchbox.html']}
#html_additional_pages = {'index': 'index.html', 'foo' : 'foo.html', 'bar': 'bar.html'}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'uthcodedoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
#latex_documents = [
#   u'Senthil Kumaran', 'manual'),
#]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True
