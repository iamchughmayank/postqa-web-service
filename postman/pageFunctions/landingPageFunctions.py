from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from postman.testData import constants
from postman.pageLocators import landing
from time import sleep
from selenium.common.exceptions import *

def navigate_to_login(resource):
    try:
        resource.driver.get(constants.base_url)
        return True
    except Exception as e:
        print('Unable to navigate to Login screen due to, ', e)
        return False

def validate_landing_screen(resource):
    try:
        postman_log = resource.driver.find_element_by_class_name(landing.logo)
        return True
    except (NoSuchElementException,TimeoutException):
        return False

def validate_login(resource):
    try:
        uname = resource.driver.find_element_by_id(landing.uname)
        uname.send_keys('iamchughmayank@gmail.com')
        pswd = resource.driver.find_element_by_id(landing.pword)
        pswd.send_keys("Dreamon*0100")
        sbmit_btn = resource.driver.find_element_by_id(landing.signinbtn)
        sbmit_btn.click()
        user_icon = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,landing.user_btn))))
        return True
    except Exception as e:
        print(e)
        return False