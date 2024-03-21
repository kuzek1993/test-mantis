from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.db import DbFixture
from fixture.james import JamesHelper


class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.db = DbFixture(self)
        self.base_url = config["web"] ["baseUrl"]
        self.config = config
        self.james = JamesHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            False


    def destroy(self):
        self.wd.quit()