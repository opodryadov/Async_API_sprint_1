from src.models import Genre


class MockGenreService:
    def add_mock_genre_from_cache(
        self, monkeypatch, genre_id: str = None, in_cache: bool = True
    ):
        resp = {"uuid": genre_id, "name": "Family"}

        async def mock(_, genre_id):
            if in_cache:
                return Genre(**resp)
            return None

        monkeypatch.setattr(
            "src.services.genre.GenreService._genre_from_cache", mock
        )

    def add_mock_get_genre_elastic(
        self,
        monkeypatch,
        genre_id: str = None,
        in_es: bool = True,
    ):
        resp = {"uuid": genre_id, "name": "Family"}

        async def mock(_, genre_id):
            if in_es:
                return Genre(**resp)
            return None

        monkeypatch.setattr(
            "src.services.genre.GenreService._get_genre_elastic", mock
        )
