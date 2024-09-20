# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver import Chrome, Edge
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.edge.service import Service as EdgeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver

# def setup_driver(browser_name, driver_path):
#     if browser_name == "chrome":
#         service = ChromeService(executable_path=driver_path)
#         driver = Chrome(service=service)
#     elif browser_name == "edge":
#         service = EdgeService(executable_path=driver_path)
#         driver = Edge(service=service)
#     elif browser_name == "firefox":
#         service = FirefoxService(executable_path=driver_path)
#         options = Options()
#         options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Adjust this to the path of your Firefox binary
#         driver = webdriver.Firefox(service=service, options=options)
#     else:
#         raise ValueError(f"Unsupported browser: {browser_name}")
#     return driver

# def test_browser(driver,  browser_name, first_rectangle_id, second_shape_id):
#     url = 'https://joyrel-vaz.github.io/cross-browser-testing/'
#     driver.get(url)
#     wait = WebDriverWait(driver, 20)
    
#     # Check browser name match
#     first_rectangle = wait.until(EC.presence_of_element_located((By.ID, first_rectangle_id)))
#     if browser_name in first_rectangle.text.lower():
#         print(f"{browser_name} browser name matches\n")
#     else:
#         print(f"{browser_name} does not match")

#     # Check automation ID
#     second_shape = wait.until(EC.presence_of_element_located((By.ID, second_shape_id)))
#     automation_id = second_shape.get_attribute("automation-id")
#     print(f"Automation ID: {automation_id}")

# def main():
    
#     url = 'https://joyrel-vaz.github.io/cross-browser-testing/'
#     # Test Chrome
#     chrome_driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
#     chrome_driver = setup_driver("chrome", chrome_driver_path)
#     try:
#         test_browser(chrome_driver, "chrome", "js-test", "chrome")
#     finally:
#         chrome_driver.quit()

#     # Test Edge
#     edge_driver_path = "C:/Users/91989/Downloads/driver/msedgedriver.exe"
#     edge_driver = setup_driver("edge", edge_driver_path)
#     try:
#         test_browser(edge_driver, "edge", "js-test", "edge")
#     finally:
#         edge_driver.quit()

#     # Test Firefox
#     firefox_driver_path = "C:/Users/91989/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe"
#     firefox_driver = setup_driver("firefox", firefox_driver_path)
#     try:
#         test_browser(firefox_driver, "firefox", "js-test", "ff")
#     finally:
#         firefox_driver.quit()

# if __name__ == "__main__":
#     main()


from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Define a mapping for the element IDs based on browser names
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
        options.binary_location = "C:/Program Files/Mozilla Firefox/firefox.exe"  # Adjust this to the path of your Firefox binary
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

    # Retrieve the correct element IDs for the browser
    first_rectangle_id = element_ids[browser_name]["first_rectangle_id"]
    second_shape_id = element_ids[browser_name]["second_shape_id"]

    try:
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

    finally:
        driver.quit()

def main():
    # Test Chrome, Edge, and Firefox
    browsers = ["chrome", "edge", "firefox"]
    for browser in browsers:
        test_browser(browser)

if __name__ == "__main__":
    main()
