from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://computer-database.gatling.io/computers'
column_no=0
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

try:
    driver.get(url)

    table = driver.find_element(By.TAG_NAME,"table")
    table_body = driver.find_element(By.TAG_NAME,"tbody")
    rows=table_body.find_elements(By.TAG_NAME,'tr')


    for row in rows:
        col = row.find_elements(By.TAG_NAME,'td')[column_no]
        print(col.text)
except TimeoutError as e:
    print(f"timeout error occured:{e}")

finally:
    driver.quit()