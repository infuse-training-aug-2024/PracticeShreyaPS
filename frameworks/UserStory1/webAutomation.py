from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

# Quit WebDriver
def teardown_driver(driver):
    driver.quit()

def test_open_google(driver):
    driver.get("https://www.google.com")
    time.sleep(3)  # Let the page load
    assert "Google" in driver.title

def test_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()
    time.sleep(3)  # Wait for search results to load
    assert "Selenium WebDriver" in driver.page_source

def test_direct_login(driver):
    try:
        driver.get("https://www.saucedemo.com/")
        expected_url="https://www.saucedemo.com/inventory.html"
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        wait = WebDriverWait(driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()
        assert driver.current_url == expected_url, f"Failed to navigate. Expected URL: {expected_url}, but got: {driver.current_url}"
    except AssertionError as ae:
        print(f"Failed to navigate. Expected URL: {expected_url}, but got: {driver.current_url}")

def test_incorrect_login(driver):
        driver.get("https://www.saucedemo.com/")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("locked_out_user")
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        wait = WebDriverWait(driver, 10)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
        login_button.click()


def test_blank_login(driver):
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    login_button = wait.until(EC.element_to_be_clickable((By.ID, 'login-button')))
    login_button.click()
    element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container')))

    # Assert that the element is present
    assert element is not None, "Error message container is not visible on the page!"

    # Optionally, assert the text content of the error message
    expected_error_text = "Your expected error message"
    assert expected_error_text in element.text, f"Expected '{expected_error_text}', but got '{element.text}'"
    pass

def test_invalid_login(driver):
    pass

def run_tests():
    driver = setup_driver()
    try:
        username_list=[""]
        test_direct_login(driver)
        test_blank_login(driver)
    #     test_open_google(driver)
    #     test_search(driver)
    finally:
        teardown_driver(driver)

if __name__ == "__main__":
    run_tests()
