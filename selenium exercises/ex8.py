from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url='https://www.globalsqa.com/demo-site/sliders/#Steps'
chrome_service = chromeService(executable_path=driver_path)
driver = Chrome(service=chrome_service)


driver.get(url)

try:
    wait = WebDriverWait(driver, 20)
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.demo-frame.lazyloaded')))
    driver.switch_to.frame(iframe)

    slider_handle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ui-slider-handle.ui-corner-all.ui-state-default')))
    
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider_handle, 200, 0).perform()

finally:
    sleep(5)
    driver.quit()
