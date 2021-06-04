from selenium.webdriver.common.by import By


class PagePaths:
    HOST_GLOBAL = 'https://demo.opencart.com/'
    HOST_LOCAL = 'http://192.168.31.162/'

    MAIN = HOST_LOCAL
    PRODUCT = f'{MAIN}index.php?route=product/product&path=57&product_id=49'
    CATALOG = f'{MAIN}index.php?route=product/category&path=20'
    LOGIN = f'{MAIN}index.php?route=account/login'
    LOGIN_ADMIN = f'{MAIN}admin/'


class HomePageLocators:
    ADD_TO_BASKET = (By.XPATH, '''//button[@onclick="cart.add('43');"]''')
    ADD_TO_WISHLIST = (By.XPATH, '''//button[@onclick="wishlist.add('43');"]''')
    COMPARE = (By.XPATH, '''//button[@onclick="compare.add('43');"]''')
    PRICE = (By.CSS_SELECTOR, 'div.product-layout:nth-child(1) .price')
    PRICE_TAX = (By.CSS_SELECTOR, 'div.product-layout:nth-child(1) .price-tax')
    USER_PROFILE = (By.ID, 'user-profile')
    LOGOUT_BUTTON = (By.CSS_SELECTOR, '.fa.fa-sign-out')
    CATALOG = (By.XPATH, '''//a[contains(text(),' Catalog')]''')
    PRODUCTS = (By.XPATH, '''//a[contains(text(),'Products')]''')
    MY_ACCOUNT = (By.CSS_SELECTOR, '.dropdown-toggle .fa.fa-user')
    CHECK_REGISTER = (By.XPATH, '''//a[contains(text(),'Register')]''')
    CURRENCY_ICON = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    US_DOLLAR = (By.XPATH, '//button[@name="USD"]')
    DOLLAR_ICON = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle strong', '$')


class ProductPageLocators:
    INPUT_QUALITY = (By.ID, 'input-quantity')
    ADD_TO_CART = (By.CSS_SELECTOR, 'button#button-cart')
    BACK_TO_HOME = (By.CSS_SELECTOR, '.fa.fa-home')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content div.col-sm-4 h1')
    PRICE = (By.CSS_SELECTOR, '#content div.col-sm-4 ul li h2')


class ProductsPageLocators:
    PRODUCT = 'autotest_product'
    ADD_NEW = (By.XPATH, '//a[@data-original-title="Add New"]')
    PRODUCT_NAME = (By.ID, 'input-name1')
    META_TEG_TITLE = (By.ID, 'input-meta-title1')
    DATA = (By.XPATH, '''//a[contains(text(),'Data')]''')
    MODEL = (By.ID, 'input-model')
    SAVE_BUTTON = (By.XPATH, '//button[@data-original-title="Save"]')
    SEARCH_LIST_PRODUCTS = '''//div[@class="table-responsive"]//td[contains(text(),'{}')]'''
    CHECKBOX_PRODUCT = '//td/img[@alt="{}"]/preceding::td[1]'
    REMOVE_BUTTON = (By.CSS_SELECTOR, 'button.btn.btn-danger')


class CatalogPageLocators:
    LIST_VIEW = (By.ID, 'list-view')
    GRID_VIEW = (By.ID, 'grid-view')
    COMPARE_TOTAL = (By.ID, 'compare-total')
    SORT_BY = (By.XPATH, '//select[@id="input-sort"]/option[@selected="selected"]')
    SHOW = (By.XPATH, '//select[@id="input-limit"]/option[@selected="selected"]')


class LoginPageLocators:
    BUTTON_LOGIN = (By.XPATH, '//input[@value="Login"]')
    BUTTON_CONTINIUE = (By.CSS_SELECTOR, "#content .row div.col-sm-6:nth-child(1) a")
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    NAME_FORM = (By.CSS_SELECTOR, "#content .row div.col-sm-6:nth-child(2) h2")


class LoginAdminPageLocators:
    TEXT_LOGIN = 'user'
    TEXT_PASSWORD = 'bitnami'
    LOGIN_ADMIN = (By.ID, 'input-username')
    PASSWORD_ADMIN = (By.ID, 'input-password')
    FORGOTTEN_PASSWORD = (By.CSS_SELECTOR, '.help-block')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.btn.btn-primary')
    NAME_FORM = (By.CSS_SELECTOR, '.panel-heading')


class RegisterationUserPage:
    NAME = 'autotest_user'
    PASS = 'autotest1234'
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    PRIVACY = (By.XPATH, '//input[@type="checkbox" and @name="agree"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, '.btn.btn-primary')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#content h1', 'Your Account Has Been Created!')
