from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.support.ui import Select

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://letcode.in/forms'
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

try:
    driver.get(url)
    driver.implicitly_wait(5)
    dropdown = driver.find_element(By.TAG_NAME, 'select')
    select = Select(dropdown)
    options = select.options
    for option in options:
        print(option.text)
except TimeoutError as e:
    print(f"timeout error:{e}")
finally:
    driver.quit()

