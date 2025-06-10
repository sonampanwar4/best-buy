import products
import store
import sys



def show_list_of_all_products(my_store):
    """Display a numbered list of all active products in the store.
        param my_store: An instance of the Store class containing a list of products.
    """
    products_list = my_store.get_all_products()
    if products_list:
        for index, product in enumerate(products_list, start=1):
            print(f" {index}. {product.name}, Price: {product.price}, Quantity: {product.get_quantity()}")
    else:
        print("❎ No product exist in the store. ❎")


def show_total_amount_in_store(my_store):
    """Displays the total quantity of items in the store.
        :param my_store: A Store object containing a list of products with their quantities.
    """
    total_amount = my_store.get_total_quantity()
    print(f"🟦 Total of {total_amount} items in store. 🟦")


def make_an_order(my_store):
    """Collects user input to create an order from a Store and processes it.
    Notes:
        - Product numbers are 1-based in user input but converted to 0-based indices for processing.
        - Assumes `my_store.order` accepts a list of (product, quantity) tuples and returns a float.
        - Invalid input (e.g., non-numeric or empty input) terminates the input loop.
    :param my_store: An instance of the Store class with a list of products and an `order` method.
    """
    show_list_of_all_products(my_store)
    products = my_store.get_all_products()
    product_list = []
    total_amount = 0.0
    if products:
        print("\n🔶 When you want to finish order, enter empty text.")
        while True:
            try:
                choice = input("(choose) Which product # do you want? ").strip()
                quantity = input("What amount(quantity) do you want? ").strip()
                if not choice and not quantity:
                    break
                choice, quantity = int(choice) - 1, int(quantity)
                product_list.append((products[choice], quantity))
                print("Product added to list! 👍\n")
            except ValueError:
                print("❗Invalid input ❌")
            except IndexError:
                print("❌ Product Option does not exist.")
        print('-' * 20)
        total_amount += my_store.order(product_list)
        if total_amount == 0.0:
            print("❎ No order made! ❎")
        else:
            print(f"✅ Order made! Total payment 💰: ${total_amount} ✅")



MENU_OPTIONS = """
\tStore Menu
\t----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
"""

def start(my_store):
    """Run the main interactive menu loop for the store application.
    This function presents a menu to the user, processes their input, and performs actions based on
    the selected option. It continues running until the user chooses to exit.
        :param my_store: An instance of the Store class containing the product list and methods to manage
        the store's inventory.
    """
    while True:
        print(MENU_OPTIONS)
        try:
            choice = int(input("Please choose a number: "))
            print("🔻" * 20)
            if choice == 1:
                show_list_of_all_products(my_store)
            elif choice == 2:
                show_total_amount_in_store(my_store)
            elif choice == 3:
                make_an_order(my_store)
            elif choice == 4:
                print("Thank you, 👋 bye!")
                sys.exit()
            else:
                print("❗Please choose an option ❌")
            print("🔺" * 20)
        except ValueError:
            print("❗Invalid value ❌")



def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()