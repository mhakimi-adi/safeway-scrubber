import pandas

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

## Prepares dataset for mysql db
# TODO:
# - investigate null values
# - investigate duplicate (id, upc, pid) rows
def dataCleanup(df):
    ### 3 Nested Columns
    df_channel_eligibility = pandas.read_json(
        df['channelEligibility'].to_json()
    ).T
    for (columnName, columnData) in df_channel_eligibility.items():
        df_channel_eligibility.rename(columns = {
            columnName:'eligibility_{columnName}'.format(
                columnName=columnName
            )},
            inplace = True
        )

    df_channel_inventory = pandas.read_json(
        df['channelInventory'].to_json()
    ).T
    for (columnName, columnData) in df_channel_inventory.items():
        df_channel_inventory.rename(columns = {
            columnName:'inventory_{columnName}'.format(
                columnName=columnName
            )},
            inplace = True
        )

    df_prod_review = pandas.read_json(
        df['productReview'].to_json()
    ).T

    # Drop Unusable Nested Columns
    df = df.drop(
        ['channelEligibility', 'channelInventory', 'productReview'],
        axis=1
    )

    # Merge Clean Data with
    df = df.merge(df_channel_eligibility, left_index=True, right_index=True)
    df = df.merge(df_channel_inventory, left_index=True, right_index=True)
    df = df.merge(df_prod_review, left_index=True, right_index=True)
    
    # Clean up Data Types
    for (columnName, columnData) in df.items():
        if df[columnName].dtypes == object:
            df[columnName] = df[columnName].astype("string")
    
    return df