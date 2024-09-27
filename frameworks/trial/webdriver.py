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
        options.add_argument("--headless")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(service=service, options=options)


# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# class WebDriver:
#     def __init__(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--no-sandbox")   
#         options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
#         options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)

#         self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options

# class WebDriver:
#     def __init__(self):
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")  # Ensure headless mode is enabled
#         chrome_options.add_argument("--disable-gpu")
#         chrome_options.add_argument("--no-sandbox")
#         chrome_options.add_argument("--disable-dev-shm-usage")

#         service = Service(ChromeDriverManager().install())
#         self.driver = webdriver.Chrome(service=service, options=chrome_options)


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# class WebDriver:
#     def __init__(self):
#         options = Options()
#         options.add_argument("--headless")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")
#         options.add_argument("--disable-gpu")
        
#         # Use Remote WebDriver to connect to the Selenium Grid
#         self.driver = webdriver.Remote(
#             command_executor='http://selenium-chrome:4444/wd/hub',  # Point to the Chrome service
#             options=options
#         )
