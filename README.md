import time

from selenium import webdriver  #


def test_setup():
    global browser
    browser = webdriver.Firefox()  #
    browser.implicitly_wait(10)
    browser.maximize_window()


def test_login():
    browser.get("https://opensource-demo.orangehrmlive.com/")
    browser.find_element_by_id("txtUsername").send_keys("Admin")
