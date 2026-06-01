import products
import store


def list_products(best_buy):
    all_products = best_buy.get_all_products()

    print("------")
    for index, product in enumerate(all_products, start=1):
        print(f"{index}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
    print("------")


def make_order(best_buy):
    shopping_list = []
    all_products = best_buy.get_all_products()

    while True:
        list_products(best_buy)

        product_choice = input("Which product # do you want? ")
        if product_choice == "":
            break

        quantity_choice = input("What amount do you want? ")
        if quantity_choice == "":
            break

        try:
            product_index = int(product_choice) - 1
            quantity = int(quantity_choice)

            if product_index < 0 or product_index >= len(all_products):
                print("Invalid product number.")
                continue

            product = all_products[product_index]
            shopping_list.append((product, quantity))
            print("Product added to list!")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"Order made! Total payment: {total_price}")
        except ValueError as error:
            print(f"Error while making order: {error}")


def start(best_buy):
    while True:
        print()
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        print()

        choice = input("Please choose a number: ")

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            print(f"Total of {best_buy.get_total_quantity()} items in store")
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()