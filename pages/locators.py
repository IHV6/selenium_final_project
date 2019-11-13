from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASSWORD2 = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")
    LOGIN_EMAIL = (By.XPATH, "//input[@name='login-username']")
    LOGIN_PASSWORD = (By.XPATH, "//input[@name='login-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@name='login_submit']")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@value="Add to basket"]')
    ADD_TO_BASKET_MESSAGE = (By.XPATH, '//div[@class="alertinner "]/strong')
    PRODUCT_TITLE = (By.XPATH, '//h1')
    BASKET_TOTAL_PRICE = (By.XPATH, '//div[@class="alert alert-safe alert-noicon alert-info  fade in"]/div/p/strong')
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.XPATH, "//i[@class='icon-user']")

class BasketPageLocators():
    BASKET_IS_EMPTY = (By.XPATH, "//div[@id='content_inner']/p")
    ITEMS_TO_BUY = (By.XPATH, "//div[@class='basket-title hidden-xs']")
