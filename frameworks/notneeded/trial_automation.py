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
from Helper_Modules import HelperModules  # Import the helper class

class TestSauceDemo(unittest.TestCase):
    URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    WAIT_TIME = 10

    @classmethod
    def setUpClass(cls):
        cls.webdriver = WebDriver()
        cls.driver = cls.webdriver.driver
        cls.framework = Framework(cls.driver)
        cls.helper = HelperModules(cls.framework)  # Instantiate the helper class

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login(self):
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            self.assertEqual(self.framework.get_current_url(), self.driver.current_url)
        except Exception as e:
            print(f"Error in logging in: {e}")

    def test_add_to_cart(self):
        try:
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed())
        except Exception as e:
            print(f"Error in adding to cart: {e}")

    def test_add_to_cart2(self):
        try:
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-bike-light')
            self.assertTrue(self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').is_displayed())
        except Exception as e:
            print(f"Error in adding to cart: {e}")

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
        except Exception as e:
            print(f"Error in billing: {e}")

# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
   login_test = TestSauceDemo()
   TestSauceDemo.setUpClass()  # Call setUpClass manually
   login_test.test_billing()
   TestSauceDemo.tearDownClass()  # Make sure to clean up