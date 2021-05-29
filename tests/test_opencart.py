import pages.locators as lc
from pages.base_page import BasePage


def test_search_title(browser, url):
    bp = BasePage(browser)
    bp.open(url)
    bp.check_title(title='Your Store', timeout=3)


def test_search_items_on_the_home_page(browser):
    bp = BasePage(browser)
    bp.open(lc.PagePaths.MAIN)
    bp.waiting_for_element_present(*lc.HomePageLocators.ADD_TO_BASKET)
    bp.waiting_for_element_present(*lc.HomePageLocators.ADD_TO_WISHLIST)
    bp.waiting_for_element_present(*lc.HomePageLocators.COMPARE)
    bp.waiting_for_text_present(*lc.HomePageLocators.PRICE, text='$602.00')
    bp.waiting_for_text_present(*lc.HomePageLocators.PRICE_TAX, text='Ex Tax: $500.00')


def test_search_items_on_the_product_page(browser, helper, url):
    bp = BasePage(browser)
    bp.open(lc.PagePaths.PRODUCT)
    bp.waiting_for_element_present(*lc.ProductPageLocators.INPUT_QUALITY)
    bp.waiting_for_element_present(*lc.ProductPageLocators.ADD_TO_CART)
    bp.waiting_for_element_present(*lc.ProductPageLocators.BACK_TO_HOME)
    bp.waiting_for_text_present(*lc.ProductPageLocators.PRODUCT_NAME, text='Samsung Galaxy Tab 10.1')
    bp.waiting_for_text_present(*lc.ProductPageLocators.PRICE, text='$241.99')


def test_search_items_on_the_catalog_page(browser, url):
    bp = BasePage(browser)
    bp.open(lc.PagePaths.CATALOG)
    bp.waiting_for_element_present(*lc.CatalogPageLocators.LIST_VIEW)
    bp.waiting_for_element_present(*lc.CatalogPageLocators.GRID_VIEW)
    bp.waiting_for_element_present(*lc.CatalogPageLocators.COMPARE_TOTAL)
    bp.waiting_for_text_present(*lc.CatalogPageLocators.SORT_BY, text='Default')
    bp.waiting_for_text_present(*lc.CatalogPageLocators.SHOW, text='15')


def test_search_items_on_the_login_page(browser, url):
    bp = BasePage(browser)
    bp.open(lc.PagePaths.LOGIN)
    bp.waiting_for_element_present(*lc.LoginPageLocators.BUTTON_LOGIN)
    bp.waiting_for_element_present(*lc.LoginPageLocators.BUTTON_CONTINIUE)
    bp.waiting_for_element_present(*lc.LoginPageLocators.EMAIL)
    bp.waiting_for_element_present(*lc.LoginPageLocators.PASSWORD)
    bp.waiting_for_text_present(*lc.LoginPageLocators.NAME_FORM, text='Returning Customer')


def test_search_items_on_the_login_admin_page(browser, url):
    bp = BasePage(browser)
    bp.open(lc.PagePaths.LOGIN_ADMIN)
    bp.waiting_for_element_present(*lc.LoginAdminPageLocators.LOGIN_ADMIN)
    bp.waiting_for_element_present(*lc.LoginAdminPageLocators.PASSWORD_ADMIN)
    bp.waiting_for_element_present(*lc.LoginAdminPageLocators.FORGOTTEN_PASSWORD)
    bp.waiting_for_element_present(*lc.LoginAdminPageLocators.BUTTON_LOGIN)
    bp.waiting_for_text_present(*lc.LoginAdminPageLocators.NAME_FORM, text='Please enter your login details.')
