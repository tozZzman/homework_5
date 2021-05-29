from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def check_title(self, title, timeout):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.title_is(title=title))
        except TimeoutException:
            raise TimeoutError("Не дождались заголовка страницы")

    def waiting_for_element_present(self, how, what, timeout=2):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            raise TimeoutError(f"Элемент не был найден в течение {timeout} секунд(-ы)")

    def waiting_for_text_not_present(self, how, what, text, timeout=2):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until_not(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutError(f"Текст отображался в течение {timeout} секунд(-ы)")

    def waiting_for_element_to_be_clickable(self, how, what, timeout=2):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.element_to_be_clickable((how, what)))
        except TimeoutException:
            raise TimeoutError(f"Элемент был не кликабелен в течение {timeout} секунд(-ы)")

    def waiting_for_text_present(self, how, what, text, timeout=2):
        try:
            wait = WebDriverWait(driver=self.browser, timeout=timeout)
            wait.until(EC.text_to_be_present_in_element((how, what), text))
        except TimeoutException:
            raise TimeoutError(f"Текст не был найден в течение {timeout} секунд(-ы)")

    def click_to_element(self, how, what):
        self.waiting_for_element_to_be_clickable(how, what)
        self.browser.find_element(how, what).click()

    def enter_text(self, how, what, text):
        self.waiting_for_element_present(how, what)
        self.browser.find_element(how, what).send_keys(text)
