import random

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    import requests

    # Search GitHub's repositories for requests
    session = requests.Session()

    load = session.get(
        'https://www.safeway.com/abs/pub/xapi/v1/aisles/products?pagename=aisles&rows=14&start=0&search-type=category&featured=false&q=&sort=&pp=none&banner=safeway&channel=pickup&storeid=1965&category-id=1_1&url=https://www.safeway.com&pageurl=https://www.safeway.com&request-id=3&search-uid=',
        headers = {'Ocp-Apim-Subscription-Key': 'e914eec9448c4d5eb672debf5011cf8f'}
    )

    # Inspect some attributes of the `requests` repository
    json_response = load.json()
    return json_response
