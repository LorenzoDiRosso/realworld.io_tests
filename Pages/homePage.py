from Locators.homeLocators import HomeLocators
from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.settings_link_text = HomeLocators.settings_link_text
        self.your_feed_link_text = HomeLocators.your_feed_link_text

    def click_settings_link(self):
        self.driver.find_element(By.LINK_TEXT, self.settings_link_text).click()


    ## Check Results ##

    def check_settings_link_exists(self):
        if(self.driver.find_element(By.LINK_TEXT, self.settings_link_text)):
            return True
        else:
            return False

    def check_your_feed_link_exists(self):
        if(self.driver.find_element(By.LINK_TEXT, self.your_feed_link_text)):
            return True
        else:
            return False

    def check_username_link_is_updated(self, username):
        if(self.driver.find_element(By.LINK_TEXT, username)):
            return True
        else:
            return False