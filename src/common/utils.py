from fastapi import Query


async def get_sort(field: str) -> dict:
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


async def query_params(
    query: str | None = Query(default=""),
    sort: str | None = Query(default=""),
    page_number: int | None = Query(default=1),
    page_size: int | None = Query(default=50),
) -> dict:
    return {
        "query": query,
        "sort": await get_sort(sort),
        "page_number": page_number,
        "page_size": page_size,
    }
