from src.models import Person


class MockPersonService:
    def add_mock_person_from_cache(
        self, monkeypatch, person_id: str = None, in_cache: bool = True
    ):
        resp = {
            "uuid": person_id,
            "full_name": "Jennifer Hale",
            "films": [
                {
                    "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
                    "roles": ["actor"],
                },
                {
                    "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
                    "roles": ["actor"],
                },
                {
                    "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
                    "roles": ["actor"],
                },
                {
                    "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
                    "roles": ["actor"],
                },
            ],
        }

        async def mock(_, person_id):
            if in_cache:
                return Person(**resp)
            return None

        monkeypatch.setattr(
            "src.services.person.PersonService._person_from_cache", mock
        )

    def add_mock_get_person_elastic(
        self,
        monkeypatch,
        person_id: str = None,
        full_name: str = "Jennifer Hale",
        in_es: bool = True,
    ):
        resp = {
            "id": person_id,
            "full_name": full_name,
        }

        async def mock(_, person_id):
            if in_es:
                person = Person(**resp)
                person.films = [
                    {
                        "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
                        "roles": ["actor"],
                    },
                ]
                return person
            return None

        monkeypatch.setattr(
            "src.services.person.PersonService._get_person_elastic", mock
        )

    def add_mock_enrich(self, monkeypatch, person: Person = None):
        async def mock(_, person):
            if person:
                person.films = [
                    {
                        "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
                        "roles": ["actor"],
                    },
                    {
                        "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
                        "roles": ["actor"],
                    },
                ]
                return person
            return None

        monkeypatch.setattr(
            "src.services.person.PersonService._enrich_person", mock
        )
