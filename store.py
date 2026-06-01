import products


class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0

        for product in self.products:
            total_quantity += product.get_quantity()

        return total_quantity

    def get_all_products(self):
        active_products = []

        for product in self.products:
            if product.is_active():
                active_products.append(product)

        return active_products

    def order(self, shopping_list):
        total_price = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_list = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(products_list[0], 1), (products_list[1], 2)]))


if __name__ == "__main__":
    main()