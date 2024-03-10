import pytest

from .pages.locators import MainPageLocators
from .pages.search_page import SearchPage

@pytest.mark.ui
def test_search_product_add_to_basket_and_delete(driver):
    """Тест открывает страницу 'https://www.wildberries.ru/', находит товар,
    проверяет, что открыта страница с результатами поиска, добавляет товар в
    корзину,открывает корзину, проверяет совпадение названия товара в корзине,
    удаляет товар и проверяет, что корзину пуста"""
    page = SearchPage(driver, MainPageLocators.MAIN_PAGE_LINK)
    page.open()
    page.find_product_in_search_window()
    page.is_search_page_open()
    page.add_to_basket()
    page.open_basket()
    page.product_name_match_in_basket()
    page.delete_product_from_basket()
    page.basket_is_empty()
