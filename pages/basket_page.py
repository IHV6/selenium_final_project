from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert self.browser.current_url, "Basket link is not found"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Basket is empty message is not presented, but should be"

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Basket is empty message is not presented, but should be"
