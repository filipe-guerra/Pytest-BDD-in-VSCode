# coding=utf-8
import pytest, time
from tests.framework.fixture import googleHomePage
from tests.framework.fixture import app
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

@scenario('features/buscaGoogle.feature', 'Make a search')
def test_make_a_search():
    """Make a search."""


@given('Iam on Google search page')
def iam_on_google_search_page(googleHomePage):
    assert googleHomePage.goToGoogleSearchPage()


@when('I press enter to search')
def i_press_enter_to_search(googleHomePage):
    googleHomePage.pressEnterToSearch()


@when('I put <text> on the search input')
def i_put_text_on_the_search_input(googleHomePage, text):
    googleHomePage.putTextOnSearchInput(text)


@then('I see if results contains <txtResult>')
def i_see_if_results_contains(googleHomePage, txtResult, app):
    assert googleHomePage.seeResults(txtResult)
    app.take_screenshot('results')
    app.driver.quit()
