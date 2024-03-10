from enum import Enum

class GlobalErrorMessages(Enum):
    SEARCH_PAGE_NOT_OPEN = 'Search page not open, but should be'
    WRONG_NAME_IN_BASKET = 'The product name in the basket does not match'
    BASKET_NOT_EMPTY = 'Basket not empty'