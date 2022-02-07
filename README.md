# demo.realworld.io UI automation tests

The UI automation tests are done with python, pytest and selenium.

# Setup

- Clone this repository
- Navigate to the cloned folder
- install, create and activate the virtual environment using virtualenv

# Installation
Make sure to have the latest installation of the following:
- python3
- pip3

And then execute:

``` pip3 install -r requirements.txt```

# Usage

To run the tests, execute:

``` pytest```

# Reports

For better illustration on the testcases, allure reports has been integrated.
To enable Allure listener to collect results during the test execution, simply run:

``` pytest --alluredir=allure_test_results```

To see the actual report after the tests have finished, run:

``` allure serve allure_test_results```