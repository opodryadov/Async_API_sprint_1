PERSON_WRITER = {
    "uuid": "dbac6947-e620-4f92-b6a1-dae9a3b07422",
    "full_name": "Damon Lindelof",
    "films": [
        {
            "uuid": "6ecc7a32-14a1-4da8-9881-bf81f0f09897",
            "roles": ["writer"],
        }
    ],
}

CACHE_PERSON_WRITER = {
    "id": "dbac6947-e620-4f92-b6a1-dae9a3b07422",
    "full_name": "Damon Lindelof",
    "films": None,
}

PERSON_ACTOR = {
    "films": [
        {"roles": ["actor"], "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e"},
        {"roles": ["actor"], "uuid": "32064806-8196-4037-b758-dd5b5d274b59"},
        {"roles": ["actor"], "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a"},
        {"roles": ["actor"], "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a"},
    ],
    "full_name": "Jennifer Hale",
    "uuid": "00395304-dd52-4c7b-be0d-c2cd7a495684",
}

CACHE_PERSON_ACTOR = {
    "films": None,
    "full_name": "Jennifer Hale",
    "id": "00395304-dd52-4c7b-be0d-c2cd7a495684",
}

PERSON_WRITER_DIRECTOR = {
    "uuid": "b66db341-5dcd-4aaf-b536-050b59979357",
    "full_name": "Rian Johnson",
    "films": [
        {
            "uuid": "12a8279d-d851-4eb9-9d64-d690455277cc",
            "roles": ["writer", "director"],
        }
    ],
}

CACHE_PERSON_WRITER_DIRECTOR = {
    "films": None,
    "full_name": "Rian Johnson",
    "id": "b66db341-5dcd-4aaf-b536-050b59979357",
}

PERSON_NOT_ROLE = {
    "uuid": "a5a8f573-3cee-4c3v-8a2b-91cb9f55250a",
    "full_name": "Tori Lucas",
    "films": [],
}

CACHE_PERSON_NOT_ROLE = {
    "films": None,
    "full_name": "Tori Lucas",
    "id": "a5a8f573-3cee-4c3v-8a2b-91cb9f55250a",
}

PERSON_WRITER_FILMS = [
    {
        "uuid": "6ecc7a32-14a1-4da8-9881-bf81f0f09897",
        "title": "Star Trek Into Darkness",
        "imdb_rating": 7.7,
    }
]

CACHE_PERSON_WRITER_FILMS = [
    '{"id":"6ecc7a32-14a1-4da8-9881-bf81f0f09897","title":"Star Trek Into Darkness","imdb_rating":7.7,"description":"When the USS Enterprise crew is called back home, they find an unstoppable force of terror from within their own organization has detonated the fleet and everything it stands for, leaving our world in a state of crisis. With a personal score to settle, Captain Kirk leads a manhunt to a war-zone world to capture a one-man weapon of mass destruction. As our space heroes are propelled into an epic chess game of life and death, love will be challenged, friendships will be torn apart, and sacrifices must be made for the only family Kirk has left: his crew.","genre":[{"id":"120a21cf-9097-479e-904a-13dd7198c1dd","name":"Adventure"},{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"6c162475-c7ed-4461-9184-001ef3d9f26e","name":"Sci-Fi"}],"actors":[{"id":"4a416628-4a36-431c-9121-513674dae840","full_name":"Zoe Saldana"},{"id":"8a34f121-7ce6-4021-b467-abec993fc6cd","full_name":"Zachary Quinto"},{"id":"9f38323f-5912-40d2-a90c-b56899746f2a","full_name":"Chris Pine"},{"id":"afa7c253-6702-47d7-a451-cf2bc9350310","full_name":"Karl Urban"}],"writers":[{"id":"6960e2ca-889f-41f5-b728-1e7313e54d6c","full_name":"Gene Roddenberry"},{"id":"82b7dffe-6254-4598-b6ef-5be747193946","full_name":"Alex Kurtzman"},{"id":"9b58c99a-e5a3-4f24-8f67-a038665758d6","full_name":"Roberto Orci"},{"id":"dbac6947-e620-4f92-b6a1-dae9a3b07422","full_name":"Damon Lindelof"}],"directors":[{"id":"a1758395-9578-41af-88b8-3f9456e6d938","full_name":"J.J. Abrams"}]}'
]

PERSON_ACTOR_FILMS = [
    {
        "uuid": "2a090dde-f688-46fe-a9f4-b781a985275e",
        "title": "Star Wars: Knights of the Old Republic",
        "imdb_rating": 9.6,
    },
    {
        "uuid": "32064806-8196-4037-b758-dd5b5d274b59",
        "title": "Kinect Star Wars",
        "imdb_rating": 6.1,
    },
    {
        "uuid": "4fdffe40-e77f-4fb2-96ad-47319e3ddd2a",
        "title": "Star Trek: Starfleet Command: Orion Pirates",
        "imdb_rating": 6.6,
    },
    {
        "uuid": "c4d36327-b330-4506-a63d-fef69d3f2f8a",
        "title": "Star Wars: Jedi Knight - Jedi Academy",
        "imdb_rating": 8.5,
    },
]

CACHE_PERSON_ACTOR_FILMS = [
    '{"id":"2a090dde-f688-46fe-a9f4-b781a985275e","title":"Star Wars: Knights of the Old Republic","imdb_rating":9.6,"description":"Four thousand years before the fall of the Republic, before the fall of the Jedi, a great war was fought, between the armies of the Sith and the forces of the Republic. A warrior is chosen to rescue a Jedi with a power important to the cause of the Republic, but in the end, will the warrior fight for the Light Side of the Force, or succumb to the Darkness?","genre":[{"id":"120a21cf-9097-479e-904a-13dd7198c1dd","name":"Adventure"},{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"b92ef010-5e4c-4fd0-99d6-41b6456272cd","name":"Fantasy"}],"actors":[{"id":"00395304-dd52-4c7b-be0d-c2cd7a495684","full_name":"Jennifer Hale"},{"id":"2802ff93-f147-49cc-a38b-2f787bd2b875","full_name":"John Cygan"},{"id":"578593ee-3268-4cd4-b910-8a44cfd05b73","full_name":"Rafael Ferrer"},{"id":"bccbbbb6-be40-44f5-a025-204bcfcf2667","full_name":"Raphael Sbarge"}],"writers":[{"id":"1bc82e3e-d9ea-4da0-a5ea-69ba20b94373","full_name":"Lukas Kristjanson"},{"id":"1e8d746d-72d2-4da2-ad20-651154cfb158","full_name":"Michael Gallo"},{"id":"61bffbdc-910e-47b9-8b04-43b5f27807b4","full_name":"James Ohlen"},{"id":"63a787ba-dd3f-4176-a894-9970b5c43a12","full_name":"Drew Karpyshyn"},{"id":"8778550c-90c6-4180-a6ac-eba956f0ce59","full_name":"David Gaider"},{"id":"91c4ca66-e3e1-4932-8447-aadd67fd67b1","full_name":"Peter Thomas"},{"id":"b29e255d-644d-4e16-9018-c1bcb49934e5","full_name":"Lynn Taylor"},{"id":"f7337af0-21aa-445f-aecf-4794c0faa811","full_name":"Brett Rector"}],"directors":[{"id":"1a9e7e1f-393b-455d-a76f-d3ad2b33673e","full_name":"Casey Hudson"}]}',
    '{"id":"32064806-8196-4037-b758-dd5b5d274b59","title":"Kinect Star Wars","imdb_rating":6.1,"description":null,"genre":[{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"6c162475-c7ed-4461-9184-001ef3d9f26e","name":"Sci-Fi"}],"actors":[{"id":"00395304-dd52-4c7b-be0d-c2cd7a495684","full_name":"Jennifer Hale"},{"id":"35ded0cd-785e-4f61-80f1-08538b34f660","full_name":"Nolan North"},{"id":"5237aac5-f652-4aa5-9061-55bb007cd7be","full_name":"Tom Kane"},{"id":"d9f1ecbd-98b7-4aa4-a82e-da87cdb12b8e","full_name":"Jean Gilpin"}],"writers":[],"directors":[{"id":"1b4d95d8-b093-49f3-b67a-1f4fd7589180","full_name":"Ali Donovan"},{"id":"9b475aa1-8a72-4af1-ac01-3e5871298c74","full_name":"Jorg Neumann"}]}',
    '{"id":"4fdffe40-e77f-4fb2-96ad-47319e3ddd2a","title":"Star Trek: Starfleet Command: Orion Pirates","imdb_rating":6.6,"description":null,"genre":[{"id":"6c162475-c7ed-4461-9184-001ef3d9f26e","name":"Sci-Fi"}],"actors":[{"id":"00395304-dd52-4c7b-be0d-c2cd7a495684","full_name":"Jennifer Hale"},{"id":"5ab43d10-3e0c-427d-a8f4-528a504500fa","full_name":"John Mariano"},{"id":"b205193d-3697-4d82-b750-5dc624d4cbac","full_name":"Maurice LaMarche"},{"id":"dbedbfbc-67c9-4637-a215-9cc861f3dd0b","full_name":"Corey Burton"}],"writers":[{"id":"d1155857-0d84-4a2f-a631-4c0ce6411d4b","full_name":"David Ferrell"}],"directors":[]}',
    '{"id":"c4d36327-b330-4506-a63d-fef69d3f2f8a","title":"Star Wars: Jedi Knight - Jedi Academy","imdb_rating":8.5,"description":"You play a young Jedi Academy student who must help stop an evil plot by Dark Jedi to collect and use Dark Side energy for their own ends.","genre":[{"id":"1cacff68-643e-4ddd-8f57-84b62538081a","name":"Drama"},{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"b92ef010-5e4c-4fd0-99d6-41b6456272cd","name":"Fantasy"}],"actors":[{"id":"00395304-dd52-4c7b-be0d-c2cd7a495684","full_name":"Jennifer Hale"},{"id":"5fcc00db-3be6-4795-b5c6-693cf0b4793c","full_name":"Jason Marsden"},{"id":"be2c97e6-219c-43ea-b51c-0eec5e147c54","full_name":"Philip Tanzini"},{"id":"c23936f1-2695-4c16-bbdc-45211ef2a4a7","full_name":"Jeff Bennett"}],"writers":[{"id":"6d76e2c1-0a36-4b68-a221-0c71818b4ce4","full_name":"Jon Zuk"},{"id":"a884712f-46b7-4df5-8f38-73ab8789596b","full_name":"Kenn Hoekstra"},{"id":"e5fd9c50-0cda-4ed4-98a1-ad3f226efadc","full_name":"Michael Chang Gummelt"}],"directors":[]}',
]

PERSON_WRITER_DIRECTOR_FILMS = [
    {
        "uuid": "12a8279d-d851-4eb9-9d64-d690455277cc",
        "title": "Star Wars: Episode VIII - The Last Jedi",
        "imdb_rating": 7.0,
    }
]

CACHE_PERSON_WRITER_DIRECTOR_FILMS_1 = [
    '{"id":"12a8279d-d851-4eb9-9d64-d690455277cc","title":"Star Wars: Episode VIII - The Last Jedi","imdb_rating":7.0,"description":"Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.","genre":[{"id":"120a21cf-9097-479e-904a-13dd7198c1dd","name":"Adventure"},{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"6c162475-c7ed-4461-9184-001ef3d9f26e","name":"Sci-Fi"},{"id":"b92ef010-5e4c-4fd0-99d6-41b6456272cd","name":"Fantasy"}],"actors":[{"id":"26e83050-29ef-4163-a99d-b546cac208f8","full_name":"Mark Hamill"},{"id":"2d6f6284-13ce-4d25-9453-c4335432c116","full_name":"Adam Driver"},{"id":"7026c3f4-d7b8-414a-99d5-06de1788a0ee","full_name":"Daisy Ridley"},{"id":"b5d2b63a-ed1f-4e46-8320-cf52a32be358","full_name":"Carrie Fisher"}],"writers":[{"id":"a5a8f573-3cee-4ccc-8a2b-91cb9f55250a","full_name":"George Lucas"},{"id":"b66db341-5dcd-4aaf-b536-050b59979357","full_name":"Rian Johnson"}],"directors":[{"id":"b66db341-5dcd-4aaf-b536-050b59979357","full_name":"Rian Johnson"}]}'
]

CACHE_PERSON_WRITER_DIRECTOR_FILMS_2 = [
    '{"id":"12a8279d-d851-4eb9-9d64-d690455277cc","title":"Star Wars: Episode VIII - The Last Jedi","imdb_rating":7.0,"description":"Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.","genre":[{"id":"120a21cf-9097-479e-904a-13dd7198c1dd","name":"Adventure"},{"id":"3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff","name":"Action"},{"id":"6c162475-c7ed-4461-9184-001ef3d9f26e","name":"Sci-Fi"},{"id":"b92ef010-5e4c-4fd0-99d6-41b6456272cd","name":"Fantasy"}],"actors":[{"id":"26e83050-29ef-4163-a99d-b546cac208f8","full_name":"Mark Hamill"},{"id":"2d6f6284-13ce-4d25-9453-c4335432c116","full_name":"Adam Driver"},{"id":"7026c3f4-d7b8-414a-99d5-06de1788a0ee","full_name":"Daisy Ridley"},{"id":"b5d2b63a-ed1f-4e46-8320-cf52a32be358","full_name":"Carrie Fisher"}],"writers":[{"id":"a5a8f573-3cee-4ccc-8a2b-91cb9f55250a","full_name":"George Lucas"},{"id":"b66db341-5dcd-4aaf-b536-050b59979357","full_name":"Rian Johnson"}],"directors":[{"id":"b66db341-5dcd-4aaf-b536-050b59979357","full_name":"Rian Johnson"}]}'
]

PERSON_NOT_IN_FILMS = []

SEARCH_FILMS_RESPONSE = [
    {
        "uuid": "9f38323f-5912-40d2-a90c-b56899746f2a",
        "full_name": "Chris Pine",
        "films": [
            {
                "uuid": "020adfa7-7251-4fb9-b6db-07b60664cb67",
                "roles": ["actor"],
            },
            {
                "uuid": "4af6c9c9-0be0-4864-b1e9-7f87dd59ee1f",
                "roles": ["actor"],
            },
            {
                "uuid": "572170d4-9a3d-47aa-8ffa-24c6b4ea367c",
                "roles": ["actor"],
            },
            {
                "uuid": "5ebdd8a8-f324-4546-9126-5a24b63089ad",
                "roles": ["actor"],
            },
            {
                "uuid": "6ecc7a32-14a1-4da8-9881-bf81f0f09897",
                "roles": ["actor"],
            },
            {
                "uuid": "b1f1e8a6-e310-47d9-a93c-6a7b192bac0e",
                "roles": ["actor"],
            },
        ],
    }
]

SEARCH_FILMS_IN_CACHE = [
    '{"id":"9f38323f-5912-40d2-a90c-b56899746f2a","full_name":"Chris Pine","films":null}'
]

PAGINATIONS_VALIDATION = {
    "detail": [
        {
            "loc": ["query", "page_number"],
            "msg": "ensure this value is greater than or equal to 1",
            "type": "value_error.number.not_ge",
            "ctx": {"limit_value": 1},
        }
    ]
}
