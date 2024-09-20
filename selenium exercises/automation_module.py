# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.common.exceptions import WebDriverException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver import Chrome
# from time import sleep
# from selenium.webdriver.chrome.service import Service as chromeService
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains

# class AutomationModule():
#     def login(username_input,password_input,driver):
#         url = 'https://www.saucedemo.com/v1/'
#         username_id='user-name'
#         password_id='password'
#         login_id='login-button'
#         driver.get(url)
#         wait = WebDriverWait(driver, 10)
#         username = wait.until(EC.element_to_be_clickable((By.ID, username_id)))
#         username.send_keys(username_input)
#         wait = WebDriverWait(driver, 10)
#         password = wait.until(EC.element_to_be_clickable((By.ID, password_id)))
#         password.send_keys(password_input)
#         wait = WebDriverWait(driver, 10)
#         login = wait.until(EC.element_to_be_clickable((By.ID,login_id)))
#         login.click()

#     def scroll_up_down(driver):
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         driver.execute_script("window.scrollTo(0, 0);")

#     def see_dropdown(driver):
#         dropdown = driver.find_element(By.CLASS_NAME, 'product_sort_container')
#         select = Select(dropdown)
#         options = select.options
#         for option in options:
#             print(option.text)

#     def add_to_cart(driver,product_id):
#         wait = WebDriverWait(driver, 10)
#         add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH,product_id)))
#         add_to_cart.click()

#     def go_to_cart(driver):
#         cart_icon_class='.svg-inline--fa.fa-shopping-cart.fa-w-18.fa-3x'
#         wait = WebDriverWait(driver, 10)
#         add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,cart_icon_class)))
#         add_to_cart.click()

#     def checkout(driver):
#         checkout_id='.btn_action.checkout_button'
#         wait = WebDriverWait(driver, 10)
#         checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,checkout_id)))
#         checkout.click()

#     def continue_checkout(driver):
#         continue_id='.btn_primary.cart_button'
#         wait = WebDriverWait(driver, 10)
#         checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,continue_id)))
#         checkout.click()

#     def show_error_msg(driver,error):
#         error_element = driver.find_element(By.XPATH,error)
#         error_message = error_element.text
#         print(f"Error Message: {error_message}")

#     def try_drag_drop(driver):
#         image_id='inventory_item_img'
#         element=driver.find_element(By.CLASS_NAME, image_id)
#         action = ActionChains(driver)
#         action.drag_and_drop_by_offset(element, 200, 0).perform()



        
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
            # Use the nth-child selector to select the button for the specific item
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
        wait = WebDriverWait(self.driver, 15)  # Adjust the timeout as necessary
        
        element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, image_class)))

        
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, 200, 0).perform()


