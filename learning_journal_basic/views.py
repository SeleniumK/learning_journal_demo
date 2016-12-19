from pyramid.response import Response
import os

THIS_DIR = os.path.dirname(__file__)


def home_page(request):
    """Render home page."""
    imported_text = open(os.path.join(THIS_DIR, 'sample.txt')).read()
    return Response("hello")


def includeme(config):
    config.add_view(home_page, route_name="home")
