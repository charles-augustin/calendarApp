import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService


@pytest.fixture()
def setup(browser):
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service)
    if browser == 'chrome':
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        firefox_service = FireFoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
        print("Launching firefox browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


# pytest HTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Calendar App'
    config._metadata['Module Name'] = 'Web Test'
    config._metadata['Tester'] = 'Swapna'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
