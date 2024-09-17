from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://the-internet.herokuapp.com/tables'
row_index=1
col_index=2
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

try:
    driver.get(url)

    table = driver.find_element(By.ID,"table1")
    table_body = driver.find_element(By.TAG_NAME,"tbody")
    rows=table_body.find_elements(By.TAG_NAME,'tr')
    col = rows[row_index].find_elements(By.TAG_NAME,'td')[col_index].text

    print(f"table cell value:{col}")
except TimeoutError as e:
    print(f"timeout error:{e}")
finally:
    driver.quit()