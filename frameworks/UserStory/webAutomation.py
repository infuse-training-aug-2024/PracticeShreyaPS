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
            login_credentials={"user-name":"standard_user","password":"secret_sauce"}
            self.framework.fill_form(login_credentials)
            self.framework.submit_form((By.TAG_NAME,'form'))
            WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_all_elements_located((By.ID,'inventory_container')))
            self.assertEqual(self.framework.get_current_url(),self.driver.current_url)
            sleep(5)
        except AssertionError as ae:
            print(f"error in navigating:{ae}")
        except Exception as e:
            print(f"fill form error occured:{e}")

    def logout(self):
        self.framework.click_element((By.ID,'react-burger-menu-btn'))
        self.framework.click_element((By.ID,'logout_sidebar_link'))

    def test_add_to_cart(self):
        try:
            #self.test_login()
            self.framework.click_element((By.ID,'add-to-cart-sauce-labs-backpack'))
            WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
            self.assertTrue((By.CLASS_NAME,'shopping_cart_badge'))
        except TimeoutError as te:
            print(f"error in timeout :{te}")
        except AssertionError as ae:
            print(f"cart icon did not update:{ae}")

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

    def test_sort_a_to_z(self):
        try:
            self.test_login()
            self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
            selected_sort_option = self.framework.select_option_by_value((By.CLASS_NAME, 'product_sort_container'), 'az')
            self.assertEqual(selected_sort_option, 'Name (A to Z)', "The selected sort option is incorrect.")
            inventory_items = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            print(f"Items in inventory after sorting: {inventory_items}")
            sorted_inventory_items = sorted(inventory_items)
            print(f"Sorted inventory items: {sorted_inventory_items}")
            self.assertEqual(inventory_items, sorted_inventory_items, "The items are not sorted in ascending order.")
            print("The items are correctly sorted in ascending order.")
        
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_z_to_a(self):
        try:
            self.test_login()
            self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
            sort_dropdown = self.framework.get_element((By.CLASS_NAME, 'product_sort_container'))
            select = Select(sort_dropdown)
            select.select_by_value('za')
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'inventory_container'))
            )
            self.framework.is_element_visible((By.ID, 'inventory_container'))
            inventory_items = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
            print(f"Items in inventory after sorting: {inventory_items}")
            sorted_inventory_items_desc = sorted(inventory_items, reverse=True)
            print(f"Expected sorted inventory items (Z to A): {sorted_inventory_items_desc}")
            self.assertEqual(inventory_items, sorted_inventory_items_desc, "The items are not sorted in descending order.")
            print("The items are correctly sorted in descending order (Z to A).")
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_low_to_high(self):
        try:
            self.test_login()
            self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
            sort_dropdown = self.framework.get_element((By.CLASS_NAME, 'product_sort_container'))
            select = Select(sort_dropdown)
            select.select_by_value('lohi')
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'inventory_container'))
            )
            self.framework.is_element_visible((By.ID, 'inventory_container'))
            inventory_items = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))]
            price_list = [float(price.replace('$', '')) for price in inventory_items]
            print(f"Items in inventory after sorting: {price_list}")
            sorted_low_to_high_prices = sorted(price_list)
            print(f"Expected sorted inventory items (low to high): {sorted_low_to_high_prices}")
            self.assertEqual(price_list, sorted_low_to_high_prices, "The items are not sorted.")
            print("The items are correctly sorted ")
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_high_to_low(self):
        try:
            self.test_login()
            self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
            sort_dropdown = self.framework.get_element((By.CLASS_NAME, 'product_sort_container'))
            select = Select(sort_dropdown)
            select.select_by_value('hilo')
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, 'inventory_container'))
            )
            self.framework.is_element_visible((By.ID, 'inventory_container'))
            inventory_items = [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))]
            price_list = [float(price.replace('$', '')) for price in inventory_items]
            print(f"Items in inventory after sorting: {price_list}")
            sorted_high_to_low_prices = sorted(price_list,reverse=True)
            print(f"Expected sorted inventory items (low to high): {sorted_high_to_low_prices}")
            self.assertEqual(price_list, sorted_high_to_low_prices, "The items are not sorted.")
            print("The items are correctly sorted ")
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")


    def test_nav_to_home(self):
        try:
            self.test_login()
            self.framework.click_element((By.ID,'react-burger-menu-btn'))
            self.framework.click_element((By.ID,'inventory_sidebar_link'))
            WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_all_elements_located((By.ID,'inventory_container')))
            expected_url = "https://www.saucedemo.com/inventory.html"
            actual_url = self.driver.current_url
            self.assertEqual(expected_url, actual_url, f"Expected URL: {expected_url}, but got: {actual_url}")
        except AssertionError as ae:
            print("page did not redirect to home")

        except Exception as e:
            print(f"error occured:{e}")

    def test_nav_to_about(self):
        try:
            self.test_login()
            self.framework.click_element((By.ID,'react-burger-menu-btn'))
            self.framework.click_element((By.ID,'about_sidebar_link'))
            WebDriverWait(self.driver, self.WAIT_TIME).until(EC.url_to_be("https://saucelabs.com/"))
            expected_url = "https://saucelabs.com/"
            actual_url = self.driver.current_url
            self.assertEqual(expected_url, actual_url, f"Expected URL: {expected_url}, but got: {actual_url}")
        except AssertionError as ae:
            print("page did not redirect to about")


            
    def test_nav_to_logout(self):
        try:
            self.test_login()
            self.logout()
            expected_url = "https://www.saucedemo.com/"
            actual_url = self.driver.current_url
            self.assertEqual(expected_url, actual_url, f"Expected URL: {expected_url}, but got: {actual_url}")
        except AssertionError as ae:
            print("page did not redirect to logout")

    def test_reset(self):
        try:
            self.test_login()
            self.test_add_to_cart()
            self.framework.click_element((By.ID,'react-burger-menu-btn'))
            self.framework.click_element((By.ID,'reset_sidebar_link'))
            WebDriverWait(self.driver,self.WAIT_TIME).until(EC.visibility_of_all_elements_located((By.ID,'inventory_container')))
            shopping_badge=self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertFalse(shopping_badge)
            remove_buttons=self.framework.get_element((By.ID,'remove-sauce-labs-backpack'))
            self.assertIsNone(remove_buttons)
        except AssertionError as ae:
            print("page did not reset")

        except Exception as e:
            print(f"error occured:{e}")            


    def test_invalid_login(self):
        try:
            self.framework.navigate_to_page(self.URL)
            
            login_credentials={"user-name":"invalid","password":"invalid"}
            self.framework.fill_form(login_credentials)
            self.framework.submit_form((By.TAG_NAME,'form'))
            error_msg=self.framework.is_element_visible((By.CLASS_NAME,'error-message-container'))
            self.assertTrue(error_msg)
        except AssertionError as ae:
            print(f"error msg did not load")

    def test_navigate_to_invalid_login(self):
        try:
            self.test_login()
            self.logout()
            self.driver.back()
            self.assertEqual(self.framework.get_current_url(),self.URL)
        except AssertionError as ae:
            print(f"invalid navigation to login allowed")


# if __name__ == "__main__":
#    unittest.main()
if __name__ == "__main__":
   login_test = TestSauceDemo()
   TestSauceDemo.setUpClass()  # Call setUpClass manually
   login_test.test_navigate_to_invalid_login()
   TestSauceDemo.tearDownClass()  # Make sure to clean up
