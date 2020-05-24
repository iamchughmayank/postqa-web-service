from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from postman.testData import constants
from postman.pageLocators import workspaces
from selenium.common.exceptions import *
from random import randint


def get_number_of_workspaces(resource):
    try:
        workspace_container = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.workspace_container))))
        workspace_container = resource.driver.find_element_by_class_name(workspaces.workspace_container)
        personal_workspaces = workspace_container.find_elements_by_class_name(workspaces.each_workspace_container)
        return len(personal_workspaces)
        # return True
    except Exception as e:
        print(e)
        return False

def get_workspace_by_name(resource,ws_name):
    try:
        workspace_container = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,(workspaces.workspace_container)))))
        # workspace_container = resource.driver.find_element_by_class_name(workspaces.workspace_container)
        personal_workspaces = workspace_container.find_elements_by_class_name(workspaces.each_workspace_container)
        for p_ws in personal_workspaces:
            p_ws_title = p_ws.find_elements_by_tag_name('a')
            for ws_title in p_ws_title:
                if (ws_title.get_attribute('title')).strip() == ws_name:
                    return ws_title
        return None
    except Exception as e:
        print(e)
        return False

def create_workspace(resource):
    try:
        # create_btn = resource.driver.find_element_by_class_name(workspaces.create_ws_btn)
        create_btn = resource.wait.until(EC.visibility_of_element_located(((By.XPATH,'//button[text()="Create a new workspace"]'))))
        # create_btn = resource.driver.find_element_by_xpath('//button[text()="Create a new workspace"]')
        create_btn.click()
        ws_name = resource.wait.until(EC.visibility_of_element_located(((By.ID,workspaces.input_ws_name))))
        # ws_name = resource.driver.find_element_by_id(workspaces.input_ws_name)
        test_ws_name = resource.test_ws_name
        ws_name.send_keys(test_ws_name)
        ws_desc = resource.driver.find_elements_by_tag_name('textarea')
        ws_desc = ws_desc[0]
        test_ws_desc = resource.test_ws_desc
        ws_desc.send_keys(test_ws_desc)
        ws_confirm = resource.driver.find_element_by_xpath('//button[text()="Create Workspace"]')
        ws_confirm.click()
        resource.wait.until(EC.invisibility_of_element(ws_confirm))
        # active_ws_menu = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.active_ws_menu))))
        workspace_bar = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.workspacebar))))
        return True
        # ws_titles = active_ws_menu.find_elements_by_tag_name('span')
        # print(ws_titles)
        # for title in ws_titles:
        #     print(title.text)
        #     if (title.text).strip() == test_ws_name:
        #         return True
    except Exception as e:
        print(e)
        return False

def navigate_to_ws(resource,ws_title):
    try:
        ws_title.click()
        active_ws_menu = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.active_ws_menu))))
        return True
    except Exception as e:
        print(e)
        return False

def open_ws_menu(resource):
    try:
        page_btns = resource.driver.find_elements_by_class_name(workspaces.trigger_btns)
        page_btns[2].click()
        menu_box = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.opt_menu))))
        return True
    except Exception as e:
        print(e)
        return False


def rename_ws(resource):
    try:
        menu_box = resource.driver.find_element_by_class_name(workspaces.opt_menu)
        all_ops = menu_box.find_elements_by_class_name(workspaces.opts)
        for opt in all_ops:
            if ((opt.text).strip()).lower() == 'rename':
                opt.click()
                ws_name = resource.wait.until(EC.visibility_of_element_located(((By.ID,workspaces.input_ws_name))))
                ws_name_updated = resource.test_ws_name+'_updated'
                ws_name.clear()
                ws_name.send_keys(ws_name_updated)
                save_btn = resource.driver.find_element_by_xpath('//button[text()="Save Changes"]')
                save_btn.click()
                resource.wait.until(EC.invisibility_of_element(save_btn))
                break
        active_ws_menu = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.active_ws_menu))))
        ws_titles = active_ws_menu.find_elements_by_tag_name('span')
        for title in ws_titles:
            if (title.text).strip() == ws_name_updated:
                        return True
    except Exception as e:
        print(e)
        return False

def delete_ws(resource):
    try:
        menu_box = resource.driver.find_element_by_class_name(workspaces.opt_menu)
        all_ops = menu_box.find_elements_by_class_name(workspaces.opts)
        for opt in all_ops:
            if ((opt.text).strip()).lower() == 'delete':
                opt.click()
                delete_modal = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.delete_opts))))
                delete_btn = resource.driver.find_element_by_xpath('//button[text()="Delete"]')
                delete_btn.click()
                workspace_container = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.workspace_container))))
                return True
        return False
    except Exception as e:
        print(e)
        return False

def navigate_to_user_dashboard(resource,url):
    try:
        resource.driver.get(url)
        active_ws_menu = resource.wait.until(EC.visibility_of_element_located(((By.CLASS_NAME,workspaces.active_ws_menu))))
        return True
    except Exception as e:
        print(e)
        return False
    