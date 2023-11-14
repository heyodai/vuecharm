from unittest.mock import patch
import pytest
from vuecharm.app import VueApp
from vuecharm.page import Page

@patch('dagwood.assemble')
def test_init(mock_assemble):
    mock_assemble.return_value = "Mocked log"
    app = VueApp()
    assert app.log == "Mocked log"
    assert app.pages == []

def test_transpile():
    pass

def test_build_routes():
    app = VueApp()

    home_page = Page('Home', 'Home Page', 'home')
    about_page = Page('About', 'About Page', 'about')
    app.pages = [home_page, about_page]

    routes = app.build_routes()
    expected_routes = ["{ path: '/home', component: Home }", "{ path: '/about', component: About }"]
    assert routes == expected_routes
