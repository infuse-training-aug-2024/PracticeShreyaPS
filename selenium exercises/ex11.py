from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService

class TableCellAutomation:
    def __init__(self, driver_path, url):
        self.driver_path = driver_path
        self.url = url
        self.driver = None

    def start_browser(self):
        chrome_service = chromeService(executable_path=self.driver_path)
        self.driver = Chrome(service=chrome_service)
        self.driver.implicitly_wait(5)
        self.driver.get(self.url)

    def get_table_cell(self, table_id, row_index, col_index):
        try:
            table = self.driver.find_element(By.ID, table_id)
            table_body = table.find_element(By.TAG_NAME, "tbody")
            rows = table_body.find_elements(By.TAG_NAME, 'tr')
            cell_value = rows[row_index].find_elements(By.TAG_NAME, 'td')[col_index].text
            print(f"Table cell value: {cell_value}")

        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def close_browser(self):
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
    url = 'https://the-internet.herokuapp.com/tables'
    row_index = 1
    col_index = 2

    automation = TableCellAutomation(driver_path, url)
    automation.start_browser()
    automation.get_table_cell("table1", row_index, col_index)    
    automation.close_browser()
