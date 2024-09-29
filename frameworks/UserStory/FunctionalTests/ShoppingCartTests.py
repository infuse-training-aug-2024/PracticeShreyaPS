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
from Helper_Modules import HelperModules
from selenium.common.exceptions import StaleElementReferenceException


class ShoppingCartTests(unittest.TestCase):
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
            cls.helper = HelperModules(cls.framework)
        except Exception as e:
            print(f"error in setup;{e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  
        
    def test_add_product_to_cart(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            item_id = 'add-to-cart-sauce-labs-backpack'
            result = self.helper.add_item_to_cart(item_id)
            self.assertTrue(
                result,
                f"Cart badge did not appear after adding item with ID '{item_id}'"
            )
        except AssertionError:
            print("product 1 could not be added")

    def test_add_product2_to_cart(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            item_id = 'add-to-cart-sauce-labs-bike-light'
            result = self.helper.add_item_to_cart(item_id)
            # Assert that the cart badge is visible
            self.assertTrue(
                result,
                f"Cart badge did not appear after adding item with ID '{item_id}'"
            )
        except AssertionError:
            print("product 1 could not be added")
 
    def test_shopping_cart_icon_count(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.test_add_product_to_cart()
            self.test_add_product2_to_cart()
            items_added_from_inventory=['Sauce Labs Bike Light','Sauce Labs Backpack']
            self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge'))
            cart_item_count = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertEqual(int(cart_item_count), 2)
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            items_in_cart = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            for item_added_from_inventory in items_added_from_inventory:
                self.assertIn(item_added_from_inventory, items_in_cart, f"{item_added_from_inventory} not found in cart")
            
            print("All items from inventory are correctly present in the cart.")
        
        except AssertionError as ae:
            print(f"Assertion error: {ae}")
        except Exception as e:
            print(f"Error occurred in counting or checking cart items: {e}")

    def test_removal_from_cart(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.test_add_product_to_cart()
            self.test_add_product2_to_cart()
            remove_button = self.framework.is_element_visible((By.ID, 'remove-sauce-labs-backpack'))
            self.assertTrue(remove_button, "Remove button not found for Sauce Labs Backpack.")
            self.framework.click_element((By.ID, 'remove-sauce-labs-backpack'))
            cart_items_removed_from_inventory = ['Sauce Labs Backpack']
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            items_in_cart = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            for item_removed in cart_items_removed_from_inventory:
                self.assertNotIn(item_removed, items_in_cart, f"{item_removed} was found in the cart but should have been removed.")
            print("Item removal from cart is verified successfully.")
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_cart_persistance(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.test_add_product_to_cart()
            self.test_add_product2_to_cart()
            self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge'))
            cart_item_count_before_logout = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.helper.logout()
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            cart_item_count_after_login = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertEqual(int(cart_item_count_before_logout), int(cart_item_count_after_login))
        except AssertionError as ae:
            print(f"cart icon history didnt persist: {ae}")
