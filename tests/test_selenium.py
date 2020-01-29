import pytest

# This set of tests checks various sites to make sure everyone has the right
# NBA all stars for the 2019-2020 season

def test_nbadotcom(browser, nba_dot_com, expected_data):
    """
    Navigates to nba.com and makes sure that the nba all star starters match
    expected_data.json
    """

    # Go to official nba.com all star page
    browser.get("https://www.nba.com/allstar/2020/roster#/")
    web_names = nba_dot_com.player_names()

    def names_match(web_names, expected_data):
        names = []

        for name in expected_data['all_stars']['east']:
            names.append(name)

        for name in expected_data['all_stars']['west']:
            names.append(name)

        return names.sort() == web_names.sort()

    assert(names_match(web_names, expected_data))

