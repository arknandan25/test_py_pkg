import os
import jinja2

PWD = os.path.dirname(__file__)

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(PWD))

URL = "http://api.tvmaze.com/search/shows?q={user_input}"

WARNING = '\033[93m'
