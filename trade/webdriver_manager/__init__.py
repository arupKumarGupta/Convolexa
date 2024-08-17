from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
class WebdriverManager():
    
    __instance = None

    @staticmethod
    def get_instance() -> WebDriver:
        if(WebdriverManager.__instance == None):
            WebdriverManager.__instance = webdriver.Chrome(options=WebdriverManager.get_webdriver_options())
        return WebdriverManager.__instance

    @staticmethod
    def get_webdriver_options():
        options = webdriver.ChromeOptions()
        options.add_argument(
            '--headless'
        )
        return options
    