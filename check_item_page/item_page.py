from selenium import webdriver

URL = 'http://127.0.0.1:8080/litecart/en/'


def find_items(browser):
    page = browser.find_element_by_css_selector('div.middle')
    elements = page.find_elements_by_css_selector('a.link')
    return len(elements)


def parse_color(color):
    # rgba(204, 0, 0, 1) - make list to compare RGB value
    color = color[5:-1].split(', ')
    return color


def find_parameters(browser, num):

    for i in range(num):
        page = browser.find_element_by_css_selector('div.middle')
        element = page.find_elements_by_css_selector('a.link')[i]
        parameters = [element.get_attribute('href')]
        name = element.find_element_by_css_selector('.name').text
        print("INFO: ", name)
        parameters.append(name)
        if element.find_elements_by_css_selector('.price'):
            price = element.find_elements_by_css_selector('.price')[0].text
            parameters.append(price)
        else:
            reg_price = element.find_elements_by_css_selector('.regular-price')[0].text
            font_size_regular = element.find_element_by_css_selector('.regular-price').value_of_css_property('font-size')
            decoration = element.find_element_by_css_selector('.regular-price').value_of_css_property("text-decoration")
            decoration = decoration.split(' ')[0]
            if decoration != 'line-through':
                print(decoration, ' - style is not line-through')
            color = element.find_element_by_css_selector('.regular-price').value_of_css_property("color")
            color = parse_color(color)
            # compare RGB value
            if color[0] != color[1] and color[1] != color[2]:
                print(color, ' is not grey')

            sale = element.find_elements_by_css_selector('.campaign-price')[0].text
            font_size_campaign = element.find_element_by_css_selector('.campaign-price').value_of_css_property(
                'font-size')
            color = element.find_element_by_css_selector('.campaign-price').value_of_css_property("color")
            color = parse_color(color)
            decoration = element.find_element_by_css_selector('.campaign-price').value_of_css_property("font-weight")
            if decoration != 'bold':
                print(decoration, ' - is not bold')
            if color[1] != '0' or color[2] != '0':
                print(color, 'is not red')
            parameters.append(reg_price)
            parameters.append(sale)
            if float(font_size_campaign[:-2]) < float(font_size_regular[:-2]):
                print('fonts: ', font_size_campaign, '<',  font_size_regular)

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
    driver = webdriver.Chrome()
    driver.get(URL)
    find_parameters(driver, find_items(driver))
    driver.close()
