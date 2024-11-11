import json
import requests

product_catalog = None
product_catalog_src = "https://gist.githubusercontent.com/altakis/962ab969a13ee892f3f29ffeca89ba9b/raw"

def load_product_catalog():
    if product_catalog is not None:
        return product_catalog
    response = requests.get(product_catalog_src)
    if response.status_code == 200:
        return response.json() 

def __getProductInfoByName(product_name=None):
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
