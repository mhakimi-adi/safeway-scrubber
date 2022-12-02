from enum import Enum
import os

# API Schema
DEFAULT_MEDIA_TYPE = 'application/json'

# Product List URI
PROD_LIST_URI = 'https://www.safeway.com/abs/pub/xapi/v1/aisles/products'

# Product List by Category Params
class Categories(Enum):
    BABY = '1_1'
    BEVS = '1_5'
    BREAD = '1_2'
    CEREAL = '1_7'
    CANNED = '1_9'
    SPICE = '1_20'
    CANDY = '1_24'
    DAIRY = '1_11'
    DELI = '1_12'
    FLOWER = '1_14'
    FROZEN = '1_15'
    PRODUCE = '1_23'
    PASTA = '1_6'
    INTL = '1_13'
    MEAT = '1_19'
    CLEAN = '1_18'
    PERSONAL = '1_17'
    PET = '1_22'
    WINE = '1_29'

DEFAULT_ROWS = 100
DEFAULT_START = 0
DEFAULT_CATEGORY_ID = Categories.INTL.value
DEFAULT_STORE_ID = 1965

# MySQL DB Connections
SFS_DB_HOST = os.getenv('SFS_DB_HOST')
SFS_DB_PORT = os.getenv('SFS_DB_PORT')
SFS_DB_USER = os.getenv('SFS_DB_USER')
SFS_DB_PASS = os.getenv('SFS_DB_PASS')
SFS_DB_DBS = os.getenv('SFS_DB_DBS')