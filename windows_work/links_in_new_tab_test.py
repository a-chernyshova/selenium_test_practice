from selenium import webdriver
from les_1 import login_test
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


def add_new_country(driver):
    wait = WebDriverWait(driver, 2)
    driver.refresh()
    country_link = driver.find_elements_by_id('app-')[2]
    country_link.click()
    driver.find_element_by_class_name('button').click()
    table = driver.find_element_by_css_selector('#content table')
    links = table.find_elements_by_tag_name('i')
    for link in links:

        wait.until(EC.new_window_is_opened)
        link.click()
        driver.close()

if __name__ == '__main__':
    try:
        driver = login_test.login(URL, LOGIN, PASSWORD)
        driver.implicitly_wait(5)
        add_new_country(driver)
    finally:
        #driver.quit()
        pass