from Locators.signinLocator import SigninLocator
from selenium.webdriver.common.by import By

class SigninPage: 

    def __init__(self, driver):
        self.driver = driver
        self.signin_link_text = SigninLocator.signin_link_text
        self.email_textbox_xpath = SigninLocator.email_textbox_xpath
        self.password_textbox_xpath = SigninLocator.password_textbox_xpath
        self.signin_button_xpath = SigninLocator.signin_button_xpath

    def click_signin_Link(self):
        self.driver.find_element(By.LINK_TEXT, self.signin_link_text).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_signin_button(self):
        self.driver.find_element(By.XPATH, self.signin_button_xpath).click()

    def check_signin_link_exists(self):
        if(self.driver.find_element(By.LINK_TEXT, self.signin_link_text)):
            return True
        else:
            return False