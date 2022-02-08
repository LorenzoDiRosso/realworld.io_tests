from Locators.signinLocator import SigninLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

class SigninPage: 

    def __init__(self, driver):
        self.driver = driver
        

    def click_signin_Link(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SigninLocator.signin_link)).click()
        # self.driver.find_element(By.LINK_TEXT, self.signin_link_text).click()

    def enter_email(self, email):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SigninLocator.email_textbox)).send_keys(email)
        # self.driver.find_element(By.XPATH, self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SigninLocator.password_textbox)).send_keys(password)
        # self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys(password)

    def click_signin_button(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SigninLocator.signin_button)).click()
        # self.driver.find_element(By.XPATH, self.signin_button_xpath).click()

    def check_signin_link_exists(self):
        if(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(SigninLocator.signin_link))):
        # if(self.driver.find_element(By.LINK_TEXT, self.signin_link_text)):
            return True
        else:
            return False