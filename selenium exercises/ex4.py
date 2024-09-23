from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep

class FormAutomation:
    def __init__(self, driver_path, url):
        chrome_service = ChromeService(executable_path=driver_path)
        self.driver = Chrome(service=chrome_service)
        self.url = url
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 10)

    def select_radio_button_by_index(self, radio_name, index):
        try:
            radio_buttons = self.wait.until(EC.presence_of_all_elements_located((By.NAME, radio_name)))
            radio_buttons[index].click()
            print(f"Radio button at index {index} clicked.")
        except TimeoutError as e:
            print(f"Timeout error while selecting radio button: {e}")


    def select_checkbox(self, checkbox_id):
        try:
            checkbox_button = self.wait.until(EC.element_to_be_clickable((By.ID, checkbox_id)))
            checkbox_button.click()
            print(f"Checkbox '{checkbox_id}' clicked.")
        except TimeoutError as e:
            print(f"Timeout error while selecting checkbox: {e}")
        finally:
            self.driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://demo.automationtesting.in/Register.html'
    automation = FormAutomation(driver_path, url)
    automation.select_radio_button_by_index('radiooptions', 1)
    automation.select_checkbox('checkbox1')
