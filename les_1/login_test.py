# -*- coding: utf-8 -*-
from selenium import webdriver

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


def login(url, login, password):
    global browser
    browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    #browser = webdriver.Ie()
    #browser = webdriver.Opera()
    #browser = webdriver.Edge()
    #browser = webdriver.Firefox(capabilities={"marionette": False}) # old fashion
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox45\\firefox.exe",
    #                            capabilities={"marionette": False})
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
    #                            capabilities={"marionette": True})
    #browser = webdriver.Firefox(firefox_binary='C:\\Program Files(x86)\\Firefox Developer Edition\\firefox.exe')
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files(x86)\\Nightly\\firefox.exe")
    browser.get(url)
    browser.find_element_by_name('username').send_keys(login)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('login').click()
    return browser


def work_with_coockies(browser):
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())
    browser.refresh()


def close(browser):
    browser.quit()


if __name__ == '__main__':
    try:
        work_with_coockies(login(URL, LOGIN, PASSWORD))
    finally:
        close(browser)
