import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://localhost:8080/litecart/admin'
LOGIN = 'admin'
PASSWORD = 'admin'


def login(url, login, password):
    global browser
    browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    #browser = webdriver.Ie()
    #browser = webdriver.Opera()
    #browser = webdriver.Edge()
    #browser = webdriver.Firefox(capabilities={"marionette": False}) # old fashion
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox45\\firefox.exe",
    #                            capabilities={"marionette": False})
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
    #                            capabilities={"marionette": True})
    #browser = webdriver.Firefox(firefox_binary='C:\\Program Files(x86)\\Firefox Developer Edition\\firefox.exe')
    #browser = webdriver.Firefox(firefox_binary="c:\\Program Files(x86)\\Nightly\\firefox.exe")
    browser.get(url)
    browser.find_element_by_name('username').send_keys(login)
    browser.find_element_by_name('password').send_keys(password)
    browser.find_element_by_name('login').click()
    return browser


def work_with_coockies(browser):
    print(browser.get_cookies())
    browser.delete_all_cookies()
    print(browser.get_cookies())
    browser.refresh()


def close(browser):
    browser.quit()

@pytest.fixture
def driver(request):
    wd = webdriver.Firefox()
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_first(driver):
    driver.get("http://www.google.com/")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))

if __name__ == '__main__':
    try:
        work_with_coockies(login(URL, LOGIN, PASSWORD))
    finally:
        close(browser)

