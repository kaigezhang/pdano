from flask.helpers import get_debug_flag
from server.settings import DevConfig, ProdConfig

from server.app import create_app

CONFIG = DevConfig if get_debug_flag() else ProdConfig
app = create_app(CONFIG)