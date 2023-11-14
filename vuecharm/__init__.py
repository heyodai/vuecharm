from .base import VueBase, VueComponent
from .app import VueApp
from .page import Page
from .components import AppBar #, Button, Card, CardActions, CardContent, CardHeader, Container, Grid, GridItem, Icon, IconButton, List, ListItem, ListItemText, Page, Text, TextField, Toolbar, Typography

def app() -> VueApp:
    """
    Create a new Vue.js app

    Returns
    -------
    VueApp
        A new Vue.js app
    """
    return VueApp()

def new_page(name: str, title: str = None, path: str = None) -> Page:
    """
    Create a new Vue.js page (i.e. a view).

    >>> page = new_page('Home', 'Home Page', '/home')
    >>> page.name
    'Home'

    >>> page.title
    'Home Page'

    >>> page.path
    '/home'

    Parameters
    ----------
    name : str
        The internal name of the page, used in Python code.
    title : str, optional
        The title of the page, used in the browser tab. Defaults to the name if not provided.
    path : str, optional
        The URL path of the page. Defaults to the name if not provided.

    Returns
    -------
    Page
        A new Vue.js page
    """
    return Page(name, title, path)
