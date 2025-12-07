import allure
import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.title('Checking click in web view')
@pytest.mark.parametrize('mobile_setup', ['ios'], indirect=True)
def test_ios_click(mobile_setup):
    with step("Check the second element has the title Web View"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[2]")).should(
            have.text('Web View'))

    with step("click the web view"):
        browser.element((AppiumBy.XPATH, "//XCUIElementTypeTabBar//XCUIElementTypeButton[2]")).click()
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )