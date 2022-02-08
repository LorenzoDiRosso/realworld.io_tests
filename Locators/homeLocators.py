from selenium.webdriver.common.by import By

class HomeLocators:

    # Home page elements
    settings_link = (By.LINK_TEXT, 'Settings')
    your_feed_link = (By.LINK_TEXT, 'Your Feed')

    bio_text = (By.XPATH, "//p[@class='ng-binding']")