from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

element_ids = {
    "chrome": {"first_rectangle_id": "js-test", "second_shape_id": "chrome"},
    "edge": {"first_rectangle_id": "js-test", "second_shape_id": "edge"},
    "firefox": {"first_rectangle_id": "js-test", "second_shape_id": "ff"},
}

def setup_driver(browser_name, driver_path):
    if browser_name == "chrome":
        service = ChromeService(executable_path=driver_path)
        driver = Chrome(service=service)
    elif browser_name == "edge":
        service = EdgeService(executable_path=driver_path)
        driver = Edge(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path=driver_path)
        options = Options()
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe" 
        driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    return driver

def test_browser(browser_name):
    driver_paths = {
        "chrome": "C:/Users/91989/Downloads/driver/chromedriver.exe",
        "edge": "C:/Users/91989/Downloads/driver/msedgedriver.exe",
        "firefox": "C:/Users/91989/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe"
    }
    
    driver_path = driver_paths[browser_name]
    driver = setup_driver(browser_name, driver_path)
    url = 'https://joyrel-vaz.github.io/cross-browser-testing/'
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    first_rectangle_id = element_ids[browser_name]["first_rectangle_id"]
    second_shape_id = element_ids[browser_name]["second_shape_id"]

    try:
        first_rectangle = wait.until(EC.presence_of_element_located((By.ID, first_rectangle_id)))
        if browser_name in first_rectangle.text.lower():
            print(f"{browser_name} browser name matches\n")
        else:
            print(f"{browser_name} does not match")

        second_shape = wait.until(EC.presence_of_element_located((By.ID, second_shape_id)))
        automation_id = second_shape.get_attribute("automation-id")
        print(f"Automation ID: {automation_id}")

    finally:
        driver.quit()

def main():
    browsers = ["chrome", "edge", "firefox"]
    for browser in browsers:
        test_browser(browser)

if __name__ == "__main__":
    main()
