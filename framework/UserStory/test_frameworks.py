import unittest
from Framework import Framework
from webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFramework(unittest.TestCase):
    URL='https://www.saucedemo.com/'
    URL2='https://cosmocode.io/automation-practice-webtable/'
    URL3='https://testpages.herokuapp.com/styled/basic-html-form-test.html'

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
        current_url=self.framework.get_current_url
        print(f"url:{current_url}")
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

    def test_enter_invalid_field(self):
        self.framework.navigate_to_page(self.URL)  
        locator = (By.ID, "invalid")  
        input_result = self.framework.enter_field(locator, "standard_user")  
        self.assertFalse(input_result, "Expected entering text into an invalid field to return False.")

    def test_get_text(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'login_logo')
        text = self.framework.get_text(locator)
        self.assertEqual(text, "Swag Labs")

    def test_get_text_invalid_case(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'invalid')
        text = self.framework.get_text(locator)
        self.assertIsNone(text)

    def test_is_element_visible(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'login_logo')
        element = self.framework.is_element_visible(locator)
        self.assertTrue(element)

    def test_is_element_not_visible(self):
        self.driver.get(self.URL)
        locator=(By.CLASS_NAME,'invalid')
        element = self.framework.is_element_visible(locator)
        self.assertFalse(element)

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

    def test_get_elements(self):
        self.driver.get(self.URL2) 
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "countries")))  
        locator = (By.TAG_NAME, "tr")  
        elements = self.framework.get_elements(locator) 
        self.assertIsNotNone(elements)
        self.assertGreater(len(elements), 0, "No elements found")

    def test_submit_form(self):
        self.driver.get(self.URL)
        locator=(By.TAG_NAME,'form') 
        result = self.framework.submit_form(locator)
        self.assertTrue(result)

    def test_submit_formInvalid(self):
        self.driver.get(self.URL)
        locator=(By.TAG_NAME,'invlaid-form') 
        result = self.framework.submit_form(locator)
        self.assertFalse(result)

    def test_fill_form(self):
        self.driver.get(self.URL)
        form_data={"user-name":"standard_user","password":"secret_sauce"}
        result=self.framework.fill_form(form_data)
        self.wait.until(EC.presence_of_element_located((By.ID,'user-name')))
        input_element = self.driver.find_element(By.ID, 'user-name')
        input_value = input_element.get_attribute("value")
        self.assertEqual(input_value,'standard_user')

    def test_fill_form_invalid_locator(self):
        self.driver.get(self.URL)
        invalid_form_data = {
            "invalid-user-name": "invalid_user", 
            "invalid-password": "invalid_password"
        }
        result = self.framework.fill_form(invalid_form_data)
        self.assertFalse(result, "Expected fill_form to return False for invalid locators.")

    def test_select_option_by_value(self):
            self.driver.get(self.URL3)  
            locator = (By.NAME, 'dropdown')  
            result = self.framework.select_option_by_value(locator, 'dd4')  
            self.assertEqual(result, "Drop Down Item 4") 
    def test_select_option_by_value_invalid(self):
            self.driver.get(self.URL3) 
            locator = (By.NAME, 'dropdown') 
            result = self.framework.select_option_by_value(locator, 'invalid')  
            self.assertIsNone(result) 

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

    def test_get_alert_text(self):
            self.driver.get("data:text/html,<script>alert('Test Alert');</script>")
            self.wait.until(EC.alert_is_present())
            alert_text = self.framework.get_alert_text()
            self.assertEqual(alert_text, "Test Alert")
            self.driver.switch_to.alert.accept()

    def test_get_alert_text_no_alert(self):
        self.driver.get("about:blank")
        alert_text = self.framework.get_alert_text()
        self.assertIsNone(alert_text, "Expected None when no alert is present")

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
        self.framework.navigate_to_page(self.URL)
        result = self.framework.maximize_window()
        if (lambda d: d.get_window_size()['width'] > 1024):
            self.assertTrue(result)

    def test_minimize_window(self):
        self.framework.navigate_to_page(self.URL)
        result = self.framework.minimize_window()
        if (lambda d: d.get_window_position()['y'] > 0):
            self.assertTrue(result)

    def test_get_page_title(self):
        page_title=self.framework.get_page_title()
        self.assertEqual(page_title,self.driver.title)
     
    def test_get_current_url(self):
         self.driver.get(self.URL)
         current_url=self.framework.get_current_url()
         self.assertEqual(current_url,self.URL)

    def test_get_attribute(self):
        self.framework.navigate_to_page(self.URL)
        locator=(By.ID,'user-name')
        element = self.framework.get_element(locator) 
        attribute_name = "placeholder"
        expected_value = "Username"  
        actual_value = self.framework.get_attribute(locator, attribute_name)
        self.assertEqual(actual_value, expected_value)

    def test_click_invalid_element(self):
        self.framework.navigate_to_page(self.URL)
        invalid_locator = (By.ID, "invalid-element")
        result = self.framework.click_element(invalid_locator)
        self.assertFalse(result, "Expected clicking an invalid element to return False.")

    def test_enter_invalid_input(self):
        self.framework.navigate_to_page(self.URL)
        locator = (By.ID, "user-name")
        input_result = self.framework.enter_field(locator, "")  
        self.assertTrue(input_result)

    def test_element_not_visible(self):
        self.framework.navigate_to_page(self.URL)
        invalid_locator = (By.ID, "hidden-element")
        is_visible = self.framework.is_element_visible(invalid_locator)
        self.assertFalse(is_visible, "Expected the element to not be visible.")

    def test_get_non_existent_element(self):
        self.framework.navigate_to_page(self.URL)
        invalid_locator = (By.ID, "non-existent")
        element = self.framework.get_element(invalid_locator)
        self.assertIsNone(element, "Expected the element to be None since it does not exist.")

    def test_get_attribute_not_found(self):
        self.framework.navigate_to_page(self.URL)
        locator = (By.ID, 'user-name')
        non_existent_attribute = self.framework.get_attribute(locator, "non_existent_attribute")
        self.assertIsNone(non_existent_attribute, "Expected None for a non-existent attribute.")

    def test_redirect_after_login(self):
        username_locator = (By.ID, "user-name")
        password_locator = (By.ID, "password")
        submit_button_locator = (By.ID, "login-button")
        self.framework.login("standard_user", "secret_sauce", username_locator, password_locator, submit_button_locator)
        WebDriverWait(self.driver, 10).until(EC.url_contains("/inventory.html"))
        self.assertIn("/inventory.html", self.driver.current_url, "Expected to be redirected to the inventory page after login.")

if __name__ == '__main__':
    unittest.main()