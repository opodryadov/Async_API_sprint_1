from fastapi import Query


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


def query_params(
    query: str | None = Query(default=""),
    sort: str | None = Query(default=""),
    page_number: int | None = Query(default=1, ge=1),
    page_size: int | None = Query(default=50, ge=1, le=200),
) -> dict:
    return {
        "query": query,
        "sort": get_sort(sort),
        "page_number": page_number - 1,
        "page_size": page_size,
    }
