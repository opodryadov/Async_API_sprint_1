from src.services.person import FilmShort


docs_actors = [
    {
        "_index": "movies",
        "_type": "_doc",
        "_id": "0657217e-9efa-48fe-be08-6ca29bcaf042",
        "_score": 7.726653,
        "_source": {
            "id": "0657217e-9efa-48fe-be08-6ca29bcaf042",
            "imdb_rating": 6.5,
            "title": "Top Star",
            "description": "Tae-sik's on he road to success when he goes from being.",
            "genre": [
                {"id": "1cacff68-643e-4ddd-8f57-84b62538081a", "name": "Drama"}
            ],
            "actors_names": [
                "Yi-hyeon So",
                "Tae-woong Eom",
                "Min-jun Kim",
                "Jin-geun Kim",
            ],
            "writers_names": ["Seok-Hwan Choi", "Joong-Hoon Park"],
            "directors_names": ["Joong-Hoon Park"],
            "actors": [
                {
                    "id": "3329a06f-aded-4148-9485-3fa941500afb",
                    "name": "Yi-hyeon So",
                },
                {
                    "id": "3a31847f-8772-4587-af41-667e8205206d",
                    "name": "Tae-woong Eom",
                },
                {
                    "id": "9c9cb347-ddf4-4e00-b807-741ba4394e93",
                    "name": "Min-jun Kim",
                },
                {
                    "id": "9cc232b1-0ebb-416f-889b-3d5bee9cfdd5",
                    "name": "Jin-geun Kim",
                },
            ],
            "writers": [
                {
                    "id": "9628808d-43c9-4eb8-9263-a90c1f873ae2",
                    "name": "Seok-Hwan Choi",
                },
                {
                    "id": "a90d678c-72f2-4e19-b921-f7a44783c70d",
                    "name": "Joong-Hoon Park",
                },
            ],
            "directors": [
                {
                    "id": "a90d678c-72f2-4e19-b921-f7a44783c70d",
                    "name": "Joong-Hoon Park",
                }
            ],
        },
    }
]

bb = [
    FilmShort(
        id="0657217e-9efa-48fe-be08-6ca29bcaf042",
        title="Top Star",
        imdb_rating=6.5,
    )
]
