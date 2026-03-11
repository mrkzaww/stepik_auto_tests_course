from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_text(self):
        # Сообщение о добавлении товара содержит название товара
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def get_basket_total_text(self):
        # Сообщение о стоимости корзины содержит цену товара
        return self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text

    def should_be_correct_product_name_in_message(self, expected_name):
        actual_name = self.get_success_message_text()
        assert expected_name == actual_name, \
            f"Product name in message is '{actual_name}', expected '{expected_name}'"

    def should_be_correct_price_in_basket_total(self, expected_price):
        actual_price = self.get_basket_total_text()
        assert expected_price == actual_price, \
            f"Basket total price is '{actual_price}', expected '{expected_price}'"