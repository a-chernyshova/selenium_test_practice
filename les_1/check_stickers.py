# -*- coding: utf-8 -*-
from selenium import webdriver


URL = 'http://localhost:8080/litecart'
STICKER_VALUE = ['NEW', 'SALE']


def check_stickers(browser):
    page = browser.find_element_by_css_selector('div.middle')
    elements = page.find_elements_by_css_selector('a.link')
    num = len(elements)
    for i in range(num):
        divs = elements[i].find_elements_by_css_selector('div.image-wrapper div')
        count_stickers = 0
        for div in divs:
            if div.text in STICKER_VALUE:
                count_stickers += 1
            if count_stickers != 1:
                print('Amount of stickers for "{}" is incorrect'.format(elements[i].text.replace('\n', ' ')))


if __name__ == "__main__":
    browser = webdriver.Firefox()
    browser.get(URL)
    check_stickers(browser)
    browser.close()
