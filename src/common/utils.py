from fastapi import Query


class PaginateQueryParams:
    def __init__(
        self,
        page_number: int = Query(
            1,
            title="Номер страницы",
            description="Номер страницы",
            ge=1,
        ),
        page_size: int = Query(
            50,
            title="Количество записей",
            description="Количество записей на одной странице",
            ge=1,
            le=500,
        ),
    ):
        self.page_number = page_number
        self.page_size = page_size


def get_sort(field: str) -> dict:
    if not field or field not in (
        "title",
        "-title",
        "imdb_rating",
        "-imdb_rating",
    ):
        return {}

    method = "desc" if "-" in field else "asc"
    field = field.replace("-", "")
    if "title" in field:
        field = field.replace("title", "title.raw")

    return {field: method}
