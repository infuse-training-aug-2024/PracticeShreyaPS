from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://demo.automationtesting.in/Register.html'
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)


driver.get(url)
try:
    wait = WebDriverWait(driver, 10)
    radio_button = wait.until(EC.element_to_be_clickable((By.NAME, 'radiooptions')))
    radio_button.click()
    wait = WebDriverWait(driver, 10)
    checkbox_button = wait.until(EC.element_to_be_clickable((By.ID, 'checkbox1')))
    checkbox_button.click()

except TimeoutError as e:
    print(f"timeout error:{e}")
finally:
    sleep(5)
    driver.quit()

