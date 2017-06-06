from selenium import webdriver
from les_1 import login_test

URL = 'http://127.0.0.1:8080/litecart/admin/?app=countries&doc=countries'
URL2 = 'http://127.0.0.1:8080/litecart/admin/?app=geo_zones&doc=geo_zones'
LOGIN = 'admin'
PASSWORD = 'admin'


def check_countries_order(browser):
    table = browser.find_element_by_css_selector('.dataTable')
    countries = table.find_elements_by_css_selector('.row a')
    countries_list = []
    for country in countries:
        if country.text != '':
            countries_list.append(country.text)

    countries_list_sorted = countries_list
    countries_list_sorted.sort()
    return countries_list == countries_list_sorted


def check_zones_order(browser):
    countries_zone_list = browser.find_elements_by_xpath('//*[@id="content"]/form/table/tbody/tr/td[6]')
    # choose countries which have zones
    links = []
    for country in countries_zone_list:
        if int(country.text) > 0:
            links.append(country.find_element_by_xpath('../td[5]/a').get_attribute('href'))

    for link in links:
        browser.get(link)
        # get list of zones
        table = browser.find_element_by_css_selector('.dataTable')
        zone_list = table.find_elements_by_xpath('//tr/td[3]')
        zone_names = []
        for zone in zone_list:
            temp = zone.text
            zone_names.append(temp)
        zone_names_sorted = zone_names
        zone_names_sorted.sort()
        print(link, '\nZones are sorted:', zone_names_sorted == zone_names)
        browser.get(URL)


def check_geo_zones(browser):
    browser.get(URL2)
    table = browser.find_element_by_css_selector('.dataTable')
    countries = table.find_elements_by_xpath('//tbody/tr/td[3]/a')
    links = []
    for country in countries:
        links.append(country.get_attribute('href'))
    for link in links:
        browser.get(link)
        rows = browser.find_elements_by_xpath('//*[@id="table-zones"]/tbody/tr/td[3]')
        zone_list = []
        for row in rows:
            options = row.find_elements_by_css_selector('option')
            for option in options:
                if option.get_attribute('selected'):
                    zone_list.append(option.get_attribute('label'))
        zone_list_sorted = zone_list
        zone_list_sorted.sort()
        print(link, '\nZones are sorted: ', zone_list == zone_list_sorted)


if __name__ == "__main__":
    driver = login_test.login(URL, LOGIN, PASSWORD)
    print('Countries order is: ', check_countries_order(driver))
    check_zones_order(driver)
    check_geo_zones(driver)
    driver.close()
