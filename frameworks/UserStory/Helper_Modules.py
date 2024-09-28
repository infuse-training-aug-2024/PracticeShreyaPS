from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class HelperModules:
    WAIT_TIME = 10  # Define WAIT_TIME within the class if it's being referenced.

    def __init__(self, framework):
        self.framework = framework

    def login(self, url, username, password):
        """Helper method to log into the application."""
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

    def add_item_to_cart(self, item_id):
        """Helper method to add an item to the cart."""
        self.framework.click_element((By.ID, item_id))
        WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
        )

    def calculate_total(self):
        """Calculate total price of items in the cart."""
        item_in_cart = self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))
        total = sum(float(item.text.replace('$', '')) for item in item_in_cart)
        tax = float(self.framework.get_text((By.CLASS_NAME, 'summary_tax_label')).replace('Tax: $', ''))
        return total + tax

    # ---------------------for sorting--------------------------------------------------------

    def sort_items(self, sort_value):
        """Helper method to sort items by the specified value."""
        self.framework.click_element((By.CLASS_NAME, 'product_sort_container'))
        sort_dropdown = self.framework.get_element((By.CLASS_NAME, 'product_sort_container'))
        select = Select(sort_dropdown)
        select.select_by_value(sort_value)

        # Use framework.driver instead of self.driver
        WebDriverWait(self.framework.driver, self.WAIT_TIME).until(
            EC.visibility_of_element_located((By.ID, 'inventory_container'))
        )
        self.framework.is_element_visible((By.ID, 'inventory_container'))

    def get_inventory_items(self):
        """Helper method to retrieve inventory item names."""
        return [item.text for item in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_name'))]

    def get_inventory_prices(self):
        """Helper method to retrieve inventory item prices."""
        return [float(price.text.replace('$', '')) for price in self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))]
#---------------------------------for sidebar------------------------------------------


    def open_sidebar(self):
        """Helper method to open the sidebar menu."""
        self.framework.click_element((By.ID, 'react-burger-menu-btn'))

    def navigate_and_verify(self, menu_item_locator, expected_url, wait_time=10):
        """Helper method to navigate to a menu item and verify the URL."""
        self.open_sidebar()
        self.framework.click_element(menu_item_locator)
        WebDriverWait(self.framework.driver, wait_time).until(EC.url_to_be(expected_url))
        actual_url = self.framework.driver.current_url
        return actual_url  # Return the actual URL instead of asserting
