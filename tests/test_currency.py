from pages.base_page import BasePage
from pages.locators import HomePageLocators, PagePaths


def test_change_currency(browser):
    client = BasePage(browser)
    client.open(url=PagePaths.MAIN)
    client.click_to_element(*HomePageLocators.CURRENCY_ICON)
    client.click_to_element(*HomePageLocators.US_DOLLAR)
    client.waiting_for_text_present(*HomePageLocators.DOLLAR_ICON)
