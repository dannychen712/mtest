import pytest


# Checks the NBA API to make sure their All Stars match my expected data
def names_match(api_names, expected_data):
    """
    Method for assertions to match any properly formatted
    names array to expected data
    """
    names = []

    for name in expected_data['all_stars']['east']:
        names.append(name)
    for name in expected_data['all_stars']['west']:
        names.append(name)
    return names.sort() == api_names.sort()

def test_nba_api_match(nba_api, expected_data):
    """
    Checks that the NBA API returns a list All Stars that match our expected
     data.
    """
    nba_api.call_all_stars()
    api_star_names = nba_api.return_all_star_names()

    assert (names_match(api_star_names, expected_data))
