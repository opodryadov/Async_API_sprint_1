FILM_INFO = {
    "uuid": "27b726f2-40e9-4d81-b608-57f7c41bfe54",
    "title": "WWE: John Morrison - Rock Star",
    "imdb_rating": 6.6,
    "description": None,
    "genre": [
        {
            "uuid": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
            "name": "Action"
        }
    ],
    "actors": [
        {
            "uuid": "4f9d60e0-f06c-470a-afc7-edb2daa30a09",
            "full_name": "Mark Calaway"
        },
        {
            "uuid": "70de3b14-aeaa-4a79-abbb-e99bfd83b776",
            "full_name": "Ric Flair"
        },
        {
            "uuid": "84c6fdb8-d636-417f-8ccd-6aa1f78bd30e",
            "full_name": "Adam Birch"
        },
        {
            "uuid": "8f1a9c3f-ed03-45e7-82ff-5e9966039d4e",
            "full_name": "John Hennigan"
        }
    ],
    "writers": [],
    "directors": [
        {
            "uuid": "de81c526-d04e-4678-9e29-5eae7c38227f",
            "full_name": "Kevin Dunn"
        }
    ]
}

FILM_INFO_CACHE = {
    'id': '27b726f2-40e9-4d81-b608-57f7c41bfe54', 'title': 'WWE: John Morrison - Rock Star', 'imdb_rating': 6.6, 'description': None, 'genre': [{'id': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff', 'name': 'Action'}], 'actors': [{'id': '4f9d60e0-f06c-470a-afc7-edb2daa30a09', 'full_name': 'Mark Calaway'}, {'id': '70de3b14-aeaa-4a79-abbb-e99bfd83b776', 'full_name': 'Ric Flair'}, {'id': '84c6fdb8-d636-417f-8ccd-6aa1f78bd30e', 'full_name': 'Adam Birch'}, {'id': '8f1a9c3f-ed03-45e7-82ff-5e9966039d4e', 'full_name': 'John Hennigan'}], 'writers': [], 'directors': [{'id': 'de81c526-d04e-4678-9e29-5eae7c38227f', 'full_name': 'Kevin Dunn'}]
}

FILM_WITHOUT_RATING_AND_PERSONS = {
    "uuid": "32fcd689-3119-4225-8076-fdeabc553c61",
    "title": "Test Film",
    "imdb_rating": None,
    "description": "This film about testers",
    "genre": [
        {
            "uuid": "6d141ad2-d407-4252-bda4-95590aaf062a",
            "name": "Documentary"
        }
    ],
    "actors": [],
    "writers": [],
    "directors": []
}

FILM_WITHOUT_RATING_AND_PERSONS_CACHE = {
    'id': '32fcd689-3119-4225-8076-fdeabc553c61', 'title': 'Test Film', 'imdb_rating': None, 'description': 'This film about testers', 'genre': [{'id': '6d141ad2-d407-4252-bda4-95590aaf062a', 'name': 'Documentary'}], 'actors': [], 'writers': [], 'directors': []
}

SEARCH_FILMS_SORT_BY_RATING_ASC_RESPONSE = [
    {
        "uuid": "de3f7ec5-1652-49dc-bac0-f49afdbc925a",
        "title": "Tell It to a Star",
        "imdb_rating": 6.1
    },
    {
        "uuid": "0352be33-bb3a-455b-80dd-444202dff23d",
        "title": "A Five Star Life",
        "imdb_rating": 6.3
    },
    {
        "uuid": "b0752ea4-76fe-4a00-986d-71fb34f908cd",
        "title": "The Blue Star Hotel",
        "imdb_rating": 7.4
    },
    {
        "uuid": "d895fded-2ea1-4889-b93e-971c58bee8e1",
        "title": "Wishes on a Falling Star",
        "imdb_rating": 8.5
    }
]

SEARCH_FILMS_SORT_BY_RATING_ASC_IN_CACHE = [
    '{"id":"de3f7ec5-1652-49dc-bac0-f49afdbc925a","title":"Tell It to a ' 'Star","imdb_rating":6.1}', '{"id":"0352be33-bb3a-455b-80dd-444202dff23d","title":"A Five Star ' 'Life","imdb_rating":6.3}', '{"id":"b0752ea4-76fe-4a00-986d-71fb34f908cd","title":"The Blue Star ' 'Hotel","imdb_rating":7.4}', '{"id":"d895fded-2ea1-4889-b93e-971c58bee8e1","title":"Wishes on a Falling ' 'Star","imdb_rating":8.5}'
]

SEARCH_FILMS_SORT_BY_TITLE_ASC_RESPONSE = [
    {
        "uuid": "0352be33-bb3a-455b-80dd-444202dff23d",
        "title": "A Five Star Life",
        "imdb_rating": 6.3
    },
    {
        "uuid": "de3f7ec5-1652-49dc-bac0-f49afdbc925a",
        "title": "Tell It to a Star",
        "imdb_rating": 6.1
    },
    {
        "uuid": "b0752ea4-76fe-4a00-986d-71fb34f908cd",
        "title": "The Blue Star Hotel",
        "imdb_rating": 7.4
    },
    {
        "uuid": "d895fded-2ea1-4889-b93e-971c58bee8e1",
        "title": "Wishes on a Falling Star",
        "imdb_rating": 8.5
    }
]

SEARCH_FILMS_SORT_BY_TITLE_ASC_IN_CACHE = [
    '{"id":"0352be33-bb3a-455b-80dd-444202dff23d","title":"A Five Star Life","imdb_rating":6.3}', '{"id":"de3f7ec5-1652-49dc-bac0-f49afdbc925a","title":"Tell It to a Star","imdb_rating":6.1}', '{"id":"b0752ea4-76fe-4a00-986d-71fb34f908cd","title":"The Blue Star Hotel","imdb_rating":7.4}', '{"id":"d895fded-2ea1-4889-b93e-971c58bee8e1","title":"Wishes on a Falling Star","imdb_rating":8.5}'
]

SEARCH_FILMS_SORT_BY_RATING_DESC_RESPONSE = [
    {
        "uuid": "d895fded-2ea1-4889-b93e-971c58bee8e1",
        "title": "Wishes on a Falling Star",
        "imdb_rating": 8.5
    },
    {
        "uuid": "b0752ea4-76fe-4a00-986d-71fb34f908cd",
        "title": "The Blue Star Hotel",
        "imdb_rating": 7.4
    },
    {
        "uuid": "0352be33-bb3a-455b-80dd-444202dff23d",
        "title": "A Five Star Life",
        "imdb_rating": 6.3
    },
    {
        "uuid": "de3f7ec5-1652-49dc-bac0-f49afdbc925a",
        "title": "Tell It to a Star",
        "imdb_rating": 6.1
    }
]

SEARCH_FILMS_SORT_BY_RATING_DESC_IN_CACHE = [
    '{"id":"d895fded-2ea1-4889-b93e-971c58bee8e1","title":"Wishes on a Falling '  'Star","imdb_rating":8.5}',  '{"id":"b0752ea4-76fe-4a00-986d-71fb34f908cd","title":"The Blue Star '  'Hotel","imdb_rating":7.4}',  '{"id":"0352be33-bb3a-455b-80dd-444202dff23d","title":"A Five Star '  'Life","imdb_rating":6.3}',  '{"id":"de3f7ec5-1652-49dc-bac0-f49afdbc925a","title":"Tell It to a '  'Star","imdb_rating":6.1}'
]

SEARCH_FILMS_SORT_BY_TITLE_DESC_RESPONSE = [
    {
        "uuid": "d895fded-2ea1-4889-b93e-971c58bee8e1",
        "title": "Wishes on a Falling Star",
        "imdb_rating": 8.5
    },
    {
        "uuid": "b0752ea4-76fe-4a00-986d-71fb34f908cd",
        "title": "The Blue Star Hotel",
        "imdb_rating": 7.4
    },
    {
        "uuid": "de3f7ec5-1652-49dc-bac0-f49afdbc925a",
        "title": "Tell It to a Star",
        "imdb_rating": 6.1
    },
    {
        "uuid": "0352be33-bb3a-455b-80dd-444202dff23d",
        "title": "A Five Star Life",
        "imdb_rating": 6.3
    }
]

SEARCH_FILMS_SORT_BY_TITLE_DESC_IN_CACHE = [
    '{"id":"d895fded-2ea1-4889-b93e-971c58bee8e1","title":"Wishes on a Falling '  'Star","imdb_rating":8.5}',  '{"id":"b0752ea4-76fe-4a00-986d-71fb34f908cd","title":"The Blue Star '  'Hotel","imdb_rating":7.4}',  '{"id":"de3f7ec5-1652-49dc-bac0-f49afdbc925a","title":"Tell It to a '  'Star","imdb_rating":6.1}',  '{"id":"0352be33-bb3a-455b-80dd-444202dff23d","title":"A Five Star '  'Life","imdb_rating":6.3}'
]
