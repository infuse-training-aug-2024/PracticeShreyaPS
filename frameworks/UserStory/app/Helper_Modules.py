from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HelperModules:
    def __init__(self, framework):
        self.framework = framework

    def login(self, url, username, password):
        """Helper method to log into the application."""
        self.framework.navigate_to_page(url)
        login_credentials = {"user-name": username, "password": password}
        self.framework.fill_form(login_credentials)
        self.framework.submit_form((By.TAG_NAME, 'form'))
        WebDriverWait(self.framework.driver, 10).until(
            EC.visibility_of_all_elements_located((By.ID, 'inventory_container'))
        )

    def add_item_to_cart(self, item_id):
        """Helper method to add an item to the cart."""
        self.framework.click_element((By.ID, item_id))
        WebDriverWait(self.framework.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'shopping_cart_badge'))
        )

    def calculate_total(self):
        """Calculate total price of items in the cart."""
        item_in_cart = self.framework.get_elements((By.CLASS_NAME, 'inventory_item_price'))
        total = sum(float(item.text.replace('$', '')) for item in item_in_cart)
        tax = float(self.framework.get_text((By.CLASS_NAME, 'summary_tax_label')).replace('Tax: $', ''))
        return total + tax
