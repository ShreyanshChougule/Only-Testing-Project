import pytest
from selenium import webdriver

from Utilities.Config_File import Config_File_Opractions


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        Edge_options = webdriver.EdgeOptions()
        Edge_options.add_argument("headless")
        driver = webdriver.Edge(options=Edge_options)

    R = Config_File_Opractions()
    # driver.get("https://only-testing-blog.blogspot.com")
    driver.get(R.getURL())
    driver.maximize_window()
    return driver
