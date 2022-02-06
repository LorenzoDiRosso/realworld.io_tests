from Locators.registerLocators import RegisterLocators
from selenium.webdriver.common.by import By

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_css = RegisterLocators.username_textbox_css
        self.email_textbox_css = RegisterLocators.email_textbox_css
        self.password_textbox_css = RegisterLocators.password_textbox_css
        self.sign_up_button_xpath = RegisterLocators.sign_up_button_xpath

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, self.username_textbox_css).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.email_textbox_css).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.password_textbox_css).send_keys(password)

    def click_signUp(self):
        self.driver.find_element(By.XPATH, self.sign_up_button_xpath).click()
