import allure
import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have



@allure.title('Checking wiki search')
@pytest.mark.parametrize('mobile_setup', ['android'], indirect=True)
def test_wiki_search(mobile_setup):
    with step('fill in search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")

    with step('verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than_or_equal(1))
        results.first.should(have.text("BrowserStack"))

    with step('open the article'):
        results.first.should(have.text("BrowserStack")).click()
        allure.attach(
            browser.driver.get_screenshot_as_png(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )
