from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://www.google.com/'
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)
try:
    driver.implicitly_wait(10.0)
    driver.get(url)
    driver.maximize_window()
    sleep(5.0)
    

except TimeoutError as e:
    print(f"Timeout error occured: {e}")
finally:

    driver.quit()
