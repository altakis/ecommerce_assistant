import json

import requests

product_catalog = None
product_catalog_src = (
    "https://gist.githubusercontent.com/altakis/962ab969a13ee892f3f29ffeca89ba9b/raw"
)


def load_product_catalog():
    if product_catalog is not None:
        return product_catalog
    response = requests.get(product_catalog_src)
    if response.status_code == 200:
        return response.json()
