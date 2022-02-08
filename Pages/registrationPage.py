from Locators.registerLocators import RegisterLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterLocators.username_textbox)).send_keys(username)

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterLocators.email_textbox)).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterLocators.password_textbox)).send_keys(password)

    def click_signUp(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterLocators.sign_up_button)).click()

    def check_error_message_exists(self):
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegisterLocators.error_message))):
            return True
        else:
            return False
