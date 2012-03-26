extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'django-tumblelog'
copyright = '2012, Chuck Harmston'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'nature'
html_title = None
html_short_title = 'django-tumblelog'
html_static_path = ['_static']
html_domain_indices = False
html_use_index = False
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
html_sidebars = {
    '**': [
        'custom_css.html',
        'about.html',
        'watch.html',
        'globaltoc.html',
        'searchbox.html',
    ],
}
htmlhelp_basename = 'django-tumblelogdoc'
