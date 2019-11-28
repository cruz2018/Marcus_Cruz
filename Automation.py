import time

from selenium import webdriver  #
import unittest

#class LogingTest(unitest.TestCase):

   
def test_setup(cls):
     global browser
     cls.browser = webdriver.Firefox()  #
     cls.browser.implicitly_wait(10)
        #browser.maximize_window()
        # Say something
        # Semething else


def test_login_valid(self):
    self.browser.get("https://opensource-demo.orangehrmlive.com/")
    self.browser.find_element_by_id("txtUsername").send_keys("Admin")
    self.browser.find_element_by_id("txtPassword").send_keys("admin123")
    self.browser.find_element_by_id("btnLogin").click()
    self.browser.find_element_by_id("welcome").click()
    time.sleep(2)

def tearDownClass(cls):
    cls.browser.close()
    cls.browser.quit()
    print("Test Complete")
