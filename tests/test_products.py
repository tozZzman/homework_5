from pages.product_page import ProductPage
from pages.locators import HomePageLocators, ProductsPageLocators


def test_adding_a_product_under_admin(browser, admin):
    admin.click_to_element(*HomePageLocators.CATALOG)
    admin.click_to_element(*HomePageLocators.PRODUCTS)
    client = ProductPage(browser)
    client.add_product(name=ProductsPageLocators.PRODUCT, meta='test', model='test')
    client.check_the_product_on_the_list(name=ProductsPageLocators.PRODUCT)


def test_remove_a_product_under_admin(browser, add_product):
    add_product.remove_products(name=ProductsPageLocators.PRODUCT)
    add_product.check_the_product_not_on_the_list(name=ProductsPageLocators.PRODUCT)
