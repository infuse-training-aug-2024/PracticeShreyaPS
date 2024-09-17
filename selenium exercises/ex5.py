from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)


driver.get('https://www.yahoo.com/')
try:
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-sbq')))
    search_input.click()
    wait = WebDriverWait(driver, 10)
    search_input = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-sbq')))
    search_input.send_keys("selenium")
    wait = WebDriverWait(driver, 10)
    search_icon = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-search')))
    search_icon.click()
finally:
    sleep(5)
    driver.quit()