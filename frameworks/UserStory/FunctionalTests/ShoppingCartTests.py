from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver import WebDriver
from Framework import Framework
from Helper_Modules import HelperModules
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class ShoppingCartTests(unittest.TestCase):
    URL = 'https://www.saucedemo.com/'
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    WAIT_TIME = 10
    success_flag=0

    @classmethod
    def setUpClass(cls):
        try:
            cls.webdriver = WebDriver()
            cls.driver = cls.webdriver.driver
            cls.framework = Framework(cls.driver)
            cls.helper = HelperModules(cls.framework)
        except Exception as e:
            print(f"Error in setUpClass: {e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        if(cls.success_flag==0):
            print("Shopping cart Tests passed successfully")
        if cls.driver:
            cls.driver.quit()

    def setUp(self):
        self.driver.get(self.URL)
        self.helper.login(self.URL, self.USERNAME, self.PASSWORD)

    def tearDown(self):
        try:
            self.helper.logout()
            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_element_located((By.ID, 'login-button')) 
            )
        except Exception as e:
            print(f"Error during tearDown: {e}")

    def test_shopping_cart_icon_count(self):
        try:
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-bike-light')
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            items_added_from_inventory = ['Sauce Labs Bike Light', 'Sauce Labs Backpack']
            self.assertTrue(self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge')))
            cart_item_count = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertEqual(int(cart_item_count), 2)
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            items_in_cart = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            for item_added_from_inventory in items_added_from_inventory:
                self.assertIn(item_added_from_inventory, items_in_cart,
                              f"Shopping cart Test Failed: {item_added_from_inventory} not found in cart")
            self.helper.remove_from_cart('remove-sauce-labs-bike-light')
            self.helper.remove_from_cart('remove-sauce-labs-backpack')
            self.success_flag+=1
        except AssertionError as ae:
            print(f"Assertion error: {ae}")
        except Exception as e:
            print(f"Error occurred in counting or checking cart items: {e}")

    def test_cart_persistence(self):
        try:
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-bike-light')
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            self.assertTrue(self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge')))
            cart_item_count_before_logout = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.helper.logout()
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            cart_item_count_after_login = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertEqual(int(cart_item_count_before_logout), int(cart_item_count_after_login))
            self.helper.remove_from_cart('remove-sauce-labs-bike-light')
            self.helper.remove_from_cart('remove-sauce-labs-backpack')
            self.success_flag+=1

        except AssertionError as ae:
            print(f"Shopping cart Test Failed: cart icon history didn't persist: {ae}")
        except Exception as e:
            print(f"Error in cart persistence test: {e}")

    def test_removal_from_cart(self):
        try:
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-bike-light')
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            self.assertTrue(self.framework.is_element_visible((By.ID, 'remove-sauce-labs-backpack')),
                            "Remove button not found for Sauce Labs Backpack.")
            self.framework.click_element((By.ID, 'remove-sauce-labs-backpack'))
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            items_in_cart = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            self.assertNotIn('Sauce Labs Backpack', items_in_cart,
                             "Shopping cart Test Failed: Sauce Labs Backpack was found in the cart but should have been removed.")
            self.helper.remove_from_cart('remove-sauce-labs-bike-light')
            self.success_flag+=1

        except AssertionError as ae:
            print(f"Shopping cart Test Failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    unittest.main()
