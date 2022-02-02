from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.add_product_to_basket()
        self.should_be_price()
        self.find_product_price_value()
        self.should_be_product_name()
        self.should_be_product_name_in_breadcrumb()
        self.should_be_product_name_in_alertinner()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "button add_to_basket not found"

    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_VALUE), "price not found"

    def find_product_price_value(self):
        price = self.find_flout_value_in_element(*ProductPageLocators.PRICE_VALUE)
        price_basket = self.find_flout_value_in_element(*ProductPageLocators.PRICE_BASKET_VALUE)
        assert price == price_basket, "price is wrong"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name not found"

    def should_be_product_name_in_breadcrumb(self):
        product_name = self.find_text_value(*ProductPageLocators.PRODUCT_NAME)
        breadcrumb_name = self.find_text_value(*ProductPageLocators.BREADCRUMB_PRODUCT_NAME)
        assert product_name == breadcrumb_name, "product name in breadcrumb is wrong"

    def should_be_product_name_in_alertinner(self):
        product_name = self.find_text_value(*ProductPageLocators.PRODUCT_NAME)
        alertinner_name = self.find_text_value(*ProductPageLocators.ALERTINNER_PRODUCT_NAME)
        assert (product_name + " has been added to your basket.") == alertinner_name, \
            "product name in alertinner is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERTINNER_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ALERTINNER_PRODUCT_NAME), \
            "Success message is not disappeared, but should be"
