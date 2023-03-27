PAGINATION_VALIDATION_PAGE_NUMBER = {
    "detail": [
        {
            "loc": ["query", "page_number"],
            "msg": "ensure this value is greater than or equal to 1",
            "type": "value_error.number.not_ge",
            "ctx": {"limit_value": 1},
        }
    ]
}

PAGINATION_VALIDATION_PAGE_SIZE = {
    "detail": [
        {
            "loc": ["query", "page_size"],
            "msg": "ensure this value is less than or equal to 200",
            "type": "value_error.number.not_le",
            "ctx": {"limit_value": 200},
        }
    ]
}

PAGINATION_VALIDATION_PAGE_SIZE_NOT_GE = {
    "detail": [
        {
            "ctx": {"limit_value": 1},
            "loc": ["query", "page_size"],
            "msg": "ensure this value is greater than or equal to 1",
            "type": "value_error.number.not_ge",
        }
    ]
}
