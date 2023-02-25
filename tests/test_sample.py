import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.conditions import have


@allure.title("Wikipedia search BrowserStack")
def test_search_wikipedia(app):
    app.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    app.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")
    app.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).should(have.size_greater_than(0))


@allure.title("Wikipedia search selene and go to page")
def test_search_selene(app):
    app.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    app.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("selene")
    app.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).click()
    app.element((AppiumBy.CLASS_NAME, 'android.widget.TextView')).should(have.text('An error occurred'))
