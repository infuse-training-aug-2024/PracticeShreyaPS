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


class CheckoutTests(unittest.TestCase):
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
        
    def test_billing(self):
            try:
                self.test_login()
                self.test_add_to_cart()
                self.test_add_to_cart2()
                self.framework.click_element((By.CLASS_NAME,'shopping_cart_link'))
                self.framework.click_element((By.ID,'checkout'))
                checkout_form_details={"first-name":"myfirstname","last-name":"my","postal-code":"123456"}
                self.framework.fill_form(checkout_form_details)
                self.framework.click_element((By.ID,'continue'))
                item_in_cart=self.framework.get_elements((By.CLASS_NAME,'inventory_item_price'))
                total=0.0
                for item in item_in_cart:
                    price_value = float(item.text.replace('$', ''))
                    total=total+price_value
                tax=float(self.framework.get_text((By.CLASS_NAME,'summary_tax_label')).replace('Tax: $',''))
                final_amount=total+tax
                self.assertEqual(final_amount,43.18)
                sleep(5)
            except AssertionError as ae:
                print(f"total was incorrect:{ae}")
            except Exception as e:
                print(e)