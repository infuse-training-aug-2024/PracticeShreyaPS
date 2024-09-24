from automation_module import AutomationModule
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService
import tensorflow as tf


driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url = 'https://www.saucedemo.com/v1/'

chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

username='standard_user'
password='secret_sauce'

error_msg_id='//*[@id="checkout_info_container"]/div/form/h3'


try:
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://www.saucedemo.com/v1/'
    automate=AutomationModule(driver_path, url)
    automate.login(username,password)
    automate.scroll_up_down()
    automate.see_dropdown()
    automate.add_to_cart([1, 2])
    automate.go_to_cart()
    automate.checkout()
    automate.continue_checkout()
    driver.back()
    driver.back()
    # automate.try_drag_drop()


except TimeoutError as e:
    print(f"timeout error occurred :{e}")
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")

finally:
    sleep(5)
    driver.quit()