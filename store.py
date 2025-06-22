from typing import List
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.product_list = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of items in the store."""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> List[Product]:
        """Return all active products in the store."""
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list: List[tuple[Product, int]]) -> float:
        """
        Process an order from a list of (Product, quantity) tuples.
        Return the total price of the order.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(f"Error purchasing {product.name}: {e}")
        return total_price

    def __contains__(self, product: Product) -> bool:
        """Check if a product exists in the store."""
        return product in self.product_list

    def __add__(self, other: 'Store') -> 'Store':
        """Combine two stores into a new store with all products."""
        if not isinstance(other, Store):
            raise TypeError("Can only combine with another Store.")
        combined_products = self.product_list + other.product_list
        return Store(combined_products)