import time

from selenium import webdriver  #


def test_setup():
    global browser
    browser = webdriver.Firefox()  #
    browser.implicitly_wait(10)
    #browser.maximize_window()


def test_login():
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id("txtUsername").send_keys("Admin")

    # Password
    browser.find_element_by_id("txtPassword").send_keys("admin123")

    # Click button
    browser.find_element_by_id("btnLogin").click()

