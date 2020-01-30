# Mersive Test
This is the test for Mersive. I am validating a list of NBA All stars for
the year 2020 located in expected_data.json matches several listings online.
Those include:
1. The web page of nba.com for a frontend test
2. The web page of basketball-reference.com for a frontend test
3. The REST api at data.nba.net

This is should highlight what I consider to be an appropriate organizational
structure of a pytest test suite.

Results are presented as html, you can view an example by opening example_report.html.
Other pytest libraries exist for reporting including JSON and JUNITXML which can be consumed by services like Jenkins.

I will probably need to update the "expected_data.json" after I submit because the new NBA all star reserves will be
announced on 1/30/2020 at 5:00PM MT, but such is the life of QA Automation :).

## Structure

page_objects:
This directory contains page objects that either abstract the web page or api.
The web tests are tested using selenium webdriver, specifically the pytest-selenium plugin.
The api tests use Requests library to make calls to the nba data api. Note the organizational
structure in nba_api.py

tests:
This contains the logic for both tests. Each actual pytest test method is begins with "test_".
Pytest knows to pick those up as individual tests. Any method that does not have a "test_" prefix is a helper method.

conftest.py:
This I use primarily to set up "fixtures" for pytest, which are made available to be passed into tests by pytest.
This is a very small project, but in a more complex project you can use this file to define logic that switches
between browsers, adds browser options, and even use remote webdriver for services like saucelabs.
Additionally you may define pre-run and post-run methods for cleanup or data recording.

expected_data.json:
A json of the NBA all stars I expect to see.

setup.py:
This installs requirements for this project. It is also used to define fields used for Distutils, which is a
way to distribute and define python modules.

## Test Cases
1. Given I navigate to the NBA all star roster page for 2019-2020 on nba.com,
When I observe the listed NBA all stars,
Then I should see that it matches expected_data.json.

2. Given I navigate to the NBA all star roster page for 2019-2020 on basketball-reference.com,
When I observe the listed NBA all stars,
Then I should see that it matches expected_data.json.

3. Given I send a GET request to data.nba.net to the 2019-2020 nba all star roster endpoint,
When I parse the json response,
Then I should be able to match the listed all stars with expected_data.json.

### Prerequisites
Python 3.7.3, pip3

### Installing
1. Clone repo into directory
2. `cd` into directory
3. create new virtual environment
    `python3 -m venv mersivetest`
4. install requirements
    `pip install .`
5. If you get an error regarding bdist-wheel, run `pip install wheel`, then
    rerung `pip install .`

## Running the tests

`pytest --driver chrome --html=results.html`


