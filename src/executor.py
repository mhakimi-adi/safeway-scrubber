import requests
from lib.utils import paramBuilder, headerBuilder, dataCleanup
import lib.constants as constants
import json
import time
from pathlib import Path
import pandas
from sqlalchemy import create_engine
from datetime import datetime
import os

# Handles the business logic for product_list_test request
def product_list_test():
    session = requests.Session()

    load = session.get(
        constants.PROD_LIST_URI,
        params=paramBuilder(
            rows=constants.DEFAULT_ROWS,
            start=constants.DEFAULT_START,
            category_id=constants.DEFAULT_CATEGORY_ID,
            storeid=constants.DEFAULT_STORE_ID,
        ),
        headers=headerBuilder()
    )

    return load

# Handles the business logic for product_list_category request
def product_list_category(
    results: int,
    offset: int,
    category_id: str,
    storeid: int
):
    session = requests.Session()

    load = session.get(
        constants.PROD_LIST_URI,
        params=paramBuilder(
            rows=results,
            start=offset,
            category_id=category_id,
            storeid=storeid,
        ),
        headers=headerBuilder()
    )

    return load

# Handles the business logic for product_list_all request
def product_list_all():
    total = 0
    results = []
    for data in constants.Categories:

        # print("Total: ", total)
        # print("Results: ", len(results))
        # print("Category: ", data.value)

        load = product_list_category(
            results=constants.DEFAULT_ROWS,
            offset=constants.DEFAULT_START,
            category_id=data.value,
            storeid=constants.DEFAULT_STORE_ID
        )

        total += load.json()['response']['numFound']
        curr_total = load.json()['response']['numFound']
        results += load.json()['response']['docs']

        time.sleep(30)

        while len(results) < total:
            temp = product_list_category(
                results=constants.DEFAULT_ROWS,
                offset=curr_total - (total-len(results)),
                category_id=data.value,
                storeid=constants.DEFAULT_STORE_ID
            )
            results += temp.json()['response']['docs']

    path = Path(__file__).parent / "../data/data.json"
    with open(path, 'w') as f:
        json.dump(results, f)

    return json.dumps({'total': total})

# Handles the business logic for product_list_sync request
def product_list_sync():
    # Get data to insert
    df = pandas.read_json(os.path.join(os.getcwd(), "data/data.json"))
    df = dataCleanup(df)
    total = 0

    # Create SQLAlchemy engine to connect to MySQL Database
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}:{port}/{db}"
                    .format(
                        host=constants.SFS_DB_HOST,
                        port=constants.SFS_DB_PORT,
                        db=constants.SFS_DB_DBS,
                        user=constants.SFS_DB_USER,
                        pw=constants.SFS_DB_PASS
                    )
    )

    # Table timestamp
    now = datetime.now() # current date and time
    date_time = now.strftime("%m_%d_%Y")
    name = "safeway_scrubber_{date_time}".format(date_time=date_time)

    # Save to DB
    try:
        total = df.to_sql(
            name,
            engine,
            if_exists='replace',
            index=True
        )
    except Exception as e:
        print("Error :: product_list_sync() :: ", e)
        return json.dumps({'total': total})
    
    return json.dumps({'total': total})