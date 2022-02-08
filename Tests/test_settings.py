# from selenium.webdriver.common.by import By
from Pages import homePage
from Pages.registrationPage import RegistrationPage
from Pages.homePage import HomePage
from Pages.settingsPage import SettingsPage
from Pages.signinPage import SigninPage
from selenium.webdriver.common.by import By
from Base.base import Base
import pytest
from time import sleep
from datetime import datetime

@pytest.mark.usefixtures('set_up')
class Test_Settings(Base):

    #ensures unique email + username is used for each test
    def set_input_parameters(self):
        now = datetime.now() # used to generate unique number
        unique_number = now.strftime("%Y%m%d%H%M%S") # This is to ensure no regitration with exisitng usernames/emails

        usernameString = 'User '+unique_number
        emailString = 'test+'+unique_number+'@test.com'
        passwordString = '1234'

        return usernameString, emailString, passwordString

    # This is essentially a set up function for the setting page tests. Will clean this up later
    def register_new_user(self, driver, username, email, password):
        register = RegistrationPage(driver)
        register.enter_username(username)
        register.enter_email(email)
        register.enter_password(password)
        register.click_signUp()
        sleep(5); #temporary solution

    def test_change_username_success_TC002(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver

        self.register_new_user(driver, usernameString, emailString, passwordString)
        
        driver.get("https://demo.realworld.io/#/settings")
 
        updated_username = 'updated '+usernameString

        settings = SettingsPage(driver)
        settings.enter_username(updated_username)
        
        # settings.click_update_settings_button # not working - not doing .click()

        # Temporary fix
        updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
        updateSettingBtn.click()

        home = HomePage(driver)
        assert home.check_username_link_is_updated(updated_username)


    def test_change_bio_success_TC003(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver
 
        self.register_new_user(driver, usernameString, emailString, passwordString)

        driver.get("https://demo.realworld.io/#/settings")

        bio = "A short bio"

        settings = SettingsPage(driver)
        settings.enter_bio(bio)
        
        # settings.click_update_settings_button # not working - not doing click()

        # Temporary fix
        updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
        updateSettingBtn.click()
 

        home = HomePage(driver)
        home.assert_text_exists_in_page_source(bio)


    def test_change_email_success_TC004(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver

        self.register_new_user(driver, usernameString, emailString, passwordString)
        
        driver.get("https://demo.realworld.io/#/settings")
 
        updated_email = 'updated'+emailString

        settings = SettingsPage(driver)
        settings.enter_email(updated_email)
        
        # settings.click_update_settings_button # not working - not doing .click()

        # Temporary fix
        updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
        updateSettingBtn.click()

        driver.get("https://demo.realworld.io/#/settings")

        settings.click_logout_button

        signin = SigninPage(driver)
        signin.click_signin_Link
        signin.enter_email(updated_email)
        signin.enter_password(passwordString)
        signin.click_signin_button

        home = HomePage(driver)
        assert home.check_your_feed_link_exists

    def test_change_password_success_TC005(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver

        self.register_new_user(driver, usernameString, emailString, passwordString)
        
        driver.get("https://demo.realworld.io/#/settings")
 
        updated_password = 'updated'+passwordString

        settings = SettingsPage(driver)
        settings.enter_password(updated_password)
        
        # settings.click_update_settings_button # not working - not doing .click()

        # Temporary fix
        updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
        updateSettingBtn.click()

        driver.get("https://demo.realworld.io/#/settings")

        settings.click_logout_button

        signin = SigninPage(driver)
        signin.click_signin_Link
        signin.enter_email(emailString)
        signin.enter_password(updated_password)
        signin.click_signin_button

        home = HomePage(driver)
        assert home.check_your_feed_link_exists

    def test_logout_success_TC006(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver
 
        self.register_new_user(driver, usernameString, emailString, passwordString)

        driver.get("https://demo.realworld.io/#/settings")

        settings = SettingsPage(driver)
        settings.click_logout_button

        signin = SigninPage(driver)
        assert signin.check_signin_link_exists
         



