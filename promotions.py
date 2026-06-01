from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        if not name:
            raise ValueError("Promotion name cannot be empty")

        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)

        if percent < 0 or percent > 100:
            raise ValueError("Percent must be between 0 and 100")

        self.percent = percent

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2

        return (
            full_price_items * product.price +
            half_price_items * product.price * 0.5
        )


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        paid_items = quantity - free_items

        return paid_items * product.price