from .base import VueBase, VueComponent, VuePage
from .components import AppBar

def app():
    """
    Create a new Vue.js app
    """
    app_bar = AppBar()
    return app_bar.render()