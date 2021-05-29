from pages.registeration_page import RegistrationUserPage
from pages.locators import HomePageLocators, RegisterationUserPage, PagePaths


def test_adding_a_product_under_admin(browser):
    client = RegistrationUserPage(browser)
    client.open(url=PagePaths.MAIN)
    client.click_to_element(*HomePageLocators.MY_ACCOUNT)
    client.click_to_element(*HomePageLocators.CHECK_REGISTER)
    client.registration_user()
    client.waiting_for_text_present(*RegisterationUserPage.SUCCESS_MESSAGE)
