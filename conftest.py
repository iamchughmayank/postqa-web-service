from time import sleep
from random import randint
import pytest
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import allure
from allure_commons.types import AttachmentType


driver = None
remote = None
uname = None
passwd = None


def pytest_addoption(parser):
    parser.addoption("--remote", action="store_true", help = "If given, it will try to connect to Selenium at 4444 remote docker")
    parser.addoption("--uname", action="store", help = "username with which login has to be done", required=True)
    parser.addoption("--passwd", action="store", help = "password with which login has to be done",required = True)

def pytest_configure(config):
    global remote
    global uname
    global passwd
    remote = config.getoption("--remote")
    uname = config.getoption("--uname")
    passwd = config.getoption("--passwd")


class Setup():
    def __init__(self,test_ws_name,test_ws_desc,uname,passwd):
        desired_caps = {}
        desired_caps = DesiredCapabilities.CHROME.copy()
        self.test_ws_name = test_ws_name
        self.test_ws_desc = test_ws_desc
        self.uname = uname
        self.passwd = passwd
        global driver
        if remote:
            driver = webdriver.Remote ('http://127.0.0.1:4444/wd/hub', desired_caps)
        else:
            driver = webdriver.Chrome(desired_capabilities=desired_caps)
        self.driver = driver
        self.wait = WebDriverWait (driver, 20)
        print('Driver has been globalized. It can be accessed anywhere in conftest for hooks')

def generate_test_data():
    test_ws_name = 'MyTestWorkspace'+str(randint(1,100))
    test_ws_desc = 'MyTestWorkspaceDesc'+str(randint(1,100))
    return test_ws_name,test_ws_desc
@pytest.fixture(scope='session')
def resource(request):
    test_ws_name,test_ws_desc = generate_test_data()
    setupObj = Setup(test_ws_name,test_ws_desc,uname,passwd)
    return setupObj

@pytest.fixture(scope='function',autouse=True)
def capture_screen(request):
    #before test tasks
    yield
    #after tests tasks
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)