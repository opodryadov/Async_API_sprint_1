from fastapi import Query


async def query_params(
    query: str | None = Query(default=""),
    page_size: int | None = Query(default=50),
    page_number: int | None = Query(default=1),
):
    return {"query": query, "page_size": page_size, "page_number": page_number}
