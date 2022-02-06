import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument('window-size=1920x1080') #standard resolution
        self.driver = webdriver.Chrome(options=chrome_options)

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
        
