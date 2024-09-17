from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://cosmocode.io/automation-practice-webtable/'
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

try:
    driver.get(url)

    table = driver.find_element(By.ID,"countries")
    header_row=table.find_element(By.TAG_NAME,'tr')
    cols = header_row.find_elements(By.TAG_NAME,'td')

    for col in cols:
        print(col.text)
        
except TimeoutError as e:
    print(f"timeout error:{e}")
finally:
    driver.quit()

