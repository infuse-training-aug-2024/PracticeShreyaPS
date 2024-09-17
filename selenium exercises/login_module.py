from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class LoginModule():
    def login(username,password,login_button,url,driver):
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.element_to_be_clickable((By.ID, username)))
        username.send_keys("standard_user")
        wait = WebDriverWait(driver, 10)
        password = wait.until(EC.element_to_be_clickable((By.ID, password)))
        password.send_keys("secret_sauce")
        wait = WebDriverWait(driver, 10)
        login = wait.until(EC.element_to_be_clickable((By.ID,login_button)))
        login.click()

    def scroll_up_down(driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, 0);")

    def see_dropdown(driver):
        dropdown = driver.find_element(By.CLASS_NAME, 'product_sort_container')
        select = Select(dropdown)
        options = select.options
        for option in options:
            print(option.text)

    def add_to_cart(driver,product_id):
        wait = WebDriverWait(driver, 10)
        add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH,product_id)))
        add_to_cart.click()

    def go_to_cart(driver,cart_id):
        wait = WebDriverWait(driver, 10)
        add_to_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,cart_id)))
        add_to_cart.click()

    def checkout(driver,checkout_id):
        wait = WebDriverWait(driver, 10)
        checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,checkout_id)))
        checkout.click()

    def continue_checkout(driver,continue_id):
        wait = WebDriverWait(driver, 10)
        checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,continue_id)))
        checkout.click()

    def show_error_msg(driver,error):
        error_element = driver.find_element(By.XPATH,error)
        error_message = error_element.text
        print(f"Error Message: {error_message}")

    def try_drag_drop(driver,img_id):
        element=driver.find_element(By.CLASS_NAME, img_id)
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(element, 200, 0).perform()



        
