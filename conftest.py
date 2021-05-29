import os
import sys
import pytest
from selenium import webdriver

sys.path.append(os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))), '..')))

from pages.login_page import LogingPage
from pages.locators import ProductsPageLocators, HomePageLocators
from pages.product_page import ProductPage


def pytest_addoption(parser):
    parser.addoption('--browser',
                     action='store',
                     help='Browser selection flag',
                     choices=['chrome', 'firefox', 'opera'],
                     default='chrome')
    parser.addoption('--url',
                     action='store',
                     help='Flag for selecting url',
                     default='https://demo.opencart.com/')


@pytest.fixture(scope='function')
def browser(request):
    br = request.config.getoption('--browser')

    if br == 'chrome':
        driver = webdriver.Chrome()
    elif br == 'firefox':
        driver = webdriver.Firefox()
    elif br == 'opera':
        driver = webdriver.Opera()
    else:
        raise ValueError(f"Driver not suported: {br}")

    request.addfinalizer(driver.quit)

    return driver


@pytest.fixture(scope='function')
def url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def admin(browser, request):
    client = LogingPage(browser)
    client.admin_authorization()

    request.addfinalizer(client.logout)

    return client


@pytest.fixture(scope='function')
def add_product(browser, admin):
    admin.click_to_element(*HomePageLocators.CATALOG)
    admin.click_to_element(*HomePageLocators.PRODUCTS)
    client = ProductPage(browser)
    client.add_product(name=ProductsPageLocators.PRODUCT, meta='test', model='test')
    client.check_the_product_on_the_list(name=ProductsPageLocators.PRODUCT)

    return client
