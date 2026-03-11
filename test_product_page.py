import pytest
from selenium import webdriver
from pages.product_page import ProductPage

@pytest.fixture
def browser():
    from selenium import webdriver
    driver = webdriver.Chrome()  # или webdriver.Firefox() и т.д.
    yield driver
    driver.quit()

def test_guest_can_add_product_to_basket(browser):
    # Открываем страницу товара с параметром promo
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # Добавляем товар в корзину
    page.add_to_basket()

    # Решаем математический алерт и получаем код
    page.solve_quiz_and_get_code()

    # Проверяем, что название товара совпадает с названием в сообщении о добавлении
    product_name = page.get_product_name()
    page.should_be_correct_product_name_in_message(product_name)

    # Проверяем, что цена товара совпадает со стоимостью корзины в сообщении
    product_price = page.get_product_price()
    page.should_be_correct_price_in_basket_total(product_price)