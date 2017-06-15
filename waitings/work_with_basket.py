from selenium import webdriver
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://localhost:8080/litecart'
CHECKOUT_URL = 'http://127.0.0.1:8080/litecart/en/checkout'


def fill_out_basket(driver):
    driver.implicitly_wait(1)
    for i in [1, 2, 3]:
        link = driver.find_elements_by_css_selector('a.link')[i].get_attribute('href')
        add_item(driver, link)

    driver.find_element_by_css_selector('#cart a.link').click()
    del_from_basket()


def del_from_basket():
    wait = WebDriverWait(driver, 2)
    driver.refresh()
    while driver.find_elements_by_name('cart_form'):
        to_remove = driver.find_element_by_name('remove_cart_item')
        to_remove.click()
        item = driver.find_element_by_name('cart_form')
        wait.until(EC.staleness_of(item))


def add_item(driver, link):
    driver.implicitly_wait(1)
    basket = driver.find_element_by_id('cart-wrapper')
    items_amount = basket.find_element_by_css_selector('.quantity').text

    driver.get(link)
    wait = WebDriverWait(driver, 2)
    driver.refresh()

    size = driver.find_elements_by_name('options[Size]')
    if size:
        Select(size[0]).select_by_value('Medium')
    quantity = driver.find_element_by_name('quantity')
    quantity.clear()
    num = randint(1, 5)
    quantity.send_keys(num)
    driver.find_element_by_name('add_cart_product').click()

    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="cart"]/a[2]/span[1]'), str(int(items_amount) + num)))
    # basket = driver.find_element_by_id('cart-wrapper')
    # changed_amount_of_items = basket.find_element_by_css_selector('.quantity').text

    driver.get(URL)


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get(URL)
        fill_out_basket(driver)
    finally:
        driver.close()
