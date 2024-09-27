from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver import WebDriver
from Framework import Framework

class TestSauceDemo(unittest.TestCase):
    URL='https://www.saucedemo.com/'
    USERNAME='standard_user'
    PASSWORD='secret_sauce'
    WAIT_TIME=10

    @classmethod
    def setUpClass(cls):
        try:
            cls.webdriver =WebDriver()
            cls.driver= cls.webdriver.driver
            cls.framework= Framework(cls.driver)
        except Exception as e:
            print(f"error in setup;{e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test_login(self):
        try:
            self.framework.navigate_to_page(self.URL)
            self.framework.get_element((By.ID,'user-name'))
            self.framework.enter_field((By.ID,'user-name'),self.USERNAME)
            self.assertEqual(self.framework.get_text((By.ID,'user-name'),self.USERNAME))

        except Exception :
            print("error occured")
        


if __name__ == "__main__":
   unittest.main()
