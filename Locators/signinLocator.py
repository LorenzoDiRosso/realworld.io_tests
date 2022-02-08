from selenium.webdriver.common.by import By

class SigninLocator:

    # Signin page elements
    signin_link = (By.LINK_TEXT, 'Sign in')
    email_textbox = (By.XPATH, "//input[@type='email']")
    password_textbox = (By.XPATH, "//input[@type='password']")
    signin_button = (By.XPATH, "//button[@type='submit']")