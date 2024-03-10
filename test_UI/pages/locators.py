from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE_LINK = 'https://www.wildberries.ru/'
    SEARCH_WINDOW = (By.ID, 'searchInput')


class ProductLocators:
    PRODUCT_NAME = 'Laird tputty 607 5см3 (17.25г) Жидкая термопрокладка'


class SearchPageLocators:
    ADD_TO_BASKET_BUTTON = (
    By.CSS_SELECTOR, 'a.product-card__add-basket.j-add-to-basket.btn-main')
    BASKET_LINK = (
    By.CSS_SELECTOR, 'span.navbar-pc__icon.navbar-pc__icon--basket')
    SEARCH_PAGE_COUNT = (By.CSS_SELECTOR, 'span.searching-results__count')
    SEARCH_BUTTON = (By.ID, 'applySearchBtn')


class BasketLocators:
    DELETE_FROM_BASKET_BUTTON = (By.CLASS_NAME, 'btn__del.j-basket-item-del')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, 'span.good-info__good-name')
    BASKET_IS_EMPTY = (
    By.CSS_SELECTOR, 'h1.section-header.basket-empty__title')
