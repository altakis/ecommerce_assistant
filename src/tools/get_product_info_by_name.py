from .utils import product_catalog, load_product_catalog


def _getProductInfoByName(product_name=None):
    product_catalog = load_product_catalog()

    results = []
    for product in product_catalog:
        # Check if the product matches the search criteria
        if (product_name and product_name.lower() in product["Name"].lower()) or (
            product_name and product_name.lower() in product["Description"].lower()
        ):
            # Format the product details to return
            product_info = {
                "ProductID": product["ProductID"],
                "Name": product["Name"],
                "Description": product["Description"],
                "Price": product["Price"],
                "StockAvailability": product["StockAvailability"],
                "LastStockUpdate": product["LastStockUpdate"],
                "Category": product["Category"],
                "Supplier": product["Supplier"],
                "Discount": product["Discount"],
                "IsOrganic": product["IsOrganic"],
                "Rating": product["Rating"],
            }
            results.append(product_info)
    return results


_getProductInfoByName_tool_definition = {
    "type": "function",
    "function": {
        "name": "__getProductInfoByName",
        "description": "Queries the product catalog for all the products that match a name search parameter.",
        "parameters": {
            "type": "object",
            "properties": {
                "product_name": {
                    "type": "string",
                    "description": "The name of the product to search for.",
                },
            },
            "required": ["product_name"],
        },
    },
}
