from utils import product_catalog, load_product_catalog

def __getProductStockById(product_id):
    product_catalog = load_product_catalog()

    # Search for the product by ProductID
    for product in product_catalog:
        if product["ProductID"] == product_id:
            # Return the stock information if found
            return {
                "ProductID": product["ProductID"],
                "Name": product["Name"],
                "StockAvailability": product["StockAvailability"],
                "LastStockUpdate": product["LastStockUpdate"],
            }
    # If no product is found, return a message indicating so
    return {"error": "Product not found."}


__getProductStockById_tool_definition = {
        "type": "function",
        "function": {
            "name": "__getProductStockById",
            "description": "Queries the product catalog for a product matching an specified id",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_id": {
                        "type": "number",
                        "description": "The id of the product to search for.",
                    },
                },
                "required": ["product_id"],
            },
        },
    }

