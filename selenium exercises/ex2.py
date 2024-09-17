from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

driver.get('https://www.quora.com/')

title=driver.title

print(title)