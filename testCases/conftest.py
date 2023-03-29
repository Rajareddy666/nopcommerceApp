from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome('C:\Drivers\chromedriver_win32/chromedriver')
        print("Launching chrome browser.........")
    elif browser=='edge':
        driver=webdriver.Edge('C:\Drivers\edgedriver_win64/msedgedriver')
        print("Launching Edge browser.........")
    else:
        driver = webdriver.Chrome('C:\Drivers\chromedriver_win32/chromedriver')
        print("Launching chrome browser.........")

    return driver
def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

def pytest_configure (config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Raja'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)