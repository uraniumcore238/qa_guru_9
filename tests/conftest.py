import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selene.support.shared import browser
from selene import Browser, Config

from utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

# @pytest.fixture(scope='session')
# def browser_name(request):
#     return request.config.getoption('--browser')



@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub", options=options)
    # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=options)

    # browser = Browser(Config(driver))
    browser.config.driver = driver

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

