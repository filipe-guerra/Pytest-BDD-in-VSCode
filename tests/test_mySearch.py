# coding=utf-8
from selenium import webdriver
from tests.pages.googlePage import GoogleHomePage
import pytest

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@pytest.fixture
def driver():
    driver = None
    if driver == None:
        driver = webdriver.Chrome()
    return driver

@pytest.fixture
def googleHomePage(driver):
    googleHomePage = GoogleHomePage(driver)
    yield googleHomePage

@scenario('features/buscaGoogle.feature', 'Make a search')
def test_make_a_search():
    """Make a search."""


@given('Iam on Google search page')
def iam_on_google_search_page(googleHomePage):
    googleHomePage.iamOnGoogleSearchPage()


@when('I press enter to search')
def i_press_enter_to_search(googleHomePage):
    googleHomePage.pressEnterToSearch()


@when('I put <text> on the search input')
def i_put_text_on_the_search_input(googleHomePage, text):
    googleHomePage.putTextOnSearchInput(text)


@then('I see if results contains <txtResult>')
def i_see_if_results_contains(googleHomePage, txtResult):
    googleHomePage.seeResults(txtResult)