class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > self.quantity:
            raise ValueError("Not enough items in stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        self.quantity = 0

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        return quantity * self.price

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: Unlimited")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        if maximum <= 0:
            raise ValueError("Maximum must be greater than 0")

        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        print(
            f"{self.name}, Price: {self.price}, "
            f"Quantity: {self.quantity}, Maximum per order: {self.maximum}"
        )

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} units of this product"
            )

        return super().buy(quantity)

