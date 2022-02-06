from Pages.registrationPage import RegistrationPage
from Pages.homePage import HomePage
from Base.base import Base
import pytest
from datetime import datetime

@pytest.mark.usefixtures('set_up')
class Test_Register(Base):

    #ensures unique email + username is used for each test
    def set_input_parameters(self):
        now = datetime.now() # used to generate unique number
        unique_number = now.strftime("%Y%m%d%H%M%S") # This is to ensure no regitration with exisitng usernames/emails

        usernameString = 'User '+unique_number
        emailString = 'test+'+unique_number+'@test.com'
        passwordString = '1234'

        return usernameString, emailString, passwordString

    
    def test_registration_success(self):
        usernameString, emailString, passwordString = self.set_input_parameters()

        driver = self.driver
        register = RegistrationPage(driver)
        register.enter_username(usernameString)
        register.enter_email(emailString)
        register.enter_password(passwordString)
        register.click_signUp()

        home = HomePage(driver)
    
        #Fix here
        assert home.check_settings_link_exists
        assert home.check_your_feed_link_exists
        