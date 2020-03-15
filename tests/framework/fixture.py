import pytest
from tests.pages.googlePage import GoogleHomePage
from tests.framework.app import APP

@pytest.fixture
def app():
    app = APP()
    yield app

@pytest.fixture
def googleHomePage(app):
    googleHomePage = GoogleHomePage(app)
    yield googleHomePage
