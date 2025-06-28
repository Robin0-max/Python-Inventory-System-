from datetime import datetime
from write import save_products

def display_products(products):
    """
    Displays the list of products in a tabular format.
    """
    # Print product table header
    print("")
    print("ID   Name                 Brand           Qty   Price       Origin")
    print("----------------------------------------------------------------------")
    # Display each product in formatted row
    for product_id, product in products.items():
        # Calculate selling price (2x cost price)
        selling_price = product["cost_price"] * 2
        # pid = product ID converted to string
        pid = str(product_id)
        name = product["name"]
        brand = product["brand"]
        qty = str(product["quantity"])
        price = "Rs." + str(selling_price)
        origin = product["origin"]
        # Build formatted row
        row = (
            pid.ljust(5)
            + name.ljust(20)
            + brand.ljust(15)
            + qty.ljust(6)
            + price.ljust(10)
            + origin.ljust(15)
        )
        # Print completed row
        print(row)
    print("")


def sell_products(products):
    """
    Handles the selling operation and generates an invoice.
    """
    # Get customer information first
    print("Please enter your details first.")
    
    # Validate customer name
    while True:
        customer_name = input("Enter customer name: ")
        if customer_name.replace(" ", "").isalpha():  # Allows spaces in the name
            break
        else:
            print("Invalid name! Please enter a valid name (letters and spaces only).")
    
    # Validate customer phone number (must be an integer)
    while True:
        try:
            customer_phone = int(input("Enter customer phone number: "))  # Ensures input is numeric
            break
        except ValueError:
            print("Invalid phone number! Please enter numbers only.")
    
    print("")
    
    # Initialize invoice variables
    total_amount = 0
    now = datetime.now()
    # Format date and time strings
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

    # Create invoice header
    invoice_content = (
        "--- Invoice ---\n"
        "Customer Name: " + customer_name + "\n" +
        "Customer Phone: " + str(customer_phone) + "\n" +
        "Date: " + date + " " + time + "\n" +
        "--------------------------------------------------------------\n" +
        "ID   Name             Qty   Free   Price       Subtotal\n" +
        "--------------------------------------------------------------\n"
    )

    # Sales transaction loop
    while True:
        # Show available products
        display_products(products)
        try:
            # Get product selection
            product_id = int(input("Enter the product ID to sell: "))
            # Validate product ID exists
            if product_id not in products:
                print("Invalid Product ID! Please try again.")
                continue
            # Get quantity to sell
            product_quantity = int(input("Enter the quantity to sell: "))
            product = products[product_id]
            # Check stock availability
            if product_quantity > product["quantity"]:
                print("Insufficient stock! Please try again.")
                continue

            # Calculate free items (Buy 2 Get 1 Free promotion)
            free_items = product_quantity // 3
            total_deduct = product_quantity + free_items
            # Update inventory
            product["quantity"] -= total_deduct
            # Calculate pricing
            selling_price = product["cost_price"] * 2
            subtotal = product_quantity * selling_price
            total_amount += subtotal

            # Format invoice line (pid = product ID string for display)
            pid = str(product_id)
            name = product["name"]
            qty = str(product_quantity)
            freeq = str(free_items)
            price = "Rs." + str(selling_price)
            sub = "Rs." + str(subtotal)

            # Build formatted invoice row
            row = (
                pid.ljust(4)
                + name.ljust(15)
                + qty.ljust(6)
                + freeq.ljust(6)
                + price.ljust(12)
                + sub.ljust(10)
            )

            # Add row to invoice content
            invoice_content += row + "\n"
            print("")
            print("Transaction recorded successfully.")
            print("")
            # Check if customer wants to buy more
            more_items = input("Do you want to buy another product? (yes/no): ")
            if more_items.lower() != "yes":
                break
        except ValueError:
            print("Invalid input! Please enter numeric values where required.")
        except Exception as e:
            print("An error occurred: " + str(e))

    # Add footer to invoice
    invoice_content += (
        "--------------------------------------------------------------\n" +
        "Total Amount: Rs." + str(total_amount) + "\n"
    )
    # Display invoice in the terminal
    print("\n" + invoice_content)

    # Save invoice to file
    invoice_filename = "sales_invoice.txt"
    try:
        with open(invoice_filename, "w") as invoice_file:
            invoice_file.write(invoice_content)
        print("Invoice generated and saved as " + invoice_filename)
    except Exception as e:
        print("An error occurred while saving the invoice: " + str(e))

    # Save updated products to file
    save_products(products)


def restock_products(products):
    """
    Handles the restocking operation and generates an invoice.
    """
    print("")
    print("Restocking products...")
    
    # Validate supplier/vendor name (must be a string without numbers)
    while True:
        supplier_name = input("Enter supplier/vendor name: ")
        if supplier_name.replace(" ", "").isalpha():  # Allows spaces in the name
            break
        else:
            print("Invalid name! Please enter a valid name (letters and spaces only).")
    
    
    # Get current timestamp
    now = datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

    # Create restock invoice header
    invoice_content = (
        "Supplier Name: " + supplier_name + "\n" +
        "Date: " + date + " " + time + "\n" +
        "--------------------------------------------------\n" +
        "ID   Name             Qty   Cost Price   Total Cost\n" +
        "--------------------------------------------------\n"
    )
    total_amount = 0

    try:
        # Restocking loop
        while True:
            display_products(products)
            # Get product to restock (0 = new product)
            product_id = int(input("Enter the product ID to restock (or 0 to add a new product): "))
            if product_id == 0:
                # Add new product flow
                name = input("Enter Product Name: ")
                brand = input("Enter Brand: ")
                quantity = int(input("Enter Quantity: "))
                cost_price = float(input("Enter Cost Price: "))
                origin = input("Enter Origin: ")
                # Create new product ID
                new_id = max(products.keys(), default=0) + 1
                # Add new product to dictionary
                products[new_id] = {
                    "name": name,
                    "brand": brand,
                    "quantity": quantity,
                    "cost_price": cost_price,
                    "origin": origin,
                }
                save_products(products)
                print("New product ID " + str(new_id) + " added successfully!")
                continue
            # Validate existing product ID
            if product_id not in products:
                print("Invalid Product ID! Please try again.")
                continue
            # Get restock details
            restock_quantity = int(input("Enter the quantity to restock: "))
            cost_price = float(input("Enter the cost price (if changed): "))
            # Update inventory
            products[product_id]["quantity"] += restock_quantity
            products[product_id]["cost_price"] = cost_price
            total_cost = restock_quantity * cost_price
            total_amount += total_cost

            # Format invoice line (pid = product ID string for display)
            pid = str(product_id)
            name = products[product_id]["name"]
            qty = str(restock_quantity)
            price = "Rs." + str(cost_price)
            totalcost = "Rs." + str(total_cost)

            # Build formatted row
            row = (
                pid.ljust(4)
                + name.ljust(15)
                + qty.ljust(5)
                + price.ljust(10)
                + totalcost.ljust(10)
            )
            # Add row to invoice
            invoice_content += row + "\n"
            # Check if more items to restock
            more_restock = input("Do you want to restock another product? (yes/no): ")
            if more_restock.lower() != "yes":
                break
    except Exception as e:
        print("An error occurred: " + str(e))

    # Add footer to restock invoice
    invoice_content += (
        "--------------------------------------------------\n" +
        "Total Restock Cost: Rs." + str(total_amount) + "\n"
    )
    # Save restock invoice
    invoice_filename = "restock_invoice.txt"
    try:
        with open(invoice_filename, "w") as invoice_file:
            invoice_file.write(invoice_content)
        print("Invoice generated and saved as " + invoice_filename)
    except Exception as e:
        print("An error occurred while saving the invoice: " + str(e))

    # Save updated product data
    save_products(products)
