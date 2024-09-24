from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

class WebDriver:
    def __init__(self):
        chromedriver_path= os.path.join(os.getcwd(),'driver','chromedriver')
        service= Service(executable_path=chromedriver_path)
        self.driver =webdriver.Chrome(service=service)