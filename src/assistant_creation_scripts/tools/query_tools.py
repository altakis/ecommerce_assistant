from .package import packaged_tools_funcs

packaged_tools = []

packaged_tools.append(
    {
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
    }
)

packaged_tools.append(
    {
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
    }
)

packaged_tools.append(
    {
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
    }
)
