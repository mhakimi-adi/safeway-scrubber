# Sets the params for safeway product GET request
def paramBuilder(
        rows: int,
        start: int,
        category_id: str,
        storeid: int,
    ):
    return {
        'pagename': 'aisles',
        'rows': rows,
        'start': start,
        'search-type': 'category',
        'featured': False,
        'q': '',
        'sort': '',
        'pp': None,
        'banner': 'safeway',
        'channel': 'pickup',
        'storeid': storeid,
        'category-id': category_id,
        'url': 'https://www.safeway.com',
        'pageurl': 'https://www.safewaycom',
        'request-id': 1,
        'search-uid': ''       
    }

# Sets the headers for safeway product GET request
def headerBuilder():
    return {
        'Ocp-Apim-Subscription-Key': 'e914eec9448c4d5eb672debf5011cf8f'
    }