import pytest


# This set of tests checks various sites to make sure everyone has the right
# NBA all stars for the 2019-2020 season

def test_nbadotcom(browser, nba_dot_com, expected_data):
    """
    Navigates to nba.com and makes sure that the nba all stars match
    expected_data.json
    """

    # Go to official nba.com all star page
    browser.get("https://www.nba.com/allstar/2020/roster#/")
    web_names = nba_dot_com.player_names()
    web_names.sort()
    expected_stars = expected_data['all_stars']
    expected_stars.sort()

    assert(web_names == expected_stars)

def test_bball_reference(browser, expected_data, basketball_reference):
    """
    Navigates to basketball-reference.com and checks that the listed all stars
    matches expected_data.json. THIS SHOULD FAIL as of 1/30 UNTIL BASKETBALL
    REFERENCE UPDATES THEIR SITE FOR ALL STAR RESERVES.
    """
    browser.get("https://www.basketball-reference.com/allstar/NBA_2020.html")
    web_names = basketball_reference.player_names()
    web_names.sort()
    expected_stars = expected_data['all_stars']
    expected_stars.sort()

    assert(web_names == expected_stars)