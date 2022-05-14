import os

import jinja2

# PWD = os.path.dirname(__file__)
# or
PWD = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])

template_dir = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    autoescape=True)

URL = "http://api.tvmaze.com/search/shows?q={user_input}"

WARNING = '\033[93m'
