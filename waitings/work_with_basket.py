from selenium import webdriver
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://localhost:8080/litecart'


def fill_out_basket(driver):
    for i in [1, 2, 3]:
        link = driver.find_elements_by_css_selector('a.link')[i].get_attribute('href')
        add_item(driver, link)
        driver.implicitly_wait(5)

    driver.get('http://127.0.0.1:8080/litecart/en/checkout')
    del_from_basket()


def del_from_basket():
    remove_list = driver.find_elements_by_name('remove_cart_item')
    for item in remove_list:
        item.click()


def add_item(driver, link):
    driver.get(link)
    size = driver.find_elements_by_name('options[Size]')
    if size:
        Select(size[0]).select_by_value('Medium')
    quantity = driver.find_element_by_name('quantity')
    num = randint(1, 5)
    quantity.send_keys(num)
    driver.find_element_by_name('add_cart_product').click()

    wait = WebDriverWait(driver, 2)
    driver.refresh()
    wait.until(EC.staleness_of(driver.find_element_by_id('cart-wrapper')))
    print('waiting')
    driver.get(URL)


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get(URL)
        fill_out_basket(driver)
    finally:
        pass
        #driver.close()
