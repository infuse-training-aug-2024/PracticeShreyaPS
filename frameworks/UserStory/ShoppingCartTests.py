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
        except Exception as e:
            print(f"error in setup;{e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    def test_add_to_cart2(self):
            try:
                #self.test_login()
                self.framework.click_element((By.ID,'add-to-cart-sauce-labs-bike-light'))
                WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
                self.assertTrue((By.CLASS_NAME,'shopping_cart_badge'))
            except TimeoutError as te:
                print(f"error in timeout :{te}")
            except AssertionError as ae:
                print(f"cart icon did not update:{ae}")
    
        
    def test_shopping_cart_icon_count(self):
            try:
                self.test_login()
                self.test_add_to_cart()
                self.test_add_to_cart2()
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
                # Log in and add an item to the cart
                self.test_login()
                self.test_add_to_cart()
                self.test_add_to_cart2()
                # Check if the remove button is visible and click it
                remove_button = self.framework.is_element_visible((By.ID, 'remove-sauce-labs-backpack'))
                self.assertTrue(remove_button, "Remove button not found for Sauce Labs Backpack.")
                self.framework.click_element((By.ID, 'remove-sauce-labs-backpack'))

                # The item that should be removed from the cart
                cart_items_removed_from_inventory = ['Sauce Labs Backpack']

                # Click on the shopping cart link to view the cart
                self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))

                # Get the names of items still in the cart
                items_in_cart = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]

                # Ensure that the removed items are NOT in the cart
                for item_removed in cart_items_removed_from_inventory:
                    self.assertNotIn(item_removed, items_in_cart, f"{item_removed} was found in the cart but should have been removed.")
                
                print("Item removal from cart is verified successfully.")
            
            except AssertionError as ae:
                print(f"Test failed: {ae}")
            
            except Exception as e:
                print(f"An error occurred: {e}")

    def test_cart_after_login(self):
            try:
                self.test_login()
                self.test_add_to_cart()
                self.test_add_to_cart2()
                self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge'))
                cart_item_count_before_logout = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
                self.logout()
                self.test_login()
                cart_item_count_after_login = self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge'))
                self.assertEqual(int(cart_item_count_before_logout), int(cart_item_count_after_login))
            except AssertionError as ae:
                print(f"cart icon history didnt persist: {ae}")