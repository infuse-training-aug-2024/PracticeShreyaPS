from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
class HelperModules:
    WAIT_TIME = 10 

    def __init__(self, framework):
        self.framework = framework

    def login(self, url, username, password):
        self.framework.navigate_to_page(url)
        login_credentials = {"user-name": username, "password": password}
        self.framework.fill_form(login_credentials)
        self.framework.submit_form((By.TAG_NAME, 'form'))
        WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
            EC.visibility_of_all_elements_located((By.ID, 'inventory_container'))
        )

    def logout(self):
        self.framework.click_element((By.ID,'react-burger-menu-btn'))
        self.framework.click_element((By.ID,'logout_sidebar_link'))

    def calculate_total(self):
        item_in_cart = self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))
        total = sum(float(item.text.replace('$', '')) for item in item_in_cart)
        tax = float(self.framework.get_text((By.CLASS_NAME, 'summary_tax_label')).replace('Tax: $', ''))
        return total + tax

    def sort_items(self, sort_value):
        self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
        sort_dropdown = self.framework.get_element((By.CLASS_NAME, 'product_sort_container'))
        select = Select(sort_dropdown)
        select.select_by_value(sort_value)
        WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, 'inventory_container'))
        )
        self.framework.is_element_visible((By.ID, 'inventory_container'))

    def get_inventory_items(self):
        return [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]

    def get_inventory_prices(self):
        return [float(price.text.replace('$', '')) for price in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))]

    def open_sidebar(self):
        self.framework.click_element((By.ID, 'react-burger-menu-btn'))

    def navigate_and_verify(self, menu_item_locator, expected_url, wait_time=10):
        self.open_sidebar()
        self.framework.click_element(menu_item_locator)
        WebDriverWait(self.framework.driver, wait_time).until(EC.url_to_be(expected_url))
        actual_url = self.framework.driver.current_url
        return actual_url  

    def remove_from_cart(self, item_id):
        self.framework.click_element((By.ID, item_id))

    def get_cart_item_count(self):
        return int(self.framework.get_text((By.CLASS_NAME, 'shopping_cart_badge')))

    def get_cart_items(self):
        self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
        return [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]
    
    def test_add_to_cart(self):
        try:
            self.framework.click_element((By.ID,'add-to-cart-sauce-labs-backpack'))
            WebDriverWait(self.framework.driver,self.WAIT_TIME).until(
                EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
            self.assertTrue((By.CLASS_NAME,'shopping_cart_badge'))
        except TimeoutError as te:
            print(f"error in timeout :{te}")
        except AssertionError as ae:
            print(f"cart icon did not update:{ae}")

    def test_add_to_cart2(self):
        try:
            self.framework.click_element((By.ID,'add-to-cart-sauce-labs-bike-light'))
            WebDriverWait(self.framework.driver,self.WAIT_TIME).until(
                EC.visibility_of_element_located((By.CLASS_NAME,'shopping_cart_badge')))
            self.assertTrue((By.CLASS_NAME,'shopping_cart_badge'))
        except TimeoutError as te:
            print(f"error in timeout :{te}")
        except AssertionError as ae:
            print(f"cart icon did not update:{ae}")

    def add_item_to_cart(self, item_id):
        retries = 3 
        for attempt in range(retries):
            try:
                WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
                    EC.element_to_be_clickable((By.ID, item_id))
                )
                element = self.framework.get_element((By.ID, item_id))
                element.click()
                WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
                )
                return True 
            except StaleElementReferenceException:
                print(f"StaleElementReferenceException: Attempt {attempt + 1} of {retries}")
                if attempt < retries - 1:
                    continue  
            except TimeoutException:
                print(f"TimeoutException: Element with ID {item_id} was not clickable in {self.WAIT_TIME} seconds.")
                return False
            except Exception as e:
                print(f"Error adding item to cart: {e}")
                return False
        
        return False  

    def remove_item_from_cart(self, item_id):
            self.framework.click_element((By.CLASS_NAME, 'shopping_cart_link'))
            WebDriverWait(self.framework.driver, self.framework.WAIT_TIME).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'cart_item'))
            )
            try:
                remove_button = self.framework.get_element(By.ID, item_id)
                remove_button.click()
            except Exception as e:
                print(f"Error removing item with ID {item_id}: {e}")