from .utils import product_catalog, load_product_catalog


def __getProductInfoByCategory(category=None):
    product_catalog = load_product_catalog()

    results = []
    for product in product_catalog:
        # Check if the product matches the search criteria
        if category and product["Category"].lower() == category.lower():
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


__getProductInfoByCategory_tool_definition = {
    "type": "function",
    "function": {
        "name": "__getProductInfoByCategory",
        "description": "Queries the product catalog for all the products that match a category search parameter.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The category of products to search for.",
                },
            },
            "required": ["category"],
        },
    },
}
