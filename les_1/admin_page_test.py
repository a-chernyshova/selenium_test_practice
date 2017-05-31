# -*- coding: utf-8 -*-
from les_1 import login_test


URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


# check if page has no h1 tag
def check_h1(browser, element):
    if not browser.find_elements_by_css_selector('h1'):
        print('Error: {} has no h1'.format(element))


# walk through all menu entries
def walk_through_menu(browser):
    list_menu = browser.find_elements_by_xpath('//*[@id="app-"]/a')
    num_menu = len(list_menu)
    for i in range(num_menu):
        browser.find_elements_by_xpath('//*[@id="app-"]/a')[i].click()
        element = browser.find_elements_by_xpath('//*[@id="app-"]/a')[i].text
        check_h1(browser, element)
        list_submenu = browser.find_elements_by_css_selector('.docs li')
        num_submenu = len(list_submenu)
        if list_submenu:
            for i in range(num_submenu):
                browser.find_elements_by_css_selector('.docs li')[i].click()
                element = browser.find_elements_by_css_selector('.docs li')[i].text
                check_h1(browser, element)


if __name__ == '__main__':
    browser = login_test.login(URL, LOGIN, PASSWORD)
    walk_through_menu(browser)
    login_test.close(browser)
