# -*- coding: utf-8 -*-
from selenium import webdriver

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


def login(url, login, password):
    global browser
    browser = webdriver.Firefox()
    browser.get(url)
    browser.find_element_by_name('username').send_keys(login)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('login').click()


def close(browser):
    browser.quit()


if __name__ == '__main__':
    try:
        login(URL, LOGIN, PASSWORD)
    finally:
        close(browser)
