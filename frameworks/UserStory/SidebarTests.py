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

class SidebarTests(unittest.TestCase):
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
        
    def test_nav_to_home(self):
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            actual_url = self.helper.navigate_and_verify((By.ID, 'inventory_sidebar_link'), "https://www.saucedemo.com/inventory.html")
            self.assertEqual("https://www.saucedemo.com/inventory.html", actual_url, f"Expected URL: https://www.saucedemo.com/inventory.html, but got: {actual_url}")
        except AssertionError as ae:
            print("Page did not redirect to home.")
        except Exception as e:
            print(f"Error occurred: {e}")


    def test_nav_to_about(self):
        """Test sidebar navigation to about page."""
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            self.helper.navigate_and_verify((By.ID, 'about_sidebar_link'), "https://saucelabs.com/")
        except AssertionError:
            print("Page did not redirect to about.")
        except Exception as e:
            print(f"Error occurred: {e}")

    def test_nav_to_logout(self):
        """Test sidebar navigation to logout."""
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            self.helper.logout()
            actual_url = self.driver.current_url
            self.assertEqual(self.URL, actual_url, f"Expected URL: {self.URL}, but got: {actual_url}")
        except AssertionError:
            print("Page did not redirect to logout.")
        except Exception as e:
            print(f"Error occurred: {e}")

    def test_reset(self):
        """Test sidebar reset functionality."""
        try:
            self.helper.login(self.URL, self.USERNAME, self.PASSWORD)
            self.helper.add_item_to_cart('add-to-cart-sauce-labs-backpack')
            self.helper.open_sidebar()
            self.framework.click_element((By.ID, 'reset_sidebar_link'))

            WebDriverWait(self.driver, self.WAIT_TIME).until(
                EC.visibility_of_all_elements_located((By.ID, 'inventory_container'))
            )

            shopping_badge = self.framework.is_element_visible((By.CLASS_NAME, 'shopping_cart_badge'))
            self.assertFalse(shopping_badge)

            remove_button = self.framework.get_element((By.ID, 'remove-sauce-labs-backpack'))
            self.assertIsNone(remove_button)
        except AssertionError:
            print("Page did not reset.")
        except Exception as e:
            print(f"Error occurred: {e}")