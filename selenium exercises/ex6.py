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
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

driver.get('https://letcode.in/forms')


try:
    dropdown = driver.find_element(By.TAG_NAME, 'select')
    select = Select(dropdown)
    options = select.options
    for option in options:
        print(option.text)

finally:
    sleep(5)
    driver.quit()

