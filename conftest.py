import pytest
import requests
import json
from page_objects.nba_dot_com import NBADotCom


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
