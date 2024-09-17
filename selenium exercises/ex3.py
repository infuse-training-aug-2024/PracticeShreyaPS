from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService

driver_path="C:/Users/91989/Downloads/driver/chromedriver.exe"
chrome_service = chromeService(executable_path=driver_path)
driver=Chrome(service=chrome_service)

driver.get('https://www.quora.com/')
try:
    wait = WebDriverWait(driver, 10)
    add_question_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.q-click-wrapper.puppeteer_test_add_question_button.byzv0ju.b1rvgfgm.bobc9nh.b1cg7ppz.c1nud10e.qu-active--textDecoration--none.qu-focus--textDecoration--none.qu-borderTopLeftRadius--pill.qu-borderBottomLeftRadius--pill.qu-alignItems--center.qu-justifyContent--center.qu-whiteSpace--nowrap.qu-userSelect--none.qu-display--inline-flex.qu-bg--red.qu-tapHighlight--white.qu-textAlign--center.qu-cursor--pointer.qu-hover--textDecoration--none')))
    add_question_button.click()
finally:
    sleep(5)
    driver.quit()

