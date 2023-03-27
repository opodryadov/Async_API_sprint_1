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

GENRE_FILMS_SORT_BY_TITLE_ASC_RESPONSE = [
    {
        "uuid": "145524fb-6c49-45c7-ade3-ec430355a3ca",
        "title": "2-Star",
        "imdb_rating": 7.4
    },
    {
        "uuid": "6657a608-2f9d-42ce-8448-e406cf1280ce",
        "title": "7 Star Grand Mantis",
        "imdb_rating": 4.9
    },
    {
        "uuid": "6067058b-a894-4062-b17d-88e3ebfe5617",
        "title": "A Few Moments with Eddie Cantor, Star of 'Kid Boots'",
        "imdb_rating": 6.5
    },
    {
        "uuid": "0993dde6-034e-46a5-8625-3a68615884ef",
        "title": "A Mock Time: A Star Trek Wedding",
        "imdb_rating": 8.2
    },
    {
        "uuid": "56a184c5-400a-4e63-8eb3-9d888235c08f",
        "title": "A Movie Star",
        "imdb_rating": 5.9
    },
    {
        "uuid": "15667b7c-337f-4c00-b1c8-a066884fc56e",
        "title": "A Star Is Bored",
        "imdb_rating": 7.7
    },
    {
        "uuid": "ce7a7670-9cb7-47c6-b64d-c62103fa559c",
        "title": "A Star for Christmas",
        "imdb_rating": 5.3
    },
    {
        "uuid": "21371dea-02cd-4936-853b-cb42651cca86",
        "title": "Alex Jones Explains the Star Wars Prequels",
        "imdb_rating": 6.2
    },
    {
        "uuid": "7c6c5f66-4322-483d-8307-655294185026",
        "title": "All About Ann: Governor Richards of the Lone Star State",
        "imdb_rating": 7.8
    },
    {
        "uuid": "a9b57067-b910-47b8-bb83-3169429c84e1",
        "title": "All Star Comedy Jam",
        "imdb_rating": 7.5
    },
    {
        "uuid": "b99e4551-231e-4df9-86f1-5037c3ce6a62",
        "title": "All Star Comedy Jam: Live from South Beach",
        "imdb_rating": 6.7
    },
    {
        "uuid": "c11df3f1-8b6a-4899-82f1-67a1c326a4b4",
        "title": "All Star Revue",
        "imdb_rating": 8.2
    },
    {
        "uuid": "7bb20f05-4f91-41a7-882f-63607544679b",
        "title": "All-Star 25th Birthday: Stars and Street Forever!",
        "imdb_rating": 5.5
    },
    {
        "uuid": "54855a4a-d242-4b87-b549-7bd2df83d70c",
        "title": "All-Star Birthday Party at Annapolis",
        "imdb_rating": 4.9
    },
    {
        "uuid": "3431e396-04be-415f-8c8c-7f1dde2330c3",
        "title": "All-Star Comedy Birthday Party from West Point",
        "imdb_rating": 6.5
    },
    {
        "uuid": "8167ee1a-61e2-4ec0-bb24-008822cde8cf",
        "title": "All-Star Party for 'Dutch' Reagan",
        "imdb_rating": 5.4
    },
    {
        "uuid": "0d5e1522-cc03-454b-b501-085348206b81",
        "title": "All-Star Party for Carol Burnett",
        "imdb_rating": 9.2
    },
    {
        "uuid": "ded3515c-3220-42f4-9ec6-0d04556229e9",
        "title": "All-Star Party for Lucille Ball",
        "imdb_rating": 8.1
    },
    {
        "uuid": "1ca9a4b7-d78d-4cee-b590-c99c063bbd67",
        "title": "All-Star Vaudeville",
        "imdb_rating": 5.8
    },
    {
        "uuid": "57b16fe9-4a0f-4621-a0de-db9b3332a1b6",
        "title": "America's All-Star Tribute to Elizabeth Taylor",
        "imdb_rating": 6.3
    },
    {
        "uuid": "5f1a4219-b533-489f-8af2-0d2692504857",
        "title": "An All-Star Toast to the Improv",
        "imdb_rating": 7.2
    },
    {
        "uuid": "489d2054-ccf2-4017-abb2-ec0bc5ec1195",
        "title": "Anything for a Pop Star",
        "imdb_rating": 4.7
    },
    {
        "uuid": "c47ef26a-b87a-49ba-bb87-c226850d6c74",
        "title": "Barney's Christmas Star",
        "imdb_rating": 6.9
    },
    {
        "uuid": "68e0a8f5-c028-4d9f-9a52-f0e22303aa3b",
        "title": "Beam Me Up - Die große Star Trek Show",
        "imdb_rating": 6
    },
    {
        "uuid": "a010b701-9a46-4a23-aa5d-b029c18353dd",
        "title": "Big Star's Little Star",
        "imdb_rating": 6.3
    },
    {
        "uuid": "4b6977e2-b3db-4f04-b83e-f091c6fcd49c",
        "title": "Brightest Star",
        "imdb_rating": 5.1
    },
    {
        "uuid": "935e418d-09f3-4de4-8ce3-c31f31580b12",
        "title": "Bucky Larson: Born to Be a Star",
        "imdb_rating": 3.2
    },
    {
        "uuid": "a1bf30bf-08ee-4000-8d9a-a1e17ab2c197",
        "title": "Buzz Lightyear of Star Command",
        "imdb_rating": 6.7
    },
    {
        "uuid": "0236282f-8ea5-418e-ab9b-13662a4688a9",
        "title": "Buzz Lightyear of Star Command: The Adventure Begins",
        "imdb_rating": 6.2
    },
    {
        "uuid": "7b1c1238-6e7f-4e8c-8911-10a749dfb8ad",
        "title": "Captain Star",
        "imdb_rating": 7.6
    },
    {
        "uuid": "b2540995-0f91-4db1-99ed-dd7bcb3976d9",
        "title": "Catch a Falling Star",
        "imdb_rating": 6
    },
    {
        "uuid": "463d7234-2af1-4e54-a353-2a8c2c269103",
        "title": "Chatur Singh Two Star",
        "imdb_rating": 1.8
    },
    {
        "uuid": "377da75d-c80e-4d7b-88ab-07a3417b5934",
        "title": "Child Star Psychologist",
        "imdb_rating": 6.8
    },
    {
        "uuid": "2d94a1e5-d216-452b-88ea-b62e76d0bc4b",
        "title": "Comedy Central's All-Star Non-Denominational Christmas Special",
        "imdb_rating": 6.1
    },
    {
        "uuid": "ce6e41a2-ac38-443a-b4ec-10307b4e0b38",
        "title": "Confessions of an Action Star",
        "imdb_rating": 2.9
    },
    {
        "uuid": "e60412c9-43d2-48c0-94a1-81c6b04af84e",
        "title": "Confessions of an Action Star",
        "imdb_rating": 2.4
    },
    {
        "uuid": "4b721889-7b44-4684-a65e-3a30135bc55e",
        "title": "DD Fist of the North Star",
        "imdb_rating": 5.4
    },
    {
        "uuid": "856bc547-0bae-4de5-8bcc-6d3f9e92d3eb",
        "title": "Dark Star",
        "imdb_rating": 6.3
    },
    {
        "uuid": "6be27471-2dd9-4989-8307-e5e96e9c38da",
        "title": "Death Star Repairmen",
        "imdb_rating": 6.4
    },
    {
        "uuid": "192b3fc9-97e2-4260-91c6-a9b91a41e520",
        "title": "Dickie Roberts: Former Child Star",
        "imdb_rating": 5.5
    },
    {
        "uuid": "273bd379-fdc8-4133-acc7-7be18ef1b699",
        "title": "Dog Star",
        "imdb_rating": 7.1
    },
    {
        "uuid": "833b1926-ef16-49a1-b41d-eddd618a036e",
        "title": "Double Digits: The Story of a Neighborhood Movie Star",
        "imdb_rating": 9.1
    },
    {
        "uuid": "3e5bbf91-a78e-4848-8118-390a29cff142",
        "title": "Ed Sullivan All-Star Comedy Special",
        "imdb_rating": 7.3
    },
    {
        "uuid": "365a95f0-37f9-4205-aa38-7fa308c709b9",
        "title": "Follow a Star",
        "imdb_rating": 6.7
    },
    {
        "uuid": "f5e487d3-6404-4bc3-b0cd-8305a3a7bfbd",
        "title": "Ford Star Jubilee",
        "imdb_rating": 7.3
    },
    {
        "uuid": "f1e279b0-5604-4242-8f7a-b1d2d6ebf4f7",
        "title": "Four Star Playhouse",
        "imdb_rating": 7.8
    },
    {
        "uuid": "c06dd0f4-d75d-4952-a81c-36837a30351b",
        "title": "Frat Star",
        "imdb_rating": 3.5
    },
    {
        "uuid": "6c38c65e-46c9-4bc4-839a-6eaadd947ad7",
        "title": "Futari wa purikyua: Splash Star",
        "imdb_rating": 8
    },
    {
        "uuid": "2bfe2cca-86e5-44d3-954f-4c215d43fc8b",
        "title": "Goal Star",
        "imdb_rating": 8.1
    },
    {
        "uuid": "fceabcf0-9879-4c76-9ad8-576802df33ff",
        "title": "Hayley Wagner, Star",
        "imdb_rating": 5
    }
]

GENRE_FILMS_SORT_BY_TITLE_ASC_IN_CACHE = [
    '{"id":"145524fb-6c49-45c7-ade3-ec430355a3ca","title":"2-Star","imdb_rating":7.4}',  '{"id":"6657a608-2f9d-42ce-8448-e406cf1280ce","title":"7 Star Grand '  'Mantis","imdb_rating":4.9}',  '{"id":"6067058b-a894-4062-b17d-88e3ebfe5617","title":"A Few Moments with '  'Eddie Cantor, Star of \'Kid Boots\'","imdb_rating":6.5}',  '{"id":"0993dde6-034e-46a5-8625-3a68615884ef","title":"A Mock Time: A Star '  'Trek Wedding","imdb_rating":8.2}',  '{"id":"56a184c5-400a-4e63-8eb3-9d888235c08f","title":"A Movie '  'Star","imdb_rating":5.9}',  '{"id":"15667b7c-337f-4c00-b1c8-a066884fc56e","title":"A Star Is '  'Bored","imdb_rating":7.7}',  '{"id":"ce7a7670-9cb7-47c6-b64d-c62103fa559c","title":"A Star for '  'Christmas","imdb_rating":5.3}',  '{"id":"21371dea-02cd-4936-853b-cb42651cca86","title":"Alex Jones Explains '  'the Star Wars Prequels","imdb_rating":6.2}',  '{"id":"7c6c5f66-4322-483d-8307-655294185026","title":"All About Ann: '  'Governor Richards of the Lone Star State","imdb_rating":7.8}',  '{"id":"a9b57067-b910-47b8-bb83-3169429c84e1","title":"All Star Comedy '  'Jam","imdb_rating":7.5}',  '{"id":"b99e4551-231e-4df9-86f1-5037c3ce6a62","title":"All Star Comedy Jam: '  'Live from South Beach","imdb_rating":6.7}',  '{"id":"c11df3f1-8b6a-4899-82f1-67a1c326a4b4","title":"All Star '  'Revue","imdb_rating":8.2}',  '{"id":"7bb20f05-4f91-41a7-882f-63607544679b","title":"All-Star 25th '  'Birthday: Stars and Street Forever!","imdb_rating":5.5}',  '{"id":"54855a4a-d242-4b87-b549-7bd2df83d70c","title":"All-Star Birthday '  'Party at Annapolis","imdb_rating":4.9}',  '{"id":"3431e396-04be-415f-8c8c-7f1dde2330c3","title":"All-Star Comedy '  'Birthday Party from West Point","imdb_rating":6.5}',  '{"id":"8167ee1a-61e2-4ec0-bb24-008822cde8cf","title":"All-Star Party for '  '\'Dutch\' Reagan","imdb_rating":5.4}',  '{"id":"0d5e1522-cc03-454b-b501-085348206b81","title":"All-Star Party for '  'Carol Burnett","imdb_rating":9.2}',  '{"id":"ded3515c-3220-42f4-9ec6-0d04556229e9","title":"All-Star Party for '  'Lucille Ball","imdb_rating":8.1}',  '{"id":"1ca9a4b7-d78d-4cee-b590-c99c063bbd67","title":"All-Star '  'Vaudeville","imdb_rating":5.8}',  '{"id":"57b16fe9-4a0f-4621-a0de-db9b3332a1b6","title":"America\'s All-Star '  'Tribute to Elizabeth Taylor","imdb_rating":6.3}',  '{"id":"5f1a4219-b533-489f-8af2-0d2692504857","title":"An All-Star Toast to '  'the Improv","imdb_rating":7.2}',  '{"id":"489d2054-ccf2-4017-abb2-ec0bc5ec1195","title":"Anything for a Pop '  'Star","imdb_rating":4.7}',  '{"id":"c47ef26a-b87a-49ba-bb87-c226850d6c74","title":"Barney\'s Christmas '  'Star","imdb_rating":6.9}',  '{"id":"68e0a8f5-c028-4d9f-9a52-f0e22303aa3b","title":"Beam Me Up - Die große '  'Star Trek Show","imdb_rating":6.0}',  '{"id":"a010b701-9a46-4a23-aa5d-b029c18353dd","title":"Big Star\'s Little '  'Star","imdb_rating":6.3}',  '{"id":"4b6977e2-b3db-4f04-b83e-f091c6fcd49c","title":"Brightest '  'Star","imdb_rating":5.1}',  '{"id":"935e418d-09f3-4de4-8ce3-c31f31580b12","title":"Bucky Larson: Born to '  'Be a Star","imdb_rating":3.2}',  '{"id":"a1bf30bf-08ee-4000-8d9a-a1e17ab2c197","title":"Buzz Lightyear of Star '  'Command","imdb_rating":6.7}',  '{"id":"0236282f-8ea5-418e-ab9b-13662a4688a9","title":"Buzz Lightyear of Star '  'Command: The Adventure Begins","imdb_rating":6.2}',  '{"id":"7b1c1238-6e7f-4e8c-8911-10a749dfb8ad","title":"Captain '  'Star","imdb_rating":7.6}',  '{"id":"b2540995-0f91-4db1-99ed-dd7bcb3976d9","title":"Catch a Falling '  'Star","imdb_rating":6.0}',  '{"id":"463d7234-2af1-4e54-a353-2a8c2c269103","title":"Chatur Singh Two '  'Star","imdb_rating":1.8}',  '{"id":"377da75d-c80e-4d7b-88ab-07a3417b5934","title":"Child Star '  'Psychologist","imdb_rating":6.8}',  '{"id":"2d94a1e5-d216-452b-88ea-b62e76d0bc4b","title":"Comedy Central\'s '  'All-Star Non-Denominational Christmas Special","imdb_rating":6.1}',  '{"id":"ce6e41a2-ac38-443a-b4ec-10307b4e0b38","title":"Confessions of an '  'Action Star","imdb_rating":2.9}',  '{"id":"e60412c9-43d2-48c0-94a1-81c6b04af84e","title":"Confessions of an '  'Action Star","imdb_rating":2.4}',  '{"id":"4b721889-7b44-4684-a65e-3a30135bc55e","title":"DD Fist of the North '  'Star","imdb_rating":5.4}',  '{"id":"856bc547-0bae-4de5-8bcc-6d3f9e92d3eb","title":"Dark '  'Star","imdb_rating":6.3}',  '{"id":"6be27471-2dd9-4989-8307-e5e96e9c38da","title":"Death Star '  'Repairmen","imdb_rating":6.4}',  '{"id":"192b3fc9-97e2-4260-91c6-a9b91a41e520","title":"Dickie Roberts: Former '  'Child Star","imdb_rating":5.5}',  '{"id":"273bd379-fdc8-4133-acc7-7be18ef1b699","title":"Dog '  'Star","imdb_rating":7.1}',  '{"id":"833b1926-ef16-49a1-b41d-eddd618a036e","title":"Double Digits: The '  'Story of a Neighborhood Movie Star","imdb_rating":9.1}',  '{"id":"3e5bbf91-a78e-4848-8118-390a29cff142","title":"Ed Sullivan All-Star '  'Comedy Special","imdb_rating":7.3}',  '{"id":"365a95f0-37f9-4205-aa38-7fa308c709b9","title":"Follow a '  'Star","imdb_rating":6.7}',  '{"id":"f5e487d3-6404-4bc3-b0cd-8305a3a7bfbd","title":"Ford Star '  'Jubilee","imdb_rating":7.3}',  '{"id":"f1e279b0-5604-4242-8f7a-b1d2d6ebf4f7","title":"Four Star '  'Playhouse","imdb_rating":7.8}',  '{"id":"c06dd0f4-d75d-4952-a81c-36837a30351b","title":"Frat '  'Star","imdb_rating":3.5}',  '{"id":"6c38c65e-46c9-4bc4-839a-6eaadd947ad7","title":"Futari wa purikyua: '  'Splash Star","imdb_rating":8.0}',  '{"id":"2bfe2cca-86e5-44d3-954f-4c215d43fc8b","title":"Goal '  'Star","imdb_rating":8.1}',  '{"id":"fceabcf0-9879-4c76-9ad8-576802df33ff","title":"Hayley Wagner, '  'Star","imdb_rating":5.0}'
]

GENRE_FILMS_SORT_BY_RATING_ASC_RESPONSE = [
    {
        "uuid": "5c568226-b6cb-4c04-b9a8-24117ec85bb2",
        "title": "Top star magazín",
        "imdb_rating": 2.9
    },
    {
        "uuid": "9db186d9-a813-4d86-8e3e-d023cc9926c8",
        "title": "Star Wars: The Last Jedi Cast Live Q&A",
        "imdb_rating": 3.9
    },
    {
        "uuid": "f9ca2c1f-dc35-471d-ad65-d9be49735210",
        "title": "Super Star",
        "imdb_rating": 3.9
    },
    {
        "uuid": "75ded9f4-1894-4996-8945-0023fe055bc0",
        "title": "The Star Jones Reynolds Report",
        "imdb_rating": 4.4
    },
    {
        "uuid": "83af8d01-580a-462e-8c96-2171385935cc",
        "title": "Jimmy Kimmel Live's All-Star Salute to Jimmy Kimmel Live!",
        "imdb_rating": 7.5
    },
    {
        "uuid": "3fd7c00f-aaff-4798-a9b7-5cf29a832698",
        "title": "Mr. Plinkett's The Star Wars Awakens Review",
        "imdb_rating": 8
    },
    {
        "uuid": "46143f45-25f5-4df9-8927-b5f7fa92e1a3",
        "title": "The Star Wars Show",
        "imdb_rating": 8
    },
    {
        "uuid": "b16d59f7-a386-467b-bea3-35e7ffbba902",
        "title": "Star Tech",
        "imdb_rating": 8.8
    }
]

GENRE_FILMS_SORT_BY_RATING_ASC_IN_CACHE = [
    '{"id":"5c568226-b6cb-4c04-b9a8-24117ec85bb2","title":"Top star '  'magazín","imdb_rating":2.9}',  '{"id":"9db186d9-a813-4d86-8e3e-d023cc9926c8","title":"Star Wars: The Last '  'Jedi Cast Live Q&A","imdb_rating":3.9}',  '{"id":"f9ca2c1f-dc35-471d-ad65-d9be49735210","title":"Super '  'Star","imdb_rating":3.9}',  '{"id":"75ded9f4-1894-4996-8945-0023fe055bc0","title":"The Star Jones '  'Reynolds Report","imdb_rating":4.4}',  '{"id":"83af8d01-580a-462e-8c96-2171385935cc","title":"Jimmy Kimmel Live\'s '  'All-Star Salute to Jimmy Kimmel Live!","imdb_rating":7.5}',  '{"id":"3fd7c00f-aaff-4798-a9b7-5cf29a832698","title":"Mr. Plinkett\'s The '  'Star Wars Awakens Review","imdb_rating":8.0}',  '{"id":"46143f45-25f5-4df9-8927-b5f7fa92e1a3","title":"The Star Wars '  'Show","imdb_rating":8.0}',  '{"id":"b16d59f7-a386-467b-bea3-35e7ffbba902","title":"Star '  'Tech","imdb_rating":8.8}'
]

GENRE_FILMS_SORT_BY_TITLE_DESC_RESPONSE = [
    {
        "uuid": "0e662af2-7ed0-45af-845e-ebc90a9d4610",
        "title": "À la recherche de la nouvelle star",
        "imdb_rating": 2.7
    },
    {
        "uuid": "96c5ff26-b615-408a-a144-137664907c48",
        "title": "Wish Upon a Star",
        "imdb_rating": 6.7
    },
    {
        "uuid": "c03a3a97-5000-4187-944d-b483a984e6f2",
        "title": "The Star of Christmas",
        "imdb_rating": 7
    },
    {
        "uuid": "416a4645-f6d4-4b71-8808-b6995bdc15f3",
        "title": "The Star of Bethlehem",
        "imdb_rating": 7.3
    },
    {
        "uuid": "134989c3-3b20-4ae7-8092-3e8ad2333d59",
        "title": "The Star Wars Holiday Special",
        "imdb_rating": 2.1
    },
    {
        "uuid": "996262ef-e565-426a-a25e-c6863eff474d",
        "title": "The Star",
        "imdb_rating": 6.2
    },
    {
        "uuid": "76ab440d-373c-4431-9cce-e71bf8dce462",
        "title": "The Shooting Star Salesman",
        "imdb_rating": 8
    },
    {
        "uuid": "73725516-9067-4b3b-ad44-8c73d330b8a8",
        "title": "The Raccoons and the Lost Star",
        "imdb_rating": 8.4
    },
    {
        "uuid": "08002477-4b59-43ed-a1d1-50688fde338f",
        "title": "The Princess with the Golden Star",
        "imdb_rating": 7.3
    },
    {
        "uuid": "efd7fc0b-a496-45f8-be2e-1faaa47680e3",
        "title": "The Prince and the Evening Star",
        "imdb_rating": 7.1
    },
    {
        "uuid": "34b15abf-cade-4f0e-8682-760b7379adee",
        "title": "The Lone Star Kid",
        "imdb_rating": 6.3
    },
    {
        "uuid": "92f246d5-c125-4362-b380-2a993f975757",
        "title": "The Christmas Star",
        "imdb_rating": 6.5
    },
    {
        "uuid": "30c9c72e-8ef6-4c52-b3bd-7f0439848be5",
        "title": "Texaco Star Theatre",
        "imdb_rating": 7.7
    },
    {
        "uuid": "5bd6b2f9-f07d-4d6c-b8d5-a9cf649f8aa7",
        "title": "Teen Star Academy",
        "imdb_rating": 7.3
    },
    {
        "uuid": "175beb94-30fb-4786-be98-052009d73541",
        "title": "Star-Studded Spoof of the New TV Season, G-Rated, with Glamour, Glitter and Gags",
        "imdb_rating": 7.1
    },
    {
        "uuid": "ea434935-cb62-4012-9138-be74435890cd",
        "title": "Star vs. the Forces of Evil",
        "imdb_rating": 8
    },
    {
        "uuid": "eb075c31-9f9a-4e14-a8ba-b777585f8afa",
        "title": "Star in the Night",
        "imdb_rating": 7.8
    },
    {
        "uuid": "8cc3c3aa-e531-4eeb-a707-08119024b3ea",
        "title": "Star Wars: The Clone Wars",
        "imdb_rating": 5.9
    },
    {
        "uuid": "ec8bad1c-7643-49b3-93b5-cee9c8c1e602",
        "title": "Star Wars: Super Bombad Racing",
        "imdb_rating": 7.5
    },
    {
        "uuid": "ac29ce6b-b33b-4733-bbb0-e96ddb33afcb",
        "title": "Star Wars: Generations",
        "imdb_rating": 6.9
    },
    {
        "uuid": "e4685c58-06eb-4575-a5e6-9932fbf84794",
        "title": "Star Wars: Forces of Destiny",
        "imdb_rating": 5
    },
    {
        "uuid": "933fe9ef-70ea-4903-8119-2c864c4fdb8b",
        "title": "Star Wars: Episode I - The Gungan Frontier",
        "imdb_rating": 6.8
    },
    {
        "uuid": "0e60f41c-cdc2-4556-ae73-a517fbbe230a",
        "title": "Star Wars: Droids",
        "imdb_rating": 6.1
    },
    {
        "uuid": "fdfc8266-5ece-4d85-b614-3cfe9be97b71",
        "title": "Star Wars: Clone Wars",
        "imdb_rating": 7.8
    },
    {
        "uuid": "a9d52337-3249-49ae-92b8-65ee9ebaf359",
        "title": "Star Wars Rebels",
        "imdb_rating": 8
    },
    {
        "uuid": "0f83f470-41d0-42c1-b6bb-aedea263cb4c",
        "title": "Star Wars Galaxy of Adventures",
        "imdb_rating": 5.1
    },
    {
        "uuid": "4c3c4c0d-1a2f-49cf-a562-f4ab67e7bf04",
        "title": "Star Wars Forces of Destiny: Volume 2",
        "imdb_rating": 6.4
    },
    {
        "uuid": "3e21bf14-ae47-40f0-b71d-459ec61eb4f8",
        "title": "Star Trek: The Game Show",
        "imdb_rating": 6.6
    },
    {
        "uuid": "db5dcded-29da-4c96-91a2-df1407f0a80a",
        "title": "Star Trek: The Animated Series",
        "imdb_rating": 7.5
    },
    {
        "uuid": "49c79cbf-5cf5-45df-95ef-89368152dc8d",
        "title": "Star Trek: Pinball",
        "imdb_rating": 6.3
    },
    {
        "uuid": "f2dc0ce0-1b3d-4e2d-b4f7-00711829f8b4",
        "title": "Star Stuff: The Story of Carl Sagan",
        "imdb_rating": 8.6
    },
    {
        "uuid": "9e3c4a97-0bca-4d0c-af93-dad143407d0f",
        "title": "Star Street: The Adventures of the Star Kids",
        "imdb_rating": 8.1
    },
    {
        "uuid": "f927a766-742d-4f2a-9f3b-bb6e65a0c00d",
        "title": "Star Search",
        "imdb_rating": 5.4
    },
    {
        "uuid": "85c22cbc-8612-4587-8eb9-3e4ddfec0692",
        "title": "Star Paws",
        "imdb_rating": 6
    },
    {
        "uuid": "cdd0d1bf-e473-4cfd-bf4a-31e42a5df212",
        "title": "Star Kid",
        "imdb_rating": 5.3
    },
    {
        "uuid": "6d647d21-0443-47f2-ab0c-c1aab661c9a1",
        "title": "Star Falls",
        "imdb_rating": 4.6
    },
    {
        "uuid": "6a251905-d6f7-44d0-8807-bc2e8960b09a",
        "title": "Star Academy",
        "imdb_rating": 3.1
    },
    {
        "uuid": "ffaec4b6-477d-4247-add0-dbe2ad91b3dd",
        "title": "Star Academy",
        "imdb_rating": 3.6
    },
    {
        "uuid": "ce98c597-42ed-4a60-af20-ec6f985d2ea2",
        "title": "Star",
        "imdb_rating": 7
    },
    {
        "uuid": "707aaaba-e6a4-4271-9a14-1de111b04259",
        "title": "Sesame Street: All-Star Alphabet",
        "imdb_rating": 8.4
    },
    {
        "uuid": "a2002931-73bc-4331-8381-c62af1ac2c46",
        "title": "Second Star to the Left",
        "imdb_rating": 7.3
    },
    {
        "uuid": "f6cfad60-864f-4591-b60c-360da7aff5a9",
        "title": "Rogue One: A Star Wars Toy Story",
        "imdb_rating": 6.4
    },
    {
        "uuid": "830857b7-64d2-4a95-98c4-b03351daff52",
        "title": "Robot Chicken: Star Wars III",
        "imdb_rating": 8.1
    },
    {
        "uuid": "d1099968-805e-4a2b-a2ec-18bbde1201ac",
        "title": "Robot Chicken: Star Wars Episode II",
        "imdb_rating": 8.1
    },
    {
        "uuid": "d77e45fc-2b84-442f-b652-caf31cb07c80",
        "title": "Robot Chicken: Star Wars",
        "imdb_rating": 8.1
    },
    {
        "uuid": "d2de739d-49e5-4308-947d-d683a3f07aca",
        "title": "Rainbow Brite and the Star Stealer",
        "imdb_rating": 6.9
    },
    {
        "uuid": "44496348-3201-45c3-848f-756d7b02b6fd",
        "title": "Puppy Star Christmas",
        "imdb_rating": 3.4
    },
    {
        "uuid": "68ce1580-1c25-4138-abe7-20c93052a170",
        "title": "Pup Star: World Tour",
        "imdb_rating": 3.8
    },
    {
        "uuid": "b577d989-9e9e-4f18-a3ba-00d79d239968",
        "title": "Pup Star: Better 2Gether",
        "imdb_rating": 4.5
    },
    {
        "uuid": "83ba0fc6-0f89-4d9a-94e0-58dcc611733b",
        "title": "Pup Star",
        "imdb_rating": 4.2
    }
]

GENRE_FILMS_SORT_BY_TITLE_DESC_IN_CACHE = [
    '{"id":"0e662af2-7ed0-45af-845e-ebc90a9d4610","title":"À la recherche de la '  'nouvelle star","imdb_rating":2.7}',  '{"id":"96c5ff26-b615-408a-a144-137664907c48","title":"Wish Upon a '  'Star","imdb_rating":6.7}',  '{"id":"c03a3a97-5000-4187-944d-b483a984e6f2","title":"The Star of '  'Christmas","imdb_rating":7.0}',  '{"id":"416a4645-f6d4-4b71-8808-b6995bdc15f3","title":"The Star of '  'Bethlehem","imdb_rating":7.3}',  '{"id":"134989c3-3b20-4ae7-8092-3e8ad2333d59","title":"The Star Wars Holiday '  'Special","imdb_rating":2.1}',  '{"id":"996262ef-e565-426a-a25e-c6863eff474d","title":"The '  'Star","imdb_rating":6.2}',  '{"id":"76ab440d-373c-4431-9cce-e71bf8dce462","title":"The Shooting Star '  'Salesman","imdb_rating":8.0}',  '{"id":"73725516-9067-4b3b-ad44-8c73d330b8a8","title":"The Raccoons and the '  'Lost Star","imdb_rating":8.4}',  '{"id":"08002477-4b59-43ed-a1d1-50688fde338f","title":"The Princess with the '  'Golden Star","imdb_rating":7.3}',  '{"id":"efd7fc0b-a496-45f8-be2e-1faaa47680e3","title":"The Prince and the '  'Evening Star","imdb_rating":7.1}',  '{"id":"34b15abf-cade-4f0e-8682-760b7379adee","title":"The Lone Star '  'Kid","imdb_rating":6.3}',  '{"id":"92f246d5-c125-4362-b380-2a993f975757","title":"The Christmas '  'Star","imdb_rating":6.5}',  '{"id":"30c9c72e-8ef6-4c52-b3bd-7f0439848be5","title":"Texaco Star '  'Theatre","imdb_rating":7.7}',  '{"id":"5bd6b2f9-f07d-4d6c-b8d5-a9cf649f8aa7","title":"Teen Star '  'Academy","imdb_rating":7.3}',  '{"id":"175beb94-30fb-4786-be98-052009d73541","title":"Star-Studded Spoof of '  'the New TV Season, G-Rated, with Glamour, Glitter and '  'Gags","imdb_rating":7.1}',  '{"id":"ea434935-cb62-4012-9138-be74435890cd","title":"Star vs. the Forces of '  'Evil","imdb_rating":8.0}',  '{"id":"eb075c31-9f9a-4e14-a8ba-b777585f8afa","title":"Star in the '  'Night","imdb_rating":7.8}',  '{"id":"8cc3c3aa-e531-4eeb-a707-08119024b3ea","title":"Star Wars: The Clone '  'Wars","imdb_rating":5.9}',  '{"id":"ec8bad1c-7643-49b3-93b5-cee9c8c1e602","title":"Star Wars: Super '  'Bombad Racing","imdb_rating":7.5}',  '{"id":"ac29ce6b-b33b-4733-bbb0-e96ddb33afcb","title":"Star Wars: '  'Generations","imdb_rating":6.9}',  '{"id":"e4685c58-06eb-4575-a5e6-9932fbf84794","title":"Star Wars: Forces of '  'Destiny","imdb_rating":5.0}',  '{"id":"933fe9ef-70ea-4903-8119-2c864c4fdb8b","title":"Star Wars: Episode I - '  'The Gungan Frontier","imdb_rating":6.8}',  '{"id":"0e60f41c-cdc2-4556-ae73-a517fbbe230a","title":"Star Wars: '  'Droids","imdb_rating":6.1}',  '{"id":"fdfc8266-5ece-4d85-b614-3cfe9be97b71","title":"Star Wars: Clone '  'Wars","imdb_rating":7.8}',  '{"id":"a9d52337-3249-49ae-92b8-65ee9ebaf359","title":"Star Wars '  'Rebels","imdb_rating":8.0}',  '{"id":"0f83f470-41d0-42c1-b6bb-aedea263cb4c","title":"Star Wars Galaxy of '  'Adventures","imdb_rating":5.1}',  '{"id":"4c3c4c0d-1a2f-49cf-a562-f4ab67e7bf04","title":"Star Wars Forces of '  'Destiny: Volume 2","imdb_rating":6.4}',  '{"id":"3e21bf14-ae47-40f0-b71d-459ec61eb4f8","title":"Star Trek: The Game '  'Show","imdb_rating":6.6}',  '{"id":"db5dcded-29da-4c96-91a2-df1407f0a80a","title":"Star Trek: The '  'Animated Series","imdb_rating":7.5}',  '{"id":"49c79cbf-5cf5-45df-95ef-89368152dc8d","title":"Star Trek: '  'Pinball","imdb_rating":6.3}',  '{"id":"f2dc0ce0-1b3d-4e2d-b4f7-00711829f8b4","title":"Star Stuff: The Story '  'of Carl Sagan","imdb_rating":8.6}',  '{"id":"9e3c4a97-0bca-4d0c-af93-dad143407d0f","title":"Star Street: The '  'Adventures of the Star Kids","imdb_rating":8.1}',  '{"id":"f927a766-742d-4f2a-9f3b-bb6e65a0c00d","title":"Star '  'Search","imdb_rating":5.4}',  '{"id":"85c22cbc-8612-4587-8eb9-3e4ddfec0692","title":"Star '  'Paws","imdb_rating":6.0}',  '{"id":"cdd0d1bf-e473-4cfd-bf4a-31e42a5df212","title":"Star '  'Kid","imdb_rating":5.3}',  '{"id":"6d647d21-0443-47f2-ab0c-c1aab661c9a1","title":"Star '  'Falls","imdb_rating":4.6}',  '{"id":"6a251905-d6f7-44d0-8807-bc2e8960b09a","title":"Star '  'Academy","imdb_rating":3.1}',  '{"id":"ffaec4b6-477d-4247-add0-dbe2ad91b3dd","title":"Star '  'Academy","imdb_rating":3.6}',  '{"id":"ce98c597-42ed-4a60-af20-ec6f985d2ea2","title":"Star","imdb_rating":7.0}',  '{"id":"707aaaba-e6a4-4271-9a14-1de111b04259","title":"Sesame Street: '  'All-Star Alphabet","imdb_rating":8.4}',  '{"id":"a2002931-73bc-4331-8381-c62af1ac2c46","title":"Second Star to the '  'Left","imdb_rating":7.3}',  '{"id":"f6cfad60-864f-4591-b60c-360da7aff5a9","title":"Rogue One: A Star Wars '  'Toy Story","imdb_rating":6.4}',  '{"id":"830857b7-64d2-4a95-98c4-b03351daff52","title":"Robot Chicken: Star '  'Wars III","imdb_rating":8.1}',  '{"id":"d1099968-805e-4a2b-a2ec-18bbde1201ac","title":"Robot Chicken: Star '  'Wars Episode II","imdb_rating":8.1}',  '{"id":"d77e45fc-2b84-442f-b652-caf31cb07c80","title":"Robot Chicken: Star '  'Wars","imdb_rating":8.1}',  '{"id":"d2de739d-49e5-4308-947d-d683a3f07aca","title":"Rainbow Brite and the '  'Star Stealer","imdb_rating":6.9}',  '{"id":"44496348-3201-45c3-848f-756d7b02b6fd","title":"Puppy Star '  'Christmas","imdb_rating":3.4}',  '{"id":"68ce1580-1c25-4138-abe7-20c93052a170","title":"Pup Star: World '  'Tour","imdb_rating":3.8}',  '{"id":"b577d989-9e9e-4f18-a3ba-00d79d239968","title":"Pup Star: Better '  '2Gether","imdb_rating":4.5}',  '{"id":"83ba0fc6-0f89-4d9a-94e0-58dcc611733b","title":"Pup '  'Star","imdb_rating":4.2}'
]

GENRE_FILMS_SORT_BY_RATING_DESC_RESPONSE = [
    {
        "uuid": "3ff3e54c-0653-45dd-9586-efcd16b32b07",
        "title": "Shadow Star Narutaru",
        "imdb_rating": 6.4
    },
    {
        "uuid": "6d6a04d9-3e89-4f66-9256-7799beca0458",
        "title": "Shuten Doji: The Star Hand Kid 4 - End Game",
        "imdb_rating": 6.2
    },
    {
        "uuid": "7ba359d3-1129-423f-a6be-3d91eee8aee4",
        "title": "Inter Star Wars: The Awaking Force",
        "imdb_rating": 6.2
    },
    {
        "uuid": "12fa1213-c3de-4b62-a3b6-8c939e2addcf",
        "title": "Star Time",
        "imdb_rating": 5.8
    },
    {
        "uuid": "845c3e65-decf-4b07-8600-d2efc8f9c652",
        "title": "Shuten Doji: The Star Hand Kid Volume 3 - Time War",
        "imdb_rating": 5.5
    },
    {
        "uuid": "9a233936-915e-4e8a-99bb-5d94a1d9eeca",
        "title": "Shuten Doji: The Star Hand Kid 2 - Demon Battle in the Firefly Field",
        "imdb_rating": 5.5
    },
    {
        "uuid": "2091fc45-78f1-493c-9da7-47ead3aca31b",
        "title": "Star Party",
        "imdb_rating": 5.2
    },
    {
        "uuid": "6c6cb534-5013-4b5f-929e-cdc5436c38aa",
        "title": "STAR [Space Traveling Alien Reject]",
        "imdb_rating": 4.6
    },
    {
        "uuid": "2ee16da4-7bc4-40da-be77-cf0a1769abd2",
        "title": "Amateur Porn Star Killer",
        "imdb_rating": 4.3
    },
    {
        "uuid": "4154ea8a-a96a-45be-bf93-7539bee29e7e",
        "title": "Star Runners",
        "imdb_rating": 4.3
    },
    {
        "uuid": "e427011c-e6e7-491b-95db-128598f26684",
        "title": "Amateur Porn Star Killer 2",
        "imdb_rating": 3.7
    },
    {
        "uuid": "40340129-96e8-49ce-a45d-2d25d17be48a",
        "title": "Star Leaf",
        "imdb_rating": 3.6
    },
    {
        "uuid": "6d408030-e673-41c5-b4ce-5d713e8483de",
        "title": "Star Crystal",
        "imdb_rating": 3.5
    },
    {
        "uuid": "15c8d623-7b06-48a9-8cdb-feedfbf6e994",
        "title": "Star Vehicle",
        "imdb_rating": 3.2
    },
    {
        "uuid": "5c855467-9c2b-491d-a179-c217ea543e93",
        "title": "Porn Star Zombies",
        "imdb_rating": 2.4
    },
    {
        "uuid": "c97c8fbc-4084-4e9b-a486-eb5fcfe6104b",
        "title": "Amateur Porn Star Killer 3: The Final Chapter",
        "imdb_rating": 2.4
    }
]

GENRE_FILMS_SORT_BY_RATING_DESC_IN_CACHE = [
    '{"id":"3ff3e54c-0653-45dd-9586-efcd16b32b07","title":"Shadow Star '  'Narutaru","imdb_rating":6.4}',  '{"id":"6d6a04d9-3e89-4f66-9256-7799beca0458","title":"Shuten Doji: The Star '  'Hand Kid 4 - End Game","imdb_rating":6.2}',  '{"id":"7ba359d3-1129-423f-a6be-3d91eee8aee4","title":"Inter Star Wars: The '  'Awaking Force","imdb_rating":6.2}',  '{"id":"12fa1213-c3de-4b62-a3b6-8c939e2addcf","title":"Star '  'Time","imdb_rating":5.8}',  '{"id":"845c3e65-decf-4b07-8600-d2efc8f9c652","title":"Shuten Doji: The Star '  'Hand Kid Volume 3 - Time War","imdb_rating":5.5}',  '{"id":"9a233936-915e-4e8a-99bb-5d94a1d9eeca","title":"Shuten Doji: The Star '  'Hand Kid 2 - Demon Battle in the Firefly Field","imdb_rating":5.5}',  '{"id":"2091fc45-78f1-493c-9da7-47ead3aca31b","title":"Star '  'Party","imdb_rating":5.2}',  '{"id":"6c6cb534-5013-4b5f-929e-cdc5436c38aa","title":"STAR [Space Traveling '  'Alien Reject]","imdb_rating":4.6}',  '{"id":"2ee16da4-7bc4-40da-be77-cf0a1769abd2","title":"Amateur Porn Star '  'Killer","imdb_rating":4.3}',  '{"id":"4154ea8a-a96a-45be-bf93-7539bee29e7e","title":"Star '  'Runners","imdb_rating":4.3}',  '{"id":"e427011c-e6e7-491b-95db-128598f26684","title":"Amateur Porn Star '  'Killer 2","imdb_rating":3.7}',  '{"id":"40340129-96e8-49ce-a45d-2d25d17be48a","title":"Star '  'Leaf","imdb_rating":3.6}',  '{"id":"6d408030-e673-41c5-b4ce-5d713e8483de","title":"Star '  'Crystal","imdb_rating":3.5}',  '{"id":"15c8d623-7b06-48a9-8cdb-feedfbf6e994","title":"Star '  'Vehicle","imdb_rating":3.2}',  '{"id":"5c855467-9c2b-491d-a179-c217ea543e93","title":"Porn Star '  'Zombies","imdb_rating":2.4}',  '{"id":"c97c8fbc-4084-4e9b-a486-eb5fcfe6104b","title":"Amateur Porn Star '  'Killer 3: The Final Chapter","imdb_rating":2.4}'
]
