import products
import store

# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


if __name__ == "__main__":
    while True:
        print("\nWelcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = input("Please enter your choice (1-4): ")

            if choice == '1':
                for prod in best_buy.get_all_products():
                    prod.show()

            elif choice == '2':
                total_quantity = best_buy.get_total_quantity()
                print(f"Total quantity of all products in store: {total_quantity}")

            elif choice == '3':
                shopping_list = []
                while True:
                    prod_name = input("Enter product name to add to your order (or 'done' to finish): ")
                    if prod_name.lower() == 'done':
                        break
                    amount = int(input(f"Enter amount of {prod_name} to order: "))
                    # find product by name
                    product = next((p for p in best_buy.get_all_products() if p.name == prod_name), None)
                    if product:
                        shopping_list.append((product, amount))
                    else:
                        print(f"Product {prod_name} not found or inactive.")

                try:
                    total_cost = best_buy.order(shopping_list)
                    print(f"Your order has been processed. Total cost: {total_cost} €")
                except ValueError as e:
                    print(f"Error processing order: {e}")

            elif choice == '4':
                print("Thank you for visiting Best Buy!")
                break

        except Exception as e:
            print(f"An error occurred: {e}")
