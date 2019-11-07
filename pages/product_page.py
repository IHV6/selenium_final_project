from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def add_to_basket_message(self):
        message_text = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert message_text == product_title, "Value one is not equal to value two"

    def price_in_basket(self):
        total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert total_price == product_price, "Value one is not equal to value two"





