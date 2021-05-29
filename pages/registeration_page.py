from .base_page import BasePage
from .locators import RegisterationUserPage


class RegistrationUserPage(BasePage):
    def registration_user(self):
        self.enter_text(*RegisterationUserPage.FIRST_NAME, text=RegisterationUserPage.NAME)
        self.enter_text(*RegisterationUserPage.LAST_NAME, text=RegisterationUserPage.NAME)
        self.enter_text(*RegisterationUserPage.EMAIL,
                        text=RegisterationUserPage.NAME[:8] + '@' + RegisterationUserPage.NAME[:8] + '.com')
        self.enter_text(*RegisterationUserPage.TELEPHONE, text='89996669999')
        self.enter_text(*RegisterationUserPage.PASSWORD, text=RegisterationUserPage.PASS)
        self.enter_text(*RegisterationUserPage.PASSWORD_CONFIRM, text=RegisterationUserPage.PASS)
        self.click_to_element(*RegisterationUserPage.PRIVACY)
        self.click_to_element(*RegisterationUserPage.CONTINUE_BUTTON)
