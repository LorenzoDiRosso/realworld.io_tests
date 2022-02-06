import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('log-level=3')
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080') #standard resolution
        s=Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=s, options=chrome_options)

        print("-----------------------------------------")
        print("Test is started")

        self.driver.implicitly_wait(10)
        self.driver.get('https://demo.realworld.io/#/register')


        yield self.driver
        if self.driver is not None:
                print("-----------------------------------------")
                print("Tests is finished")
                self.driver.close()
                self.driver.quit()
        
