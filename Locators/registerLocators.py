from selenium.webdriver.common.by import By

class RegisterLocators:

    # Registration page elements
    username_textbox = (By.CSS_SELECTOR, 'fieldset:nth-of-type(1) > .form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid')
    email_textbox = (By.CSS_SELECTOR, '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid.ng-valid-email')
    password_textbox = (By.CSS_SELECTOR, '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid')
    sign_up_button = (By.XPATH, "//button[@type='submit']")

    error_message = (By.LINK_TEXT, 'error-messages')