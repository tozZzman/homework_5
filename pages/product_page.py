from .base_page import BasePage
from .locators import ProductsPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product(self, name, meta, model):
        self.click_to_element(*ProductsPageLocators.ADD_NEW)
        self.enter_text(*ProductsPageLocators.PRODUCT_NAME, text=name)
        self.enter_text(*ProductsPageLocators.META_TEG_TITLE, text=meta)
        self.click_to_element(*ProductsPageLocators.DATA)
        self.enter_text(*ProductsPageLocators.MODEL, text=model)
        self.click_to_element(*ProductsPageLocators.SAVE_BUTTON)

    def check_the_product_on_the_list(self, name):
        try:
            self.waiting_for_text_present(By.XPATH, ProductsPageLocators.SEARCH_LIST_PRODUCTS.format(name), text=name)
        except TimeoutError:
            raise AssertionError('Продукт отсуствует в списке')

    def check_the_product_not_on_the_list(self, name):
        try:
            self.waiting_for_text_not_present(By.XPATH, ProductsPageLocators.SEARCH_LIST_PRODUCTS.format(name),
                                              text=name)
        except TimeoutError:
            raise AssertionError('Продукт присутствует в списке')

    def remove_products(self, name):
        products = self.browser.find_elements(By.XPATH, ProductsPageLocators.CHECKBOX_PRODUCT.format(name))
        for product in products:
            product.click()
        self.click_to_element(*ProductsPageLocators.REMOVE_BUTTON)
        self.browser.switch_to_alert().accept()
