from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService

class TableAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_browser(self):
        chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

    def extract_column_data(self, column_no):
        try:
            table = self.driver.find_element(By.TAG_NAME, "table")
            table_header = table.find_element(By.TAG_NAME, "thead")
            table_body = table.find_element(By.TAG_NAME, "tbody")
            column_header = table_header.find_elements(By.TAG_NAME, 'th')[column_no]
            print(f"Column Header: {column_header.text}")
            rows = table_body.find_elements(By.TAG_NAME, 'tr')
            column_data = []
            for row in rows:
                col = row.find_elements(By.TAG_NAME, 'td')[column_no]
                column_data.append(col.text)
            for data in column_data:
                print(data)

        except Exception as e:
            print(f"An error occurred: {e}")

    def close_browser(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://computer-database.gatling.io/computers'
    column_no = 0

    automation = TableAutomation(driver_path, url)
    automation.start_browser()
    automation.extract_column_data(column_no)
    automation.close_browser()
