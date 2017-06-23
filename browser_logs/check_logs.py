from les_1 import login_test

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


def open_item():
    driver.find_elements_by_xpath('//*[@id="app-"]/a')[1].click()
    table = driver.find_element_by_class_name('dataTable')
    category = table.find_elements_by_class_name('row')[1]
    category.find_element_by_tag_name('a').click()
    items = driver.find_elements_by_xpath('//*[@id="content"]/form/table/tbody/tr/td[3]/a')[1:]
    items_list = []
    for item in items:
        link = item.get_attribute('href')
        items_list.append(link)
    return items_list


def check_logs(items_list):
    for link in items_list:
        driver.get(link)
        logs = driver.get_log("browser")
        if logs:
            pass
        else:
            for l in logs:
                print(l)


if __name__ == '__main__':
    try:
        driver = login_test.login(URL, LOGIN, PASSWORD)
        driver.implicitly_wait(5)
        check_logs(open_item())
    finally:
        driver.close()
