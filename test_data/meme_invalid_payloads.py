invalid_meme_payloads = [
    {
        "text": "Invalid URL meme",
        "url": "not-a-valid-url",
        "tags": ["test"],
        "info": {"author": "bad"}
    },
    {
        "text": "",
        "url": "http://example.com/image.jpg",
        "tags": ["test"],
        "info": {"author": "bad"}
    },
    {
        "text": "Tags not list",
        "url": "http://example.com/image.jpg",
        "tags": "notalist",
        "info": {"author": "bad"}
    },
    {
        "text": "Invalid info",
        "url": "http://example.com/image.jpg",
        "tags": ["test"],
        "info": {"author": 123}
    },
    {
        "text": "Meme with missing fields",
        "url": "",
        "tags": ["test"],
        "info": {"author": "test_user"}
    },
]