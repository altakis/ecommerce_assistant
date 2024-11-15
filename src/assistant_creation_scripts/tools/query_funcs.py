import json
import os
from pathlib import Path

# Get the path to the src folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Get path to test_data folder
path_to_test_data = os.path.join(BASE_DIR, "assistant_creation_scripts")
path_to_test_data = os.path.join(path_to_test_data, "test_data")

# Construct the path to the JSON file inside test_data
path_to_catalog_data = os.path.join(path_to_test_data, "grocery_store_mock_data.json")

# Load the JSON data
with open(path_to_catalog_data, "r") as file:
    product_catalog = json.load(file)


def __getProductInfoByName(product_name=None):
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


def __getProductInfoByCategory(category=None):
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


def __getProductStockById(product_id):
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
