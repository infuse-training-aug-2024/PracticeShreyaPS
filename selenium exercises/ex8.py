# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service as chromeService
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep


# driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
# url='https://www.globalsqa.com/demo-site/sliders/#Steps'
# chrome_service = chromeService(executable_path=driver_path)
# driver = Chrome(service=chrome_service)


# driver.get(url)

# try:
#     wait = WebDriverWait(driver, 20)
#     iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.demo-frame.lazyloaded')))
#     driver.switch_to.frame(iframe)

#     slider_handle = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ui-slider-handle.ui-corner-all.ui-state-default')))
    
#     action = ActionChains(driver)
#     action.drag_and_drop_by_offset(slider_handle, 200, 0).perform()

# finally:
#     sleep(5)
#     driver.quit()
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url = 'https://www.globalsqa.com/demo-site/sliders/#Steps'
chrome_service = chromeService(executable_path=driver_path)
driver = Chrome(service=chrome_service)

driver.get(url)

try:
    wait = WebDriverWait(driver, 20)
    iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.demo-frame.lazyloaded')))
    driver.switch_to.frame(iframe)

    # Locate the slider handle
    slider_handle = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'ui-slider-handle')))
    
    # Create an ActionChain object
    action = ActionChains(driver)
    
    # Click on the slider to focus on it
    slider_handle.click()
    
    # Use arrow keys to move the slider (you can use ARROW_LEFT to move in the opposite direction)
    for _ in range(5):  # Adjust the range for how many steps to move
        action.send_keys(Keys.ARROW_RIGHT).perform()
        sleep(0.2)  # Adding a small delay between each key press for smooth movement

finally:
    sleep(5)
    driver.quit()
