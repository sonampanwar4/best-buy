import pytest
from store import Store
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount


# --- Store Fixtures ---

@pytest.fixture
def product_apple():
    return Product("Apple", 1.0, 10)


@pytest.fixture
def product_banana():
    return Product("Banana", 0.5, 20)


@pytest.fixture
def non_stocked_product():
    return NonStockedProduct("Software License", 99.99)


@pytest.fixture
def limited_product():
    return LimitedProduct("Shipping Fee", 5.99, 100, 1)


@pytest.fixture
def store_with_products(product_apple, product_banana):
    return Store([product_apple, product_banana])


@pytest.fixture
def empty_store():
    return Store([])


# --- Store Tests ---

def test_store_initialization(store_with_products, product_apple, product_banana):
    assert store_with_products.product_list == [product_apple, product_banana]
    assert len(store_with_products.get_all_products()) == 2


def test_store_add_product(empty_store, product_apple):
    empty_store.add_product(product_apple)
    assert product_apple in empty_store
    assert len(empty_store.get_all_products()) == 1


def test_store_remove_product(store_with_products, product_apple):
    store_with_products.remove_product(product_apple)
    assert product_apple not in store_with_products
    assert len(store_with_products.get_all_products()) == 1


def test_store_remove_nonexistent_product(store_with_products):
    non_existent_product = Product("Orange", 0.75, 5)
    with pytest.raises(ValueError, match="list.remove.*: x not in list"):
        store_with_products.remove_product(non_existent_product)


def test_store_get_total_quantity(store_with_products):
    assert store_with_products.get_total_quantity() == 30  # 10 (apple) + 20 (banana)


def test_store_get_total_quantity_empty(empty_store):
    assert empty_store.get_total_quantity() == 0


def test_store_get_all_products(store_with_products, product_apple):
    product_apple.deactivate()
    active_products = store_with_products.get_all_products()
    assert product_apple not in active_products
    assert len(active_products) == 1


def test_store_get_all_products_empty(empty_store):
    assert empty_store.get_all_products() == []


def test_store_order(store_with_products, product_apple, product_banana):
    shopping_list = [(product_apple, 2), (product_banana, 3)]
    total_price = store_with_products.order(shopping_list)
    assert total_price == pytest.approx(3.5)  # 2 * 1.0 + 3 * 0.5
    assert product_apple.get_quantity() == 8
    assert product_banana.get_quantity() == 17


def test_store_order_with_promotion(product_apple, empty_store):
    product_apple.set_promotion(PercentDiscount("20% Off", 20))
    empty_store.add_product(product_apple)
    shopping_list = [(product_apple, 2)]
    total_price = empty_store.order(shopping_list)
    assert total_price == pytest.approx(1.6)  # 2 * 1.0 * (1 - 0.2)
    assert product_apple.get_quantity() == 8


def test_store_order_invalid_quantity(store_with_products, product_apple, capsys):
    shopping_list = [(product_apple, 100)]
    total_price = store_with_products.order(shopping_list)
    assert total_price == 0.0  # No purchase due to error
    captured = capsys.readouterr()
    assert "Error purchasing Apple: Sorry! We have 10 products in stock." in captured.out


def test_store_contains_product(store_with_products, product_apple, product_banana, non_stocked_product):
    assert product_apple in store_with_products
    assert product_banana in store_with_products
    assert non_stocked_product not in store_with_products


def test_store_add_operator(store_with_products, empty_store, non_stocked_product, limited_product):
    store2 = Store([non_stocked_product, limited_product])
    combined_store = store_with_products + store2
    assert len(combined_store.get_all_products()) == 4
    assert non_stocked_product in combined_store
    assert limited_product in combined_store
    assert store_with_products.get_all_products() == [product for product in store_with_products.product_list]
    assert store2.get_all_products() == [product for product in store2.product_list]


def test_store_add_invalid_type(store_with_products):
    with pytest.raises(TypeError, match="Can only combine with another Store."):
        store_with_products + [1, 2, 3]


def test_empty_store_contains(empty_store, product_apple):
    assert product_apple not in empty_store