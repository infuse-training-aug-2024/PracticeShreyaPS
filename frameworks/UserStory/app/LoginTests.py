import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/inventory.html")

    def test_invalid_login(self):
        driver = self.driver
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("invalid_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("wrong_password")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container'))
        )
        self.assertIn("Epic sadface: Username and password do not match any user", error_message.text)


class LogoutTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("https://www.saucedemo.com/")
        # Perform login first to access the logout functionality
        username_input = self.driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))

    def tearDown(self):
        self.driver.quit()

    def test_logout(self):
        driver = self.driver
        menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_link.click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://www.saucedemo.com/"))
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/")

if __name__ == "__main__":
    unittest.main()
