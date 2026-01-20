import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)

def start(store_object):
    """Starts the application."""
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = input("Please enter your choice (1-4): ")

            if choice == '1':
                for prod in [product for product in store_object.get_all_products() if product.quantity >= 1]:
                    prod.show()
                print("\n\n")

            elif choice == '2':
                total_quantity = store_object.get_total_quantity()
                print(f"Total quantity of all products in store: {total_quantity}")

            elif choice == '3':
                shopping_list = []
                while True:
                    for prod in [product for product in store_object.get_all_products() if product.quantity >= 1]:
                        prod.show()
                    print("\n\n")

                    prod_name = input("Enter product name to add to your order (or 'done' to finish): ")
                    if prod_name.lower() == 'done':
                        break
                    amount = int(input(f"Enter amount of {prod_name} to order: "))
                    while amount <= 0:
                        print("Invalid amount. Please enter a positive number.")
                        amount = int(input(f"Enter amount of {prod_name} to order: "))

                    # find product by name
                    product = next((p for p in store_object.get_all_products() if p.name == prod_name), None)
                    if product and product.quantity >= amount:
                        shopping_list.append((product, amount))
                    elif product.quantity < amount:
                        print(f"Insufficient quantity of {prod_name} in stock.")
                    else:
                        print(f"Product {prod_name} not found or inactive.")

                try:
                    total_cost = store_object.order(shopping_list)
                    print(f"Your order has been processed. Total cost: {total_cost} €")
                except ValueError as e:
                    print(f"Error processing order: {e}")

            elif choice == '4':
                print("Thank you for visiting Best Buy!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start(best_buy)
