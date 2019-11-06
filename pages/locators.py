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