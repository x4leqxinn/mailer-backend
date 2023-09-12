# API version
VERSION = {
    1 : '/v1',
}   

CURRENT_VERSION = str(list(VERSION.keys())[-1]) + '.0.0'

TAGS_V1_METADATA = [
    {
        "name": "Mailer v1",
        "description": "Mailer version 1.0.0."
    },
]

TAGS_METADATA = TAGS_V1_METADATA