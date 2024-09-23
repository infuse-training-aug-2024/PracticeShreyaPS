from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class AutomationModule():
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=self.chrome_service)

    def login(self, username_input, password_input):
        username_id = 'user-name'
        password_id = 'password'
        login_id = 'login-button'
        self.driver.get(self.url)
        wait = WebDriverWait(self.driver, 10)
        
        username = wait.until(EC.element_to_be_clickable((By.ID, username_id)))
        username.send_keys(username_input)
        
        password = wait.until(EC.element_to_be_clickable((By.ID, password_id)))
        password.send_keys(password_input)
        
        login_button = wait.until(EC.element_to_be_clickable((By.ID, login_id)))
        login_button.click()

    def scroll_up_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(0, 0);")

    def see_dropdown(self):
        dropdown = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        select = Select(dropdown)
        options = select.options
        for option in options:
            print(option.text)

    def add_to_cart(self, product_indices):
        for index in product_indices:
            product_selector = f".inventory_item:nth-child({index}) .btn_primary.btn_inventory"
            wait = WebDriverWait(self.driver, 10)
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, product_selector)))
            add_to_cart_button.click()

    def go_to_cart(self):
        cart_icon_id = 'shopping_cart_container'
        wait = WebDriverWait(self.driver, 10)
        cart_icon = wait.until(EC.element_to_be_clickable((By.ID, cart_icon_id)))
        cart_icon.click()

    def checkout(self):
        checkout_id = '.btn_action.checkout_button'
        wait = WebDriverWait(self.driver, 10)
        checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, checkout_id)))
        checkout_button.click()

    def continue_checkout(self):
        continue_id = '.btn_primary.cart_button'
        wait = WebDriverWait(self.driver, 10)
        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, continue_id)))
        continue_button.click()

    def show_error_msg(self, error_xpath):
        error_element = self.driver.find_element(By.XPATH, error_xpath)
        error_message = error_element.text
        print(f"Error Message: {error_message}")

    def try_drag_drop(self):
        image_class = 'inventory_item_img'
        wait = WebDriverWait(self.driver, 15) 
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, image_class)))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, 200, 0).perform()


