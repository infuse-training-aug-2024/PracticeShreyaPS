from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Setup Chrome driver
driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
chrome_service = chromeService(executable_path=driver_path)
driver = Chrome(service=chrome_service)

# Open the webpage
driver.get('https://www.globalsqa.com/demo-site/sliders/#Steps')

try:
    # Wait for the iframe to load and switch to it
    wait = WebDriverWait(driver, 20)
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.demo-frame.lazyloaded')))
    driver.switch_to.frame(iframe)

    # Wait for the slider handle to be clickable inside the iframe
    slider_handle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ui-slider-handle.ui-corner-all.ui-state-default')))
    
    # Perform drag and drop action on the slider handle
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(slider_handle, 200, 0).perform()

finally:
    # Pause for a moment to observe the result, then close the browser
    sleep(5)
    driver.quit()
