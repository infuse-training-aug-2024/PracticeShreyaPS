from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.support.ui import Select

class FormAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_browser(self):
        chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)

    def navigate(self):
        self.driver.get(self.url)

    def select_dropdown_by_value(self, dropdown_name, value):
        try:
            dropdown = self.driver.find_element(By.NAME, dropdown_name)
            select = Select(dropdown)
            select.select_by_value(value)
            selected_option = select.first_selected_option
            print(f"Selected option text: {selected_option.text}")
        except Exception as e:
            print(f"Error while selecting dropdown: {e}")

    def close_browser(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://testpages.herokuapp.com/styled/basic-html-form-test.html'
    ith_index = 'dd4'

    automation = FormAutomation(driver_path, url)
    automation.start_browser()
    automation.navigate()
    automation.select_dropdown_by_value('dropdown', ith_index)
    automation.close_browser()
