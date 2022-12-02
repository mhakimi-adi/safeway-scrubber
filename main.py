from fastapi import FastAPI, Response
import src.executor as executor
import lib.constants as constants

app = FastAPI()

# Product Sample List
@app.get("/products/sample")
def product_list_test():
    return executor.product_list_test().json()

# Product List by Category and Store
@app.get("/products"
    + "/results/{results}"
    + "/offset/{offset}"
    + "/category_id/{category_id}"
    + "/storeid/{storeid}"
)
def product_list_category(
    results: int,
    offset: int,
    category_id: str,
    storeid: int
):
    return executor.product_list_category(
        results=results,
        offset=offset,
        category_id=category_id,
        storeid=storeid
    ).json()

# Product List All Categories by Store
@app.get("/products/all")
def product_list_all():
    return Response(
        content=executor.product_list_all(),
        media_type=constants.DEFAULT_MEDIA_TYPE
    )

# Product List Save to MySQL
@app.get("/products/sync")
def product_list_sync():
    return Response(
        content=executor.product_list_sync(),
        media_type=constants.DEFAULT_MEDIA_TYPE
    )