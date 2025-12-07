import allure
import dotenv
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import os

from selenium import webdriver

dotenv.load_dotenv()
username = os.getenv('USERNAME')
accesskey = os.getenv('ACCESSKEY')

@pytest.fixture(scope='function', params=['android', 'ios'])
def mobile_setup(request):
    if request.param == 'android':
        options = UiAutomator2Options().load_capabilities({

            "platformName": "android",
            "platformVersion": "12.0",
            "deviceName": "Samsung Galaxy S22 Ultra",
            "app": "bs://sample.app",
            "bstack:options": {
                "userName": username,
                "accessKey": accesskey,
                "projectName": "android tests",
                "buildName": "browserstack-build-1",
            }
        })
    if request.param == 'ios':
        options = XCUITestOptions().load_capabilities({
            "platformName": "ios",
            "platformVersion": "17",
            "deviceName": "iPhone 15 Pro Max",
            "app": "bs://sample.app",
            'bstack:options': {
                "userName": username,
                "accessKey": accesskey,
                "projectName": "ios tests",
                "buildName": "browserstack-build-1",
            }
        }
        )

    browser.config.driver = webdriver.Remote(
        f"https://{username}:{accesskey}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    allure.attach(browser.driver.get_screenshot_as_png(), name='screenshot',attachment_type=allure.attachment_type.PNG)

    browser.quit()
