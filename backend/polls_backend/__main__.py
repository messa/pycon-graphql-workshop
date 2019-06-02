from aiohttp.web import run_app
import logging
from .app import application

logging.basicConfig(level=logging.DEBUG)
run_app(application)
