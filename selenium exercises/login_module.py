from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

class LoginModule():
    def login(username,password,login_button,url):
        driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
        chrome_service = chromeService(executable_path=driver_path)
        driver=Chrome(service=chrome_service)
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
