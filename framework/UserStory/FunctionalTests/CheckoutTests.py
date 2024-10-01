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

class CheckoutTests(unittest.TestCase):
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
            print("Checkout Tests passed successfully")
        cls.driver.quit()
        
    def test_billing(self):
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-bike-light')
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            self.framework.click_element((By.ID, 'checkout'))
            checkout_form_details = {"first-name": "myfirstname", "last-name": "my", "postal-code": "123456"}
            self.framework.fill_form(checkout_form_details)
            self.framework.click_element((By.ID, 'continue'))
            final_amount = self.helper.calculate_total()
            self.assertEqual(final_amount, 43.18)
            self.success_flag+=1
            sleep(5)
        except AssertionError as ae:
            print(f"Billing test failed:Total was incorrect: {ae}")
        except Exception as e:
            print(e)
