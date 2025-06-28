from read import load_products
from operations import sell_products, restock_products

# Load products from the file
products = load_products()

if len(products) > 0:
    print("")
    print("WeCare Wholesale System")
    print("Welcome, Admin!")

    # Main menu loop
    while True:
        print("")
        print("Choose an option:")
        print("1: Sell products to a customer")
        print("2: Restock products from the manufacturer")
        print("3: Exit")
        try:
            # Get user choice
            choice = int(input("Enter your choice: "))
            if choice == 1:
                # Call the sell_products function
                sell_products(products)
            elif choice == 2:
                # Call the restock_products function
                restock_products(products)
            elif choice == 3:
                # Exit the program
                print("Thank you! Have a great day!")
                break
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print("An error occurred: " + str(e))
