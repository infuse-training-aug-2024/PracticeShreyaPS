from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as chromeService

driver_path = "C:/Users/91989/Downloads/driver/chromedriver.exe"
url = 'https://computer-database.gatling.io/computers'
column_no = 0 

chrome_service = chromeService(executable_path=driver_path)
driver = Chrome(service=chrome_service)

try:
    driver.get(url)
    table = driver.find_element(By.TAG_NAME, "table")
    
    table_header = table.find_element(By.TAG_NAME, "thead")
    table_body = table.find_element(By.TAG_NAME, "tbody")
    
    # Get the column header
    column_header = table_header.find_elements(By.TAG_NAME, 'th')[column_no]
    print(column_header.text)
    
    # Get all the rows of the table body
    rows = table_body.find_elements(By.TAG_NAME, 'tr')
    
    # Loop through each row and print the corresponding column data
    for row in rows:
        col = row.find_elements(By.TAG_NAME, 'td')[column_no]
        print(col.text)
    
except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
