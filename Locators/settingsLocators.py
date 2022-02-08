from selenium.webdriver.common.by import By

class SettingsLocators:

    #Settings page elements
    username_textbox = (By.XPATH, "//input[@placeholder='Username']") 
    update_settings_button = (By.XPATH, "//button[@class='btn btn-lg btn-primary pull-xs-right']")
    bio_textbox = (By.XPATH, "//textarea[@placeholder='Short bio about you']")
    email_textbox = (By.XPATH, "//input[@type='email']")
    password_textbox = (By.XPATH, "//input[@type='password']")
    logout_button_css = (By.CSS_SELECTOR, ".btn.btn-outline-danger")


