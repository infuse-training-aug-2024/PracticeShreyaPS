from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService

class AutomateSearch():
    def __init__(self,driver_path):
        self.url='https://www.yahoo.com/'
        chrome_service = chromeService(executable_path=driver_path)
        self.driver=Chrome(service=chrome_service)
    def click_search_bar(self):
         try:
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10)
            search_input = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-sbq')))
            search_input.click()
         except TimeoutError as e:
            print(f"timeout error:{e}")
         finally:
            sleep(5)

    def enter_search(self):
            try:
                wait = WebDriverWait(self.driver, 10)
                search_input = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-sbq')))
                search_input.send_keys("selenium")
            except TimeoutError as e:
                print(f"timeout error:{e}")
            finally:
                sleep(5)
    def hit_search(self):
            try:
                wait = WebDriverWait(self.driver, 10)
                search_icon = wait.until(EC.element_to_be_clickable((By.ID, 'ybar-search')))
                search_icon.click()
            except TimeoutError as e:
                print(f"timeout error:{e}")
            finally:
                sleep(5)
                self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    yahoo = AutomateSearch(driver_path)
    yahoo.click_search_bar()
    yahoo.enter_search()
    yahoo.hit_search()

    



            