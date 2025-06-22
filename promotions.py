from abc import ABC, abstractmethod


class Promotion(ABC):
    """Abstract base class for promotions."""
    def __init__(self, name: str):
        if not isinstance(name, str) or name == "":
            raise ValueError("Promotion name must be a non-empty string.")
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        """Apply the promotion and return the total price."""
        pass


class PercentDiscount(Promotion):
    """Promotion for percentage discount."""
    def __init__(self, name: str, discount_percent: float):
        super().__init__(name)
        if not isinstance(discount_percent, (int, float)) or discount_percent <= 0 or discount_percent >= 100:
            raise ValueError("Discount percent must be between 0 and 100.")
        self.discount_percent = discount_percent

    def apply_promotion(self, product, quantity: int) -> float:
        """Apply percentage discount to total price."""
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        original_price = product.price * quantity
        discount = original_price * (self.discount_percent / 100)
        return original_price - discount


class SecondHalfPrice(Promotion):
    """Promotion for second item at half price."""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """Second item at half price, applied to pairs of items."""
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        full_price_items = (quantity + 1) // 2  # Round up for odd quantities
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    """Promotion for buy 2 get 1 free."""
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """Every third item is free."""
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        free_items = quantity // 3
        paid_items = quantity - free_items
        return paid_items * product.price