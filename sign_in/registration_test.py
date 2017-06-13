from selenium import webdriver
from selenium.webdriver.support.ui import Select
from random import randint
import string

URL = 'http://127.0.0.1:8080/litecart/en/'
TESTDATA_1 = {'first_name': 'Anastasia', 'last_name': 'Chernyshova', 'address1': '711 Sip streer',
               'postcode': '07087', 'city': 'Union city', 'zone': 'New Jersey',
              'phone': '6462562859', 'password': 'awesome123'}


def create_email():
    alphabet = string.ascii_lowercase
    email = ''
    for i in range(10):
        email += alphabet[randint(0, 25)]
    return email + '@gmail.com'


def go_to_registration(driver):
    link = driver.find_element_by_link_text('New customers click here')
    link.click()


def fill_out_reg_form(driver, test_data, email):
    first_name_fiels = driver.find_element_by_css_selector('input[name=firstname]')
    first_name_fiels.send_keys(test_data['first_name'])
    lastname_field = driver.find_element_by_css_selector('input[name=lastname')
    lastname_field.send_keys(test_data['last_name'])
    address1_field = driver.find_element_by_css_selector('input[name=address1')
    address1_field.send_keys(test_data['address1'])
    postcode_field = driver.find_element_by_css_selector('input[name=postcode')
    postcode_field.send_keys(test_data['postcode'])
    city_field = driver.find_element_by_css_selector('input[name=city')
    city_field.send_keys(test_data['city'])
    email_field = driver.find_element_by_css_selector('input[name=email')
    email_field.send_keys(email)
    phone = driver.find_element_by_css_selector('input[name=phone')
    phone.send_keys(test_data['phone'])
    password = driver.find_element_by_css_selector('input[name=password')
    password.send_keys(test_data['password'])
    confirmed_password = driver.find_element_by_css_selector('input[name=confirmed_password')
    confirmed_password.send_keys(test_data['password'])

    Select(driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value('NJ')
    driver.find_element_by_css_selector('button[name=create_account]').click()


def logout(driver):
    driver.find_element_by_link_text('Logout').click()


def login(driver, test_data, email):
    email_field = driver.find_element_by_css_selector('input[name=email]')
    email_field.send_keys(email)
    password = driver.find_element_by_css_selector('input[name=password]')
    password.send_keys(test_data['password'])
    driver.find_element_by_css_selector('button[name=login]').click()


if __name__ == '__main__':
    try:
        email = create_email()
        driver = webdriver.Chrome()
        driver.get(URL)
        go_to_registration(driver)
        fill_out_reg_form(driver, TESTDATA_1, email)
        print('INFO:', email, ' is registered correctly')
        logout(driver)
        login(driver, TESTDATA_1, email)
        logout(driver)
    finally:
        driver.close()
