import unittest
from Framework import Framework
from webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFramework(unittest.TestCase):
    demo_url='https://www.phptravels.net/'
    URL='https://www.saucedemo.com/'
    URL_for_inventory='https://www.saucedemo.com/inventory.html'


    @classmethod
    def setUpClass(cls):
        cls.webdriver=WebDriver()
        cls.driver =cls.webdriver.driver
        cls.framework= Framework(cls.driver)
        cls.wait = WebDriverWait(cls.driver, 10) 

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_object_creation_of_webdriver(self):
        self.assertIsInstance(self.webdriver, WebDriver)

    def test_object_creation_of_framework(self):
        self.assertIsInstance(self.framework, Framework)

    def test_navigate_to_page(self):
        page_title=self.framework.navigate_to_page(self.URL)
        print(f"title:{page_title}")
        self.assertIsNotNone(page_title)

    def test_click_element(self):
        self.framework.navigate_to_page(self.URL)
        locator = (By.ID, "user-name")
        element_clickable=self.framework.click_element(locator)
        self.assertTrue(element_clickable)

    def test_enter_valid_field(self):
        self.framework.navigate_to_page(self.URL)
        locator = (By.ID, "user-name")
        input= self.framework.enter_field(locator,"standard_user")
        self.assertTrue(input)


    def test_get_text(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'login_logo')
        text = self.framework.get_text(locator)
        self.assertEqual(text, "Swag Labs")

    def test_is_element_visible(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'login_logo')
        element = self.framework.is_element_visible(locator)
        self.assertTrue(element)

    def test_get_element_valid_case(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'login_logo')
        element=self.framework.get_element(locator)
        self.assertIsNotNone(element)

    def test_get_element_invalid_case(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'inavalid-class')
        element=self.framework.get_element(locator)
        self.assertIsNone(element)

    def test_submit_form(self):
        self.driver.get(self.URL)
        locator=(By.TAG_NAME,'form') 
        result = self.framework.submit_form(locator)
        self.assertTrue(result)

    def test_fill_form(self):
        self.driver.get(self.URL)
        form_data={"user-name":"standard_user","password":"secret_sauce"}
        result=self.framework.fill_form(form_data)
        self.wait.until(EC.presence_of_element_located((By.ID,'user-name')))
        input_element = self.driver.find_element(By.ID, 'user-name')
        input_value = input_element.get_attribute("value")
        self.assertEqual(input_value,'standard_user')



    # def test_select_option_by_value(self):
    #         self.driver.get(self.demo_url)  # Navigate to the page with the dropdown
    #         locator = (By.NAME, 'flight_type')  # Use the correct locator
    #         result = self.framework.select_option_by_value(locator, 'economy')  # Attempt to select 'economy'
            
    #         # Check if the selection was successful
    #         self.assertEqual(result, "Economy") 


    def test_handle_alert(self):
            self.driver.get("data:text/html,<script>alert('Test Alert');</script>")
            alert = self.framework.handle_alert()
            self.assertIsNotNone(alert)
            self.assertEqual(alert.text, "Test Alert")
            alert.accept()

    def test_handle_alert_no_alert(self):
        self.driver.get("about:blank")
        alert = self.framework.handle_alert()
        self.assertIsNone(alert)

    def test_login_valid_credentials(self):
            username_locator = (By.ID, "user-name")
            password_locator = (By.ID, "password")
            submit_button_locator = (By.ID, "login-button")
            login_result = self.framework.login("standard_user", "secret_sauce", username_locator, password_locator, submit_button_locator)
            self.assertTrue(login_result)
            self.assertIn("/inventory.html", self.driver.current_url)

    def test_login_invalid_credentials(self):
            username_locator = (By.ID, "user-name")
            password_locator = (By.ID, "password")
            submit_button_locator = (By.ID, "login-button")
            login_result = self.framework.login("invalid_username", "invalid_password", username_locator, password_locator, submit_button_locator)
            self.assertEqual(self.URL, self.driver.current_url)

    def test_logout(self):
        username_locator = (By.ID, "user-name")
        password_locator = (By.ID, "password")
        submit_button_locator = (By.ID, "login-button")
        self.framework.login("standard_user", "secret_sauce", username_locator, password_locator, submit_button_locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'react-burger-menu-btn')))
        self.driver.find_element(By.ID, 'react-burger-menu-btn').click()
        logout_button_locator = (By.ID, "logout_sidebar_link")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(logout_button_locator))
        logout_result = self.framework.logout(logout_button_locator)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/"))
        self.assertTrue(logout_result)
        self.assertEqual(self.URL, self.driver.current_url)



    def test_maximize_window(self):
        result = self.framework.maximize_window()
        if (lambda d: d.get_window_size()['width'] > 1024):
            self.assertTrue(result)

    def test_minimize_window(self):
        result = self.framework.minimize_window()
        if (lambda d: d.get_window_position()['y'] > 0):
            self.assertTrue(result)


 
if __name__ == '__main__':
    unittest.main()