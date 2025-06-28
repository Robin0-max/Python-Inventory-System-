# File containing product data
PRODUCT_FILE = "Product.txt"

def save_products(products):
    """
    Saves the products dictionary to the file.
    """
    try:
        # Open product file in write mode
        with open(PRODUCT_FILE, "w") as file:
            # Write each product as comma-separated line
            for product in products.values():
                # Create CSV line from product data
                line = product["name"] + "," + product["brand"] + "," + str(product["quantity"]) + "," + str(product["cost_price"]) + "," + product["origin"]
                # Write line to file
                file.write(line + "\n")
    except Exception as e:
        # Handle file write errors
        print("An error occurred while saving products: " + str(e))
