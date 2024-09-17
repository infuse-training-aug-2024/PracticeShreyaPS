from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.edge.service import Service as edgeService

driver_path="C:/Users/91989/Downloads/driver/msedgedriver.exe"
url='https://www.quora.com/'
edge_service = edgeService(executable_path=driver_path)
driver = Edge(service=edge_service)
try:

    driver.get(url)
    website_title=driver.title
    print(website_title)
except Exception as e:
    print(f"error occured :{e}")
finally:
    driver.quit()

