import os
from appium import webdriver
from dotenv import load_dotenv
from selene.support.shared import browser


class Application:

    def __init__(self, env):
        load_dotenv()
        user = os.getenv('LOGIN')
        key = os.getenv('KEY')
        url = os.getenv('APPIUM_BROWSERSTACK')
        if env == 'android':
            desired_capabilities = {
                "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
                "deviceName": "Google Pixel 3",
                "os_version": "9.0",
                "platformName": "android",
                "project": "First Python project",
                "build": "browserstack-build-1",
                "name": "mobile_test"
            }

            driver = webdriver.Remote(command_executor=f"http://{user}:{key}@{url}/wd/hub",
                                      desired_capabilities=desired_capabilities)
            browser.config.driver = driver

    def destroy(self):
        browser.quit()
