from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.service import Service as firefoxService

driver_path = "C:/Users/91989/Downloads/driver/geckodriver.exe"
url = 'https://www.saucedemo.com/v1/'

firefox_service = firefoxService(executable_path=driver_path)
driver = Firefox(service=firefox_service)

try:
    driver.get(url)
    
except TimeoutError as e:
    print(f"timeout error occurred :{e}")
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")

finally:
    driver.quit()