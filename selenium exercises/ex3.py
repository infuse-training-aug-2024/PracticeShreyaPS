from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as chromeService

class AutomateSearch:
    def __init__(self,driver_path):
        self.url="https://demo.automationtesting.in/Register.html"
        chrome_service = chromeService(executable_path=driver_path)
        self.driver=Chrome(service=chrome_service)
        
    def automate_search(self):
        try:
            self.driver.get(self.url)
            wait = WebDriverWait(self.driver, 10)
            add_question_button = wait.until(EC.element_to_be_clickable((By.ID, 'submitbtn')))
            add_question_button.click()
        except TimeoutError as e:
            print(f"timeout error:{e}")
        finally:
            sleep(5)
            self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    website = AutomateSearch(driver_path)
    website.automate_search()
