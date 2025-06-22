class Product:
    def __init__(self, name, price, quantity):
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

    def get_quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (int)."""
        if isinstance(self._quantity, int):
            return self._quantity
        else:
            raise TypeError("Value should be integer type.")

    def set_quantity(self, quantity):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        self._quantity = quantity
        if self._quantity == 0:
            self.deactivate()
        elif self._quantity > 0 and not self.is_active():
            self.activate()

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
        return f"{self.name}, Price: ${self.price:.2f}, Quantity: {self._quantity}, Active: {self.active}"

    def buy(self, quantity) -> float:
        """
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem, raises an Exception.
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
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, 0)

    def set_quantity(self, quantity):
        """Override to prevent changing quantity from 0"""
        if quantity != 0:
            raise ValueError("Non-stocked products must have quantity 0.")
        self._quantity = 0

    def buy(self, quantity) -> float:
        """Override to allow purchase without quantity tracking"""
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer number.")
        return quantity * self.price

    def show(self) -> str:
        """Returns a string that represents the non-stocked product"""
        return f"{self.name} (Non-Stocked), Price: ${self.price:.2f}, Active: {self.active}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_quantity):
        super().__init__(name, price, quantity)
        if not isinstance(max_quantity, int) or max_quantity <= 0:
            raise ValueError("Max quantity must be a positive integer.")
        self.max_quantity = max_quantity

    def buy(self, quantity) -> float:
        """Override to enforce maximum purchase quantity per order"""
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
        return quantity * self.price

    def show(self) -> str:
        """Returns a string that represents the limited product"""
        return f"{self.name} (Limited), Price: ${self.price:.2f}, Quantity: {self._quantity}, Max per order: {self.max_quantity}, Active: {self.active}"