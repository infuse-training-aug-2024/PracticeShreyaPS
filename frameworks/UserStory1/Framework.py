from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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

    def refresh_page(self):
        try:
            self.driver.execute_script("location.reload()")
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            return self.driver.title
        except Exception as e:
            print(f"Error refreshing to page: {e}")
            return None  

#interaction functions----------------------------------------------


    def click_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
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
        except Exception as e:
            print(f"Error entering text into field: {e}")
            return False

    def select_option_by_value(self, locator, value):
            try:
                # Wait until the dropdown is present
                self.wait.until(EC.presence_of_element_located(locator))
                dropdown_element = self.driver.find_element(*locator)
                dropdown = Select(dropdown_element)
                
                # Debug: Print available options
                print("Dropdown options before selection:", [option.text for option in dropdown.options])
                
                # Select the option by value
                dropdown.select_by_value(value)
                
                # Wait for the selection to reflect and get the selected option
                self.wait.until(EC.presence_of_element_located((By.XPATH, f"//option[@value='{value}'][@selected]")))
                selected_option = dropdown.first_selected_option
                
                # Debug: Print the selected option
                print("Selected option after selection:", selected_option.text)
                return selected_option.text
            except Exception as e:
                print(f"Error selecting option by value: {e}")
                return None


    def hover_over_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        except Exception as e:
            print(f"Error hovering over element: {e}")
            return False

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
                elements = self.driver.find_element(*locator)
                return elements
            except Exception as e:
                print(f"Error getting the elements: {e}")
                return []


    def is_element_visible(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except Exception as e:
            print(f"Error checking if element is visible: {e}")
            return False

    def is_element_selected(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_selected()
        except Exception as e:
            print(f"Error checking if element is selected: {e}")
            return False

    def get_text(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            element = self.driver.find_element(*locator)
            return element.text
        except Exception as e:
            print(f"Error getting text of the element: {e}")
            return None

        

    def get_attribute(self, locator, attribute_name):
        try:
            element = self.driver.find_element(locator)
            return element.get_attribute(attribute_name)
        except Exception as e:
            print(f"Error getting attribute '{attribute_name}' from element: {e}")
            return None

    def get_element_placeholder(self, locator):
        try:
            element = self.driver.find_element(locator)
            return element.get_attribute('placeholder')
        except Exception as e:
            print(f"Error getting placeholder attribute: {e}")
            return None


    def wait_for_element_visible(self, locator, timeout=10):
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
                return True
            except Exception as e:
                print(f"Error waiting for element to be visible: {e}")
                return False

    def wait_for_element_clickable(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except Exception as e:
            print(f"Error waiting for element to be clickable: {e}")
            return False

    def get_element_placeholder(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.get_attribute('placeholder')
        except Exception as e:
            print(f"Error getting placeholder: {e}")
            return None

    # Form handling ---------------------------------------------------
    def submit_form(self, locator):
        try:
            element = self.driver.find_element(*locator)
            element.submit()
            return True
        except Exception as e:
            print(f"Error submitting form: {e}")
            return False

    def fill_form(self, form_data):
        try:
            for locator_id, text in form_data.items():
                locator=(By.ID,locator_id)
                self.enter_field(locator, text)
            return True
        except Exception as e:
            print(f"Error filling form: {e}")
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

    def switch_to_frame(self, frame_locator):
        try:
            frame = self.driver.find_element(*frame_locator)
            self.driver.switch_to.frame(frame)
            return True
        except Exception as e:
            print(f"Error switching to frame: {e}")
            return False

    def handle_alert(self):
        try:
            alert = self.driver.switch_to.alert
            return alert
        except Exception as e:
            print(f"Error handling alert: {e}")
            return None


    def upload_file(self, file_path, locator):
        try:
            upload_element = self.driver.find_element(*locator)
            upload_element.send_keys(file_path)
            return True
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False

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

    # Cookies ---------------------------------------------------------
    def get_cookie(self, cookie_name):
        try:
            return self.driver.get_cookie(cookie_name)
        except Exception as e:
            print(f"Error getting cookie: {e}")
            return None

    def add_cookie(self, cookie):
        try:
            self.driver.add_cookie(cookie)
            return True
        except Exception as e:
            print(f"Error adding cookie: {e}")
            return False

    def delete_cookie(self, cookie_name):
        try:
            self.driver.delete_cookie(cookie_name)
            return True
        except Exception as e:
            print(f"Error deleting cookie: {e}")
            return False

    # Alerts ----------------------------------------------------------
    def accept_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            return True
        except Exception as e:
            print(f"Error accepting alert: {e}")
            return False

    def dismiss_alert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            return True
        except Exception as e:
            print(f"Error dismissing alert: {e}")
            return False

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except Exception as e:
            print(f"Error getting alert text: {e}")
            return None

    # Window management -----------------------------------------------
    def switch_to_window(self, window_handle):
        try:
            self.driver.switch_to.window(window_handle)
            return True
        except Exception as e:
            print(f"Error switching to window: {e}")
            return False

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

    def close_window(self):
        try:
            self.driver.close()
            return True
        except Exception as e:
            print(f"Error closing window: {e}")
            return False