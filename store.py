from products import Product
from typing import List


class Store:
    def __init__(self, products: list):
        self.product_list = products

    def remove_product(self, product):
        """Removes a product from store."""
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        total_quantity = 0
        if self.product_list:
            for product in self.product_list:
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        all_products = []
        if self.product_list:
            for product in self.product_list:
                if product.is_active():
                    all_products.append(product)

        return all_products

    def order(self, shopping_list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0.0
        for product, quantity in shopping_list:
            prod_quantity = product.get_quantity()
            if not product.active:
                raise ValueError(f"Product {product.name} is not active")
            if prod_quantity < quantity:
                raise ValueError(
                    f"Insufficient quantity for {product.name}. Available: {prod_quantity}, Requested: {quantity}")

            product.set_quantity(prod_quantity - quantity)
            total_price += product.price * quantity

        return total_price
