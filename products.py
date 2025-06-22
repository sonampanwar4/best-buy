from promotions import Promotion


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be a string type and not be empty.")
        self.name = name
        self.price = price
        self._quantity = quantity
        self.active = True
        self._promotion = None

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (int)."""
        if isinstance(self._quantity, int):
            return self._quantity
        raise TypeError("Value should be integer type.")

    def set_quantity(self, quantity: int):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()
        elif self._quantity > 0 and not self.is_active():
            self.activate()

    def get_promotion(self) -> Promotion:
        """Getter function for promotion."""
        return self._promotion

    def set_promotion(self, promotion: Promotion):
        """Setter function for promotion."""
        if not isinstance(promotion, (Promotion, type(None))):
            raise ValueError("Promotion must be a Promotion object or None.")
        self._promotion = promotion

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def __str__(self) -> str:
        """Returns a string representation of the product."""
        promotion_info = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self._quantity}, Active: {self.active}{promotion_info}"

    def __gt__(self, other) -> bool:
        """Compare products by price using > operator."""
        if not isinstance(other, Product):
            raise TypeError("Can only compare with another Product.")
        return self.price > other.price

    def __lt__(self, other) -> bool:
        """Compare products by price using < operator."""
        if not isinstance(other, Product):
            raise TypeError("Can only compare with another Product.")
        return self.price < other.price

    def buy(self, quantity: int) -> float:
        """
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Applies promotion if available.
        """
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        if quantity > self._quantity:
            raise ValueError(f"Sorry! We have {self._quantity} products in stock.")

        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        """Override to prevent changing quantity from 0."""
        if quantity != 0:
            raise ValueError("Non-stocked products must have quantity 0.")
        self._quantity = 0

    def buy(self, quantity: int) -> float:
        """Override to allow purchase without quantity tracking."""
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return quantity * self.price

    def __str__(self) -> str:
        """Returns a string representation of the non-stocked product."""
        promotion_info = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self.name} (Non-Stocked), Price: ${self.price:.2f}, Active: {self.active}{promotion_info}"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, max_quantity: int):
        super().__init__(name, price, quantity)
        if not isinstance(max_quantity, int) or max_quantity <= 0:
            raise ValueError("Max quantity must be a positive integer.")
        self.max_quantity = max_quantity

    def buy(self, quantity: int) -> float:
        """Override to enforce maximum purchase quantity per order."""
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        if quantity > self.max_quantity:
            raise ValueError(f"Cannot purchase more than {self.max_quantity} of {self.name} in a single order.")
        if quantity > self._quantity:
            raise ValueError(f"Sorry! We have {self._quantity} products in stock.")

        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        if self._promotion:
            return self._promotion.apply_promotion(self, quantity)
        return quantity * self.price

    def __str__(self) -> str:
        """Returns a string representation of the limited product."""
        promotion_info = f", Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self.name} (Limited), Price: ${self.price:.2f}, Quantity: {self._quantity}, Max per order: {self.max_quantity}, Active: {self.active}{promotion_info}"
