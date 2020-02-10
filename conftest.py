import pytest
import requests
import json
from page_objects.nba_dot_com import NBADotCom
from page_objects.basketball_reference import BasketballReference
from page_objects.nba_api import NBAApi


@pytest.fixture
def browser(selenium):
    """
    "browser" fixture defines the webdriver where test is run.
     When running tests, using flag --chrome will run tests on chromedriver.
     If geckodriver is installed, we can run with --firefox flag in the same
     way.

    pytest-selenium package is installed in setup.py. This adds a function
     scoped fixture that enables control of a selenium webdriver.

    While a new fixture isn't really needed, I like to do it to enable the
    workflow to accept a firefox options or chrome options when desired.
    """
    selenium.maximize_window()
    return selenium


@pytest.fixture
def expected_data():
    """
    Reads expected_data.json and returns a dictionary as fixture
    """
    with open("expected_data.json") as f:
        data = json.loads(f.read())

    return data


@pytest.fixture
def nba_dot_com(browser):
    """
    Makes page object for nba.com available as a fixture
    """
    return NBADotCom(browser)


@pytest.fixture
def basketball_reference(browser):
    """
    Makes page object for basketball-reference.com a fixture
    """
    return BasketballReference(browser)

@pytest.fixture
def nba_api():
    """
    Creates fixture for the abstracted nba api.
    """
    return NBAApi()