from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

driver.get('https://the-internet.herokuapp.com/tables')

table = driver.find_element(By.ID,"table1")
table_body = driver.find_element(By.TAG_NAME,"tbody")
rows=table_body.find_elements(By.TAG_NAME,'tr')
col = rows[1].find_elements(By.TAG_NAME,'td')[2].text

print(col)

driver.quit()