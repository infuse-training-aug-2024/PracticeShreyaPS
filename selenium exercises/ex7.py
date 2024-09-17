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
url='https://testpages.herokuapp.com/styled/basic-html-form-test.html'
ith_index='dd4'

chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

driver.get(url)


try:
    driver.implicitly_wait(5)
    dropdown = driver.find_element(By.NAME, 'dropdown')
    select = Select(dropdown)
    select.select_by_value(ith_index)
    selected_option = select.first_selected_option
    print(f"Text: {selected_option.text}")

finally:
    driver.quit()

