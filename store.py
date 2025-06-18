from products import Product
from typing import List


class Store:
    def __init__(self, products: list):
        self.product_list = products

    def remove_product(self, product):
        """Removes a product from store."""
        self.product_list.remove(product)

    def add_product(self, product):
        """Add a product in the store."""
        self.product_list.append(product)

    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total."""
        return sum(product.get_quantity() for product in self.product_list)

    def get_all_products(self) -> List[Product]:
        """Returns all products in the store that are active."""
        all_products = []
        if self.product_list:
            for product in self.product_list:
                if product.is_active():
                    all_products.append(product)

        return all_products

    def order(self, shopping_list: list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0
        for shop in shopping_list:
            product, quantity = shop[0], shop[1]
            try:
                total_price += product.buy(quantity)
            except Exception as e:
                print(e)

        return total_price
