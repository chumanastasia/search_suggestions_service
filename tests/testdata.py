PERSON_FIRST_NAME = "Исаак"
PERSON_LAST_NAME = "Левитан"
PERSON_MIDDLE_NAME = "Ильич"


RESPONSE_SUCCESS = [
    "Левитан",
    [
        "левитан",
        "левитан картины",
        "левитан художник",
        "левитан жк",
        "левитанский",
        "левитан дом у реки",
        [
            "fact",
            "Исаак Ильич Левитан",
            "левитан художник",
            "Русский живописец",
            None,
            {
                "type": "entity",
                "img": {
                    "url": "https://avatars.mds.yandex.net/get-entity_search/5631834/551758283/S122x122Smart",
                    "size": "s",
                    "cover": True,
                },
                "queryParams": {
                    "ento": "0oCghydXc0MzQ0MgbGa9U",
                    "loaded-from-suggest": "1",
                },
            },
        ],
    ],
    {"r": 10174, "log": "sgtype:BBBBBBWizard_entity"},
]

RESPONSE_NO_WIZARD_ENTITY = [
    "Левитан",
    [
        "левитан",
        "левитан картины",
        "левитан художник",
        "левитан жк",
        "левитанский",
        "левитан дом у реки",
    ],
    {"r": 10174, "log": "sgtype:BBBBBB"},
]


RESPONSE_NO_LOG = ["Исаак Ильич Левитан", [], {"r": 10174}]
