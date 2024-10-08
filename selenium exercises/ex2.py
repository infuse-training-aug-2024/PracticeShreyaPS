from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.edge.service import Service as edgeService

class WebsiteTitle:
    def __init__(self, driver_path):
        edge_service = edgeService(executable_path=driver_path)
        self.driver = Edge(service=edge_service)
        self.url = 'https://www.quora.com/'

    def get_title(self):
        try:
            self.driver.get(self.url)
            website_title=self.driver.title
            print(website_title)
        except Exception as e:
                print(f"error occured :{e}")
        finally:
                self.driver.quit()

if __name__ == "__main__":
    driver_path = "C:/Users/91989/Downloads/driver/msedgedriver.exe"
    Quora = WebsiteTitle(driver_path)
    Quora.get_title()


                
            
            
