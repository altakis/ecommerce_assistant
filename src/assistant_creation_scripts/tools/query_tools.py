from .query_funcs import *


{
  "name": "query_catalog",
  "description": "Queries the product catalog for names and stock information.",
  "parameters": {
    "type": "object",
    "properties": {
      "product_name": {
        "type": "string",
        "description": "The name of the product to search for."
      },
      "category": {
        "type": "string",
        "description": "The category of products to search for."
      }
    },
    "required": []
  }
}
