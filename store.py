from products import Product
from typing import List


RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'

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

    def order(self, shopping_list: list) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total_price = 0.0
        for product_index, quantity in shopping_list:
            try:
                product = self.product_list[product_index]
                prod_quantity = product.get_quantity()
                # verify the product's quantity in store more than the ordered quantity
                if quantity < 0:
                    print(f"❌ Quantity {RED}({quantity}){RESET} for {product.name}: Quantity must be a positive integer number.")
                elif prod_quantity < quantity:
                    print(f"❌ Insufficient quantity for {product.name}. {GREEN}Available: {prod_quantity}{RESET}, {RED}Requested: {quantity}{RESET}")
                else:
                    prod_quantity -= quantity
                    # deactivate product if number of quantity is 0
                    if prod_quantity == 0:
                        product.deactivate()
                    product.set_quantity(prod_quantity)
                    total_price += product.price * quantity
            except Exception:
                print(f"❌ Product {RED}Option {product_index}, Quality: {quantity}{RESET} does not exist.")

        return total_price
