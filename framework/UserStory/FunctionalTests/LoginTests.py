from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver import WebDriver
from Framework import Framework
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import StaleElementReferenceException
from Helper_Modules import HelperModules

class LoginTests(unittest.TestCase):
    URL='https://www.saucedemo.com/'
    USERNAME='standard_user'
    PASSWORD='secret_sauce'
    WAIT_TIME=10
    success_flag=0

    @classmethod
    def setUpClass(cls):
        try:
            cls.webdriver =WebDriver()
            cls.driver= cls.webdriver.driver
            cls.framework= Framework(cls.driver)
            cls.helper=HelperModules(cls.framework)
        except Exception as e:
            print(f"error in setup;{e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        if(cls.success_flag==0):
            print("Login Tests passed successfully")
        cls.driver.quit()
        
    def test_login(self):
        try:
            self.framework.navigate_to_page(self.URL)
            login_credentials={"user-name":"standard_user","password":"secret_sauce"}
            self.framework.fill_form(login_credentials)
            self.framework.submit_form((By.TAG_NAME,'form'))
            WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_all_elements_located((By.ID,'inventory_container')))
            self.assertEqual(self.framework.get_current_url(),self.driver.current_url)
            self.success_flag+=1
            sleep(5)
        except AssertionError as ae:
            print(f"error in navigating to inventory page:{ae}")
        except Exception as e:
            print(f"Login test failed")

    def test_invalid_login(self):
        try:
            self.framework.navigate_to_page(self.URL)
            
            login_credentials={"user-name":"invalid","password":"invalid"}
            self.framework.fill_form(login_credentials)
            self.framework.submit_form((By.TAG_NAME,'form'))
            error_msg=self.framework.is_element_visible((By.CLASS_NAME,'error-message-container'))
            self.assertTrue(error_msg)
        except AssertionError as ae:
            print(f"Login test failed:error msg did not load")

    def test_navigate_to_invalid_login(self):
        try:
            self.test_login()
            self.helper.logout()
            self.driver.back()
            self.assertEqual(self.framework.get_current_url(),self.URL)
        except AssertionError as ae:
            print(f"Login test failed:invalid navigation to login allowed")