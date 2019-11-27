import time

from selenium import webdriver  #
import unitest

class LogingTest(unitest.TestCase):

   

    def test_setup(cls):
        global browser
        cls.browser = webdriver.Firefox()  #
        cls.browser.implicitly_wait(10)
        #browser.maximize_window()
        # Say something
        # Semething else


def test_login():
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id("txtUsername").send_keys("Admin")

    # Password
    browser.find_element_by_id("txtPassword").send_keys("admin123")

    # Click button
    browser.find_element_by_id("btnLogin").click()

    # The page will load and the user will land into the Welcome page

    # Once the user are in the Welcome page than the user will logou from the system

    browser.find_element_by_id("welcome").click()
    time.sleep(2)

    # Close the browser
    browser.close()
    # quite 
    browser.quit()
    print("Test Complete")
