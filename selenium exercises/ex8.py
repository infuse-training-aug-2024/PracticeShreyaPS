from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

class SliderAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_browser(self):
        chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)


    def move_slider(self, iframe_selector, slider_class, steps=5, direction=Keys.ARROW_RIGHT):
        try:
            wait = WebDriverWait(self.driver, 20)
            iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector)))
            self.driver.switch_to.frame(iframe)
            slider_handle = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, slider_class)))
            action = ActionChains(self.driver)
            slider_handle.click()
            for _ in range(steps):
                action.send_keys(direction).perform()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            sleep(5) 
            self.driver.quit()


if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://www.globalsqa.com/demo-site/sliders/#Steps'

    automation = SliderAutomation(driver_path, url)
    automation.start_browser()
    automation.move_slider(iframe_selector='.demo-frame.lazyloaded', slider_class='ui-slider-handle', steps=5, direction=Keys.ARROW_RIGHT)
