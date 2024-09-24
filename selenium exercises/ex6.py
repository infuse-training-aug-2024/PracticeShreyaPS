from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

class FormDropdownAutomation:
    def __init__(self, driver_path, url):
        chrome_service = ChromeService(executable_path=driver_path)
        self.driver = Chrome(service=chrome_service)
        self.url = url
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def print_dropdown_options(self, tag_name):
        try:
            dropdown = self.driver.find_element(By.TAG_NAME, tag_name)
            select = Select(dropdown)
            options = select.options
            for option in options:
                print(option.text)
        except Exception as e:
            print(f"Error occurred while fetching dropdown options: {e}")

    def close_browser(self):
        self.driver.quit()
        print("Browser closed.")

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://letcode.in/forms'
    automation = FormDropdownAutomation(driver_path, url)
    automation.print_dropdown_options('select')
    automation.close_browser()
