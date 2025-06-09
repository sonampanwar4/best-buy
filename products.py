class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self.active = True

    @property
    def price(self):
        """Getter function for quantity. Returns the price (int or float)."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter function for price. If price is 0, raise error."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value

    @property
    def name(self):
        """Getter function for name. Returns the name (str)."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter function for name. If name is empty, raise error."""
        if not isinstance(value, str) or value == "":
            raise ValueError("Name must be as string type and not be empty.")
        self._name = value

    @property
    def quantity(self) -> int:
        """Getter function for quantity. Returns the quantity (int)."""
        if isinstance(self._quantity, int):
            return self._quantity
        else:
            raise TypeError("Value should be integer type.")

    @quantity.setter
    def quantity(self, value):
        """Setter function for quantity. If quantity reaches 0, deactivates the product."""
        if value > 0:
            self._quantity = value
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
            raise ValueError(f"Sorry! No {self._name} remains.")

        self._quantity -= quantity
        if self._quantity <= 0:
            self.deactivate()
        total_price = quantity * self._price
        return total_price

