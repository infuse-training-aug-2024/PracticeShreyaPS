from login_module import LoginModule
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url = 'https://www.saucedemo.com/v1/'
username_input_id='user-name'
password_input_id='password'
login_id='login-button'

chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

try:
    
    LoginModule.login(username_input_id,password_input_id,login_id,url)
    cart_icon_id=".svg-inline--fa.fa-shopping-cart.fa-w-18.fa-3x" 
    wait = WebDriverWait(driver, 10)
    cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,cart_icon_id)))
    cart_icon.click()
except TimeoutError as e:
    print(f"timeout error occurred :{e}")
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")

finally:
    sleep(5)
    driver.quit()