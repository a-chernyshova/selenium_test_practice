from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from les_1 import login_test
from random import randint
import string
import os

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'
TEST_DATA = {'status': 'enabled', 'name': 'New product', 'key_words': 'new, test, web, app',
             'desc': ' Dicta quia, natus hic saepe? Iure praesentium asperiores placeat, '
                    'repellat! Repellat et dolore harum earum numquam, delectus error. '
                    'Repudiandae tempore dicta dolorem.'}


def create_name():
    alphabet = string.ascii_lowercase
    name = ''
    for i in range(10):
        name += alphabet[randint(0, 25)]
    return name


def open_add_product_form(driver):
    driver.find_elements_by_xpath('//*[@id="app-"]/a')[1].click()
    driver.find_element_by_link_text('Add New Product').click()


def tab_click(tabname):
    tab = driver.find_element_by_link_text(tabname)
    tab.click()
    driver.implicitly_wait(5)


def fillout_form(driver, testdata):
    form = driver.find_element_by_id('tab-general')
    form.find_elements_by_css_selector('input[name=status]')[0].click()
    name_field = form.find_element_by_name('name[en]')
    namevalue = testdata['name']+str(randint(1, 100))
    name_field.send_keys(namevalue)
    code_field = form.find_element_by_name('code')
    code_field.send_keys(randint(1000, 1500))
    product_group = randint(1, 3)
    form.find_elements_by_name('product_groups[]')[product_group-1].click()
    quantity_field = form.find_element_by_name('quantity')
    quantity_field.clear()
    quantity_field.send_keys(randint(5, 20))
    img = form.find_element_by_name('new_images[]')
    img.send_keys(os.getcwd() + '/bug.jpg')
    date_from_fild = form.find_element_by_name('date_valid_from')
    date_from_fild.send_keys('10052017')
    date_to_field = form.find_element_by_name('date_valid_to')
    date_to_field.send_keys('01092017')
    # ActionChains(driver).move_to_element(date_to_field).move_by_offset(1, 1).perform()
    # ActionChains(driver).move_to_element_with_offset(date_to_field, 2, 1,).perform().click()

    tab_click('Information')
    fillout_info_tab(driver, namevalue, testdata)
    tab_click('Prices')
    fillout_price_tab(driver)
    driver.find_element_by_name('save').click()
    return namevalue


def fillout_info_tab(driver, namevalue, testdata):
    Select(driver.find_element_by_name("manufacturer_id")).select_by_value('1')
    key_words_field = driver.find_element_by_name('keywords')
    key_words_field.send_keys(testdata['key_words'])
    short_desc = driver.find_element_by_name('short_description[en]')
    short_desc.send_keys(testdata['desc'][:30])
    desc = driver.find_element_by_class_name('trumbowyg-editor')
    desc.send_keys(testdata['desc'])
    title = driver.find_element_by_name('head_title[en]')
    title.send_keys(namevalue)
    meta = driver.find_element_by_name('meta_description[en]')
    meta.send_keys(testdata['desc'][::5])


def fillout_price_tab(driver):
    purchase_field = driver.find_element_by_name('purchase_price')
    purchase_field.clear()
    price = randint(10, 50)
    purchase_field.send_keys(price)
    Select(driver.find_element_by_css_selector("select[name=purchase_price_currency_code]")).select_by_value('USD')
    price_field = driver.find_element_by_name('prices[USD]')
    price_field.send_keys(price + 3)
    price_with_tax = driver.find_element_by_name('gross_prices[USD]')
    price_with_tax.clear()
    price_with_tax.send_keys(str((price + 3) * 1.07))


def check_created_product(namevalue):
    table = driver.find_element_by_class_name('dataTable')
    newproduct = table.find_elements_by_link_text(namevalue)
    if len(newproduct) == 1:
        print(namevalue, ' is successfully created')
    else:
        print(namevalue, 'is not created')


if __name__ == '__main__':
    try:
        driver = login_test.login(URL, LOGIN, PASSWORD)
        open_add_product_form(driver)
        check_created_product(fillout_form(driver, TEST_DATA))
    finally:
        driver.close()
