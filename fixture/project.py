import time
class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s" % id).click()
        time.sleep(3)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        time.sleep(3)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

