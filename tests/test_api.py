import pytest


# Checks the NBA API to make sure their All Stars match my expected data


def test_nba_api_match(nba_api, expected_data):
    """
    Checks that the NBA API returns a list All Stars that match our expected
     data.
    """
    nba_api.call_all_stars()
    api_star_names = nba_api.return_all_star_names()
    api_star_names.sort()
    expected_stars = expected_data['all_stars']
    expected_stars.sort()

    assert (api_star_names == expected_stars)

