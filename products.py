class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        if not isinstance(name, str) or name == "":
            raise ValueError("Name must be as string type and not be empty.")
        self.name = name
        self.price = price
        self._quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (int)."""
        if isinstance(self._quantity, int):
            return self._quantity
        else:
            raise TypeError("Value should be integer type.")

    def set_quantity(self, value):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if value > 0:
            self._quantity += value
            self.activate()
        else:
            self._quantity = 0
            self.deactivate()

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def is_active(self) -> bool:
        """Returns True if the product is active, otherwise False."""
        return self.active

    def show(self) -> str:
        """Returns a string that represents the product"""
        return f"{self.name}, Price: {self.price}, Quantity: {self._quantity}"

    def buy(self, quantity) -> float:
        """
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        """
        if quantity > self._quantity:
            quantity = quantity - self._quantity
            raise ValueError(f"Sorry! we have {quantity} products in stock.")

        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()
        total_price = quantity * self._price
        return total_price
