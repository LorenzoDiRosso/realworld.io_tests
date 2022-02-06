from Locators.settingsLocators import SettingsLocators
from selenium.webdriver.common.by import By

class SettingsPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_xpath = SettingsLocators.username_textbox_xpath
        self.bio_textbox_xpath = SettingsLocators.bio_textbox_xpath
        self.email_textbox_xpath = SettingsLocators.email_textbox_xpath
        self.password_textbox_xpath = SettingsLocators.password_textbox_xpath
        self.update_settings_button_css = SettingsLocators.update_settings_button_css
        self.logout_button_css = SettingsLocators.logout_button_css

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys(username)

    def enter_bio(self, bio):
        self.driver.find_element(By.XPATH, self.bio_textbox_xpath).send_keys(bio)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_update_settings_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.update_settings_button_css).click()

    def click_logout_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.logout_button_css).click()