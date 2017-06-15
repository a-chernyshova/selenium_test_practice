from selenium import webdriver
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'http://localhost:8080/litecart'
CHECKOUT_URL = 'http://127.0.0.1:8080/litecart/en/checkout'


def fill_out_basket(driver):
    for i in [1, 2, 3]:
        link = driver.find_elements_by_css_selector('a.link')[i].get_attribute('href')
        add_item(driver, link)
        driver.implicitly_wait(5)

    driver.get(CHECKOUT_URL)
    del_from_basket()


def del_from_basket():
    remove_list = driver.find_elements_by_name('remove_cart_item')
    print(len(remove_list))
    wait = WebDriverWait(driver, 4)
    driver.refresh()
    # пока что тут полная чушь
    for item in remove_list:
        item.click()
        table = driver.find_element_by_class_name('dataTable')
        wait.until(EC.staleness_of(table))


def add_item(driver, link):
    driver.implicitly_wait(5)
    basket = driver.find_element_by_id('cart-wrapper')
    items_amount = basket.find_element_by_css_selector('.quantity').text
    print(items_amount)

    driver.get(link)
    wait = WebDriverWait(driver, 4)
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
    basket = driver.find_element_by_id('cart-wrapper')
    changed_amount_of_items = basket.find_element_by_css_selector('.quantity').text
    print(changed_amount_of_items)

    driver.get(URL)


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get(URL)
        fill_out_basket(driver)
    finally:
        #driver.close()
        pass
