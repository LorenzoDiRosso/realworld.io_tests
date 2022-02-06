from selenium.webdriver.common.by import By
from Pages.registrationPage import RegistrationPage
from Pages.homePage import HomePage
from Pages.settingsPage import SettingsPage
from Pages.signinPage import SigninPage
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

    def test_logout_success(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver
 
        self.register_new_user(driver, usernameString, emailString, passwordString)

        driver.implicitly_wait(500)

        home = HomePage(driver)
        home.click_settings_link

        driver.implicitly_wait(500)

        settings = SettingsPage(driver)
        settings.click_logout_button

        driver.implicitly_wait(500)

        signin = SigninPage(driver)
        assert signin.check_signin_link_exists
         

    def test_change_bio_success(self):
        usernameString, emailString, passwordString = self.set_input_parameters()
        driver = self.driver
 
        self.register_new_user(driver, usernameString, emailString, passwordString)

        sleep(5) #temporary solution
        driver.get("https://demo.realworld.io/#/settings")
        sleep(5) #temporary solution

        bio = "A short bio"

        settings = SettingsPage(driver)
        settings.enter_bio(bio)
        #settings.click_update_settings_button # not working

        #temporary solution - some trouble shooting required
        updateSettingBtn = driver.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.pull-xs-right')
        updateSettingBtn.click()

        sleep(5) #temporary solution

        assert bio in driver.page_source

  #  def test_change_email_success(self):

  #  def test_change_password_success(self):

  #  def test_change_username_success(self):
