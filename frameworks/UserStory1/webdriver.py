# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import os

# class WebDriver:
#     def __init__(self):
#         chromedriver_path= os.path.join(os.getcwd(),'UserStory1','drivers','chromedriver.exe')
#         service= Service(executable_path=chromedriver_path)
#         option=Options()
#         option.add_argument('--headless')
#         option.add_argument('--no-sandbox')
#         option.add_argument('--disable-dev-shm-usage')
#         self.driver =webdriver.Chrome(service=service,options=option)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriver:
    def __init__(self):
        # Automatically download and use the correct version of chromedriver
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=service, options=options)
