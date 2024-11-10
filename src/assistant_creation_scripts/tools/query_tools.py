import json
import os
from pathlib import Path

# Get the path to the src folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Get path to test_data folder
path_to_test_data = os.path.join(BASE_DIR, "test_data")

# Construct the path to the JSON file inside test_data
path_to_catalog_data = os.path.join(path_to_test_data, "grocery_store_mock_data.json")

# Load the JSON data
with open(path_to_catalog_data, "r") as file:
    product_catalog = json.load(file)


def __getProductInfoByName(product_name=None):
    results = []
    for product in product_catalog:
        # Check if the product matches the search criteria
        if product_name and product_name.lower() in product["Name"].lower():
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


def __getProductInfoByNameOrCategory(product_name=None, category=None):
    results = []
    for product in product_catalog:
        # Check if the product matches the search criteria
        if (product_name and product_name.lower() in product["Name"].lower()) or (
            category and product["Category"].lower() == category.lower()
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
