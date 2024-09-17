from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://joyrel-vaz.github.io/cross-browser-testing/'
chrome_service = chromeService(executable_path=driver_path)
driver = Chrome(service=chrome_service)

try:
    driver.get(url)
    browser_name = driver.capabilities['browserName'].lower()
    print(browser_name)
    first_rectangle_id='js-test'
    wait = WebDriverWait(driver, 20)
    first_rectangle = wait.until(EC.presence_of_element_located((By.ID,first_rectangle_id)))
    if(browser_name in first_rectangle.text.lower() ):
        print("browser name matches\n")
    else:
        print("does not match")

finally:
    driver.quit()