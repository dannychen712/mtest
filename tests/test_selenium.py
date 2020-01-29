import pytest

# This set of tests checks various sites to make sure everyone has the right
# NBA all stars for the 2019-2020 season

def test_nbadotcom(browser, nba_dot_com):
    """
    Navigates to nba.com and makes sure that the nba all star starters match
    expected_data.json
    """

    # Go to official nba.com all star page
    browser.get("https://www.nba.com/allstar/2020/roster#/")
    web_names =
    assert(
        nba_dot_com
    )
    import pdb; pdb.set_trace()

