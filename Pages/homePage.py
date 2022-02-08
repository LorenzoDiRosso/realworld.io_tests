from Locators.homeLocators import HomeLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_settings_link(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomeLocators.settings_link)).click()


    ## Check Results ##
    def check_settings_link_exists(self):
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomeLocators.settings_link))):
            return True
        else:
            return False

    def check_your_feed_link_exists(self):
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(HomeLocators.your_feed_link))):
            return True
        else:
            return False

    def check_username_link_is_updated(self, username):
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.LINK_TEXT, username))):
            return True
        else:
            return False