from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService

class AutomateGoogle:
    def __init__(self, driver_path):
        chrome_service = ChromeService(executable_path=driver_path)
        self.driver = Chrome(service=chrome_service)
        self.url = 'https://www.google.com/'

    def open_google(self):
        try:
            self.driver.implicitly_wait(10)
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(5)  
        except TimeoutError as e:
            print(f"Timeout error occurred: {e}")
        finally:
            self.driver.quit()

    
    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    google_object = AutomateGoogle(driver_path)
    google_object.open_google()
    google_object.close_browser()
