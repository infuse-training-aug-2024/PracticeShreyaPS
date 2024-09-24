from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService

class WebTableAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_browser(self):
        chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

    def extract_table_headers(self, table_id):
        try:
            table = self.driver.find_element(By.ID, table_id)
            header_row = table.find_element(By.TAG_NAME, 'tr')
            cols = header_row.find_elements(By.TAG_NAME, 'td')
            print("Table Headers:")
            for col in cols:
                print(col.text)

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def close_browser(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://cosmocode.io/automation-practice-webtable/'
    automation = WebTableAutomation(driver_path, url)
    automation.start_browser()
    automation.extract_table_headers('countries')
    automation.close_browser()
