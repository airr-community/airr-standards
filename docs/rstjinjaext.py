# Taken from http://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/


import jinja2


def rstjinja(app, docname, source):
    """
    Render RST page with jinja templating. Data in config.html_context
    """
    template = jinja2.Template(source[0])
    rendered = template.render(app.config.html_context)
    source[0] = rendered
    print('foo')
    print(docname)


def setup(app):
    app.connect("source-read", rstjinja)
