

from selenium.webdriver import Chrome, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def setup_driver(browser_name, driver_path):
    if browser_name == "chrome":
        service = ChromeService(executable_path=driver_path)
        driver = Chrome(service=service)
    elif browser_name == "edge":
        service = EdgeService(executable_path=driver_path)
        driver = Edge(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path=driver_path)
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    return driver

def test_browser(driver, url, browser_name, first_rectangle_id, second_shape_id):
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    
    # Check browser name match
    first_rectangle = wait.until(EC.presence_of_element_located((By.ID, first_rectangle_id)))
    if browser_name in first_rectangle.text.lower():
        print(f"{browser_name} browser name matches\n")
    else:
        print(f"{browser_name} does not match")

    # Check automation ID
    second_shape = wait.until(EC.presence_of_element_located((By.ID, second_shape_id)))
    automation_id = second_shape.get_attribute("automation-id")
    print(f"Automation ID: {automation_id}")

def main():
    url = 'https://joyrel-vaz.github.io/cross-browser-testing/'

    # Test Chrome
    chrome_driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    chrome_driver = setup_driver("chrome", chrome_driver_path)
    try:
        test_browser(chrome_driver, url, "chrome", "js-test", "chrome")
    finally:
        chrome_driver.quit()

    # Test Edge
    edge_driver_path = "C:/Users/91989/Downloads/driver/msedgedriver.exe"
    edge_driver = setup_driver("edge", edge_driver_path)
    try:
        test_browser(edge_driver, url, "edge", "js-test", "edge")
    finally:
        edge_driver.quit()

    # Test Firefox
    firefox_driver_path = "C:/Users/91989/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe"
    firefox_driver = setup_driver("firefox", firefox_driver_path)
    try:
        test_browser(firefox_driver, url, "firefox", "js-test", "ff")
    finally:
        firefox_driver.quit()

if __name__ == "__main__":
    main()
