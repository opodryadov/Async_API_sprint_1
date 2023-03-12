from src.models import Person


class MockRedis:
    def add_mock_get(
        self, monkeypatch, person_id: str = None, in_cache: bool = True
    ):
        resp = {
            "id": person_id,
            "full_name": "Jennifer Hale",
            "role": "actor",
            "film_ids": [
                "32064806-8196-4037-b758-dd5b5d274b59",
                "2a090dde-f688-46fe-a9f4-b781a985275e",
                "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
                "c4d36327-b330-4506-a63d-fef69d3f2f8a",
            ],
        }

        async def mock(_, person_id):
            if in_cache:
                return Person(**resp)
            return None

        monkeypatch.setattr(
            "src.services.person.PersonService._person_from_cache", mock
        )


class MockElastic:
    def add_mock_get(
        self, monkeypatch, person_id: str = None, in_es: bool = True
    ):
        resp = {
            "id": person_id,
            "full_name": "Jennifer Hale",
        }

        async def mock(_, person_id):
            if in_es:
                person = Person(**resp)
                person.role = "actor"
                person.film_ids = [
                    "32064806-8196-4037-b758-dd5b5d274b59",
                    "2a090dde-f688-46fe-a9f4-b781a985275e",
                    "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
                    "c4d36327-b330-4506-a63d-fef69d3f2f8a",
                ]
                return person
            return None

        monkeypatch.setattr(
            "src.services.person.PersonService._get_person_elastic", mock
        )
