from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Framework:
    def __init__(self, driver: webdriver, wait_time: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time) 

    # Navigation functions----------------------------------------------
    def navigate_to_page(self, url):
        try:
            self.driver.get(url)
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            return self.driver.title
        except Exception as e:
            print(f"Error navigating to page: {e}")
            return None  

    #interaction functions----------------------------------------------
    # def click_element(self, locator):
    #     try:
    #         element = self.driver.find_element(*locator)
    #         element.click()
    #         return True  
    #     except Exception as e:
    #         print(f"Error clicking the element: {e}")
    #         return False
    def click_element(self, locator):
        try:
            # Wait for the element to be clickable
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return True
        except Exception as e:
            print(f"Error clicking the element: {e}")
            return False

    def enter_field(self, locator, text):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(text)
            return True
        except TimeoutException:
            print(f"Element with locator {locator} not found in time.")
            return False
        
    def select_option_by_value(self, locator, value):
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                dropdown_element = self.driver.find_element(*locator)
                dropdown = Select(dropdown_element)
                dropdown.select_by_value(value)
                selected_option = dropdown.first_selected_option
                if not selected_option:
                    raise NoSuchElementException(f"Element not found for locator: {locator}")
                return selected_option.text
            except NoSuchElementException as e:
                print(f"Error selecting option by value: {e}")
                return None

    def get_element(self, locator):
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            element = self.driver.find_element(*locator)
            return element
        except Exception as e:
            print(f"Error getting the element: {e}")
            return None
        
    def get_elements(self, locator):
            try:
                self.wait.until(EC.presence_of_element_located(locator))
                elements = self.driver.find_elements(*locator)
                return elements
            except TimeoutException:
                print(f"Error getting the elements: ")
                return []

    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            print(f"Element with locator {locator} not found on the page.")
            return False

    def get_text(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            element = self.driver.find_element(*locator)
            return element.text
        except TimeoutException:
            print(f"Error getting text of the element in time: ")
            return None

    def get_attribute(self, locator, attribute_name):
        try:
            element = self.driver.find_element(*locator)
            return element.get_attribute(attribute_name)
        except Exception as e:
            print(f"Error getting attribute '{attribute_name}' from element: {e}")
            return None

    # Form handling ---------------------------------------------------
    def submit_form(self, locator):
        try:
            element = self.driver.find_element(*locator)
            element.submit()
            return True
        except NoSuchElementException:
            print(f"Error submitting form:")
            return False

    def fill_form(self, form_data):
        try:
            for locator_id, text in form_data.items():
                locator=(By.ID,locator_id)
                field_filled=self.enter_field(locator, text)
                if not field_filled:
                    raise NoSuchElementException(f"Element not found for locator: {locator}")
            return True
        except NoSuchElementException:
            print(f"Error filling form:")
            return False

    # Browser actions -------------------------------------------------
    def get_current_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            print(f"Error getting current URL: {e}")
            return None

    def get_page_title(self):
        try:
            return self.driver.title
        except Exception as e:
            print(f"Error getting page title: {e}")
            return None

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except Exception as e:
            print(f"Error handling alert: {e}")
            return None

    # Authentication --------------------------------------------------
    def login(self, username, password, username_field_locator, password_field_locator, submit_button_locator):
        try:
            self.enter_field(username_field_locator, username)
            self.enter_field(password_field_locator, password)
            self.click_element(submit_button_locator)
            return True
        except Exception as e:
            print(f"Error logging in: {e}")
            return False

    def logout(self, logout_button_locator):
        try:
            self.click_element(logout_button_locator)
            return True
        except Exception as e:
            print(f"Error logging out: {e}")
            return False

    # Alerts ----------------------------------------------------------
    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except Exception as e:
            print(f"Error getting alert text: {e}")
            return None

    # Window management -----------------------------------------------
    def maximize_window(self):
        try:
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error maximizing window: {e}")
            return False

    def minimize_window(self):
        try:
            self.driver.minimize_window()
            return True
        except Exception as e:
            print(f"Error minimizing window: {e}")
            return False
