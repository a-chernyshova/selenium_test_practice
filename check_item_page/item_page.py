from selenium import webdriver

URL = 'http://127.0.0.1:8080/litecart/en/'


def find_items(browser):
    page = browser.find_element_by_css_selector('div.middle')
    elements = page.find_elements_by_css_selector('a.link')
    num = len(elements)
    print('num of elements: ', num)
    return num


def find_parameters(browser, num):

    for i in range(num):
        parameters = []
        page = browser.find_element_by_css_selector('div.middle')
        element = page.find_elements_by_css_selector('a.link')[i]
        parameters.append(element.get_attribute('href'))
        name = element.find_element_by_css_selector('.name').text
        print("INFO: ", name)
        parameters.append(name)
        if element.find_elements_by_css_selector('.price'):
            price = element.find_elements_by_css_selector('.price')[0].text
            parameters.append(price)
        else:
            reg_price = element.find_elements_by_css_selector('.regular-price')[0].text
            sale = element.find_elements_by_css_selector('.campaign-price')[0].text
            parameters.append(reg_price)
            parameters.append(sale)

        compare_parameters(browser, parameters)


def compare_parameters(browser, parameters):
    browser.get(parameters[0])
    title = browser.find_element_by_css_selector('h1').text
    print('Name is correct:', (title == parameters[1]))
    if len(parameters) == 3:
        print('Price is correct: ', (browser.find_element_by_css_selector('.price').text == parameters[2]))
    elif len(parameters) == 4:
        print('Regular-price is correct: ', (browser.find_element_by_css_selector
                                             ('.regular-price').text == parameters[2]))
        print('Campaign-price is correct: ', (browser.find_element_by_css_selector
                                              ('.campaign-price').text == parameters[3]))
    else:
        print('smth goes wrong')
    browser.back()


if __name__ == "__main__":
    # browsers = [webdriver.Chrome(), webdriver.Firefox(), webdriver.Ie()]
    # for browser in browsers:
    #     browser.get(URL)
    driver = webdriver.Chrome()
    driver.get(URL)
    find_parameters(driver, find_items(driver))
    driver.close()
