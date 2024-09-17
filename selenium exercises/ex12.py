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

chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

username_id='user-name'
password_id='password'
login_id='login-button'
product1_id='//*[@id="inventory_container"]/div/div[1]/div[3]/button'
product2_id='//*[@id="inventory_container"]/div/div[2]/div[3]/button'
cart_icon_id='.svg-inline--fa.fa-shopping-cart.fa-w-18.fa-3x'
checkout_id='.btn_action.checkout_button'
continue_id='.btn_primary.cart_button'
error_msg_id='//*[@id="checkout_info_container"]/div/form/h3'
image_id='inventory_item_img'

try:
    LoginModule.login(username_id,password_id,login_id,url,driver)
    LoginModule.scroll_up_down(driver)
    LoginModule.see_dropdown(driver)
    LoginModule.add_to_cart(driver,product1_id)
    LoginModule.add_to_cart(driver,product2_id)
    LoginModule.go_to_cart(driver,cart_icon_id)
    LoginModule.checkout(driver,checkout_id)
    LoginModule.continue_checkout(driver,continue_id)
    driver.back()
    driver.back()
    LoginModule.try_drag_drop(driver,image_id)


except TimeoutError as e:
    print(f"timeout error occurred :{e}")
except WebDriverException as e:
    print(f"WebDriverException occurred: {e}")

finally:
    sleep(5)
    driver.quit()