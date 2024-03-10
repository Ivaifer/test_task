from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from test_UI.enums.global_enums import GlobalErrorMessages
from .base_page import BasePage
from .locators import SearchPageLocators, BasketLocators, ProductLocators, MainPageLocators


class SearchPage(BasePage):
    # Проверка, что открыта именно страница поиска.
    def is_search_page_open(self):
        assert self.is_element_present(
            *SearchPageLocators.SEARCH_PAGE_COUNT), GlobalErrorMessages.SEARCH_PAGE_NOT_OPEN

    # Добавление товара в корзину.
    def add_to_basket(self):
        self.driver.find_element(
            *SearchPageLocators.ADD_TO_BASKET_BUTTON).click()

    # Ввод названия товара в окно поиска.
    def find_product_in_search_window(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(
            SearchPageLocators.ADD_TO_BASKET_BUTTON))
        self.driver.find_element(*MainPageLocators.SEARCH_WINDOW).send_keys(
            *ProductLocators.PRODUCT_NAME + Keys.RETURN)

    # Проверка совпадения названия продукта в корзине.
    def product_name_match_in_basket(self):
        name_in_basket = self.driver.find_element(
            *BasketLocators.PRODUCT_NAME_IN_BASKET).text
        assert name_in_basket == ProductLocators.PRODUCT_NAME, GlobalErrorMessages.WRONG_NAME_IN_BASKET

    # Удаление продукта из корзины.
    def delete_product_from_basket(self):
        self.driver.find_element(
            *BasketLocators.DELETE_FROM_BASKET_BUTTON).click()

    # Проверка на удаление товара из корзины.
    def basket_is_empty(self):
        assert self.is_element_present(
            *BasketLocators.BASKET_IS_EMPTY), GlobalErrorMessages.BASKET_NOT_EMPTY

    # Открытие коризны.
    def open_basket(self):
        self.driver.find_element(*SearchPageLocators.BASKET_LINK).click()
