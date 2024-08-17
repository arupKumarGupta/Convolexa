from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class DomManager():
    # kite login
    #email
    user_id_xpath = '//*[@id="userid"]'

    #password
    pwd_xpath = '//*[@id="password"]'

    #login button
    login_btn = '//*[@id="container"]/div/div/div[2]/form/div[4]/button'

    #totp xpath
    toptp_xpath = '/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/form/div[1]/input'

    #authorize_btn
    authorize_button_xpath = '/html/body/div[1]/div/div[1]/div/div/form/div/button'

    def find_user_id_input(self, webdriver: WebDriver) -> WebElement:
        return webdriver.find_element(By.XPATH,self.user_id_xpath)
    
    
    def find_pwd(self, webdriver: WebDriver) -> WebElement:
        return webdriver.find_element(By.XPATH,self.pwd_xpath)
    
    def find_login_button(self, webdriver: WebDriver) -> WebElement:
        return webdriver.find_element(By.XPATH,self.login_btn)
    
    def find_totp_input(self, webdriver: WebDriver) -> WebElement:
            return webdriver.find_element(By.XPATH,self.toptp_xpath)
    
    def find_authorize_button(self, webdriver: WebDriver) -> WebElement:
            return webdriver.find_element(By.XPATH,self.authorize_button_xpath)


dom_manager = DomManager()