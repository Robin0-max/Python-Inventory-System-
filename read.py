"""Welcome to WeCare Wholesale System's program this a product inventory management system implemented in Python for a wholesale business"""

from datetime import datetime

# File containing product data
PRODUCT_FILE = "Product.txt"

def load_products():
    """
    Loads products from the file and returns them as a dictionary.
    """
    # Initialize empty dictionary to store products
    products = {}
    try:
        # Open product file in read mode
        with open(PRODUCT_FILE, "r") as file:
            # Start product IDs from 1
            product_id = 1
            # Process each line in the file
            for line in file:
                parts = []
                current_part = ""
                # Process each character in the line
                for char in line:
                    if char == ",":
                        # Found comma separator, add current part to list
                        parts.append(current_part)
                        current_part = ""
                    elif char == "\n":
                        # Skip newline characters
                        continue
                    else:
                        # Build current field character by character
                        current_part += char
                # Add the last field after last comma
                parts.append(current_part)
                # Validate we have all 5 required fields
                if len(parts) < 5:
                    print("Invalid product entry: " + line)
                    continue
                # Add product to dictionary with auto-incremented ID
                products[product_id] = {
                    "name": parts[0],        # Product name (first field)
                    "brand": parts[1],       # Brand name (second field)
                    "quantity": int(parts[2]), # Convert quantity to integer
                    "cost_price": float(parts[3]), # Convert price to float
                    "origin": parts[4],      # Country of origin
                }
                # Increment ID for next product
                product_id += 1
    except FileNotFoundError:
        # Handle missing file error
        print("Error: Products file not found. Please ensure 'Product.txt' exists.")
    except Exception as e:
        # Handle all other errors
        print("An error occurred while loading products: " + str(e))
    # Return the populated products dictionary
    return products
