from time import sleep
import re
import pytest
import requests
from nested_lookup import nested_lookup
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from postman.testData import constants
from postman.pageLocators import landing
from postman.pageFunctions import landingPageFunctions, workspacePageFunctions
from flaky import flaky

pytest.user_url = None

@pytest.mark.dependency()
def test_Validate_Login(resource):
    assert landingPageFunctions.navigate_to_login(resource), 'Unable to navigate to login screen'
    assert landingPageFunctions.validate_landing_screen(resource), 'Error on Login screen'
    assert landingPageFunctions.validate_login(resource), 'Unable to log into account'
    pytest.user_url = resource.driver.current_url

@pytest.mark.dependency(depends=["test_Validate_Login"])
def test_view_workspaces(resource):
    assert workspacePageFunctions.navigate_to_user_dashboard(resource,pytest.user_url)
    num_of_personal_workspaces = workspacePageFunctions.get_number_of_workspaces(resource)
    assert num_of_personal_workspaces, 'No workspaces found for user. Not even default one'
    if num_of_personal_workspaces > 1:
        print('User has more than one workspace already')

@pytest.mark.dependency(depends=["test_Validate_Login"])
def test_create_workspace(resource):
    assert workspacePageFunctions.navigate_to_user_dashboard(resource,pytest.user_url)
    assert workspacePageFunctions.create_workspace(resource), 'Workspace could not be created successfully'
        
@pytest.mark.dependency(depends=["test_create_workspace"])
def test_update_workspace(resource):
    #get workspace to be edited
    assert workspacePageFunctions.navigate_to_user_dashboard(resource,pytest.user_url)
    test_ws = workspacePageFunctions.get_workspace_by_name(resource,resource.test_ws_name)
    # test_ws = workspacePageFunctions.get_workspace_by_name(resource,ws)
    assert test_ws, 'Unable to get WS to be edited'
    assert workspacePageFunctions.navigate_to_ws(resource,test_ws), 'Unable to navigate to WS Screen'
    assert workspacePageFunctions.open_ws_menu(resource), 'Unable to open edit menu'
    assert workspacePageFunctions.rename_ws(resource), 'Unable to rename the WS'

@pytest.mark.dependency(depends=["test_create_workspace"])
def test_delete_workspace(resource):
    assert workspacePageFunctions.navigate_to_user_dashboard(resource,pytest.user_url)
    test_ws = workspacePageFunctions.get_workspace_by_name(resource,resource.test_ws_name+'_updated')
    assert test_ws, 'Unable to get WS to be deleted'
    assert workspacePageFunctions.navigate_to_ws(resource,test_ws), 'Unable to navigate to WS Screen'
    assert workspacePageFunctions.open_ws_menu(resource), 'Unable to open edit menu'
    assert workspacePageFunctions.delete_ws(resource), 'Unable to delete WS'
    assert workspacePageFunctions.navigate_to_user_dashboard(resource,pytest.user_url)
    test_ws = workspacePageFunctions.get_workspace_by_name(resource,resource.test_ws_name+'_updated')
    assert not test_ws, 'WS did not get deleted'

