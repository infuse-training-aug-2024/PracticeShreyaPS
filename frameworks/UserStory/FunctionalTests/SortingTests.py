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


class SortingTests(unittest.TestCase):
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
            cls.helper = HelperModules(cls.framework)

        except Exception as e:
            print(f"error in setup;{e}")
            cls.driver.quit()

    @classmethod
    def tearDownClass(cls):
        if(cls.success_flag==0):
            print("Sorting Tests passed successfully")
        cls.driver.quit()

    def test_sort_a_to_z(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.helper.sort_items('az')
            inventory_items = self.helper.get_inventory_items()
            sorted_inventory_items = sorted(inventory_items)
            self.assertEqual(inventory_items, sorted_inventory_items, "SortTest Failed:The items are not sorted in ascending order.")
            self.success_flag+=1
        # except AssertionError as ae:
        #     print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_z_to_a(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.helper.sort_items('za')
            inventory_items = self.helper.get_inventory_items()
            sorted_inventory_items_desc = sorted(inventory_items, reverse=True)
            self.assertEqual(inventory_items, sorted_inventory_items_desc, "SortTest Failed:The items are not sorted in descending order.")
            self.success_flag+=1
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_low_to_high(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.helper.sort_items('lohi')
            price_list = self.helper.get_inventory_prices()
            sorted_low_to_high_prices = sorted(price_list)
            self.assertEqual(price_list, sorted_low_to_high_prices, "SortTest Failed:The items are not sorted low to high by price")
            self.success_flag+=1
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def test_sort_high_to_low(self):
        try:
            self.helper.login(self.URL,self.USERNAME,self.PASSWORD)
            self.helper.sort_items('hilo')
            price_list = self.helper.get_inventory_prices()
            sorted_high_to_low_prices = sorted(price_list, reverse=True)
            self.assertEqual(price_list, sorted_high_to_low_prices, "SortTest Failed:The items are not sorted high to low by price")
            self.success_flag+=1
        except AssertionError as ae:
            print(f"Test failed: {ae}")
        except Exception as e:
            print(f"An error occurred: {e}")