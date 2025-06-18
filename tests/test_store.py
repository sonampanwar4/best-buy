import pytest
from store import Store
from products import Product

# --- Fixtures ---

@pytest.fixture
def product_apple():
    return Product("Apple", 1.0, 10)

@pytest.fixture
def product_banana():
    return Product("Banana", 0.5, 20)

@pytest.fixture
def inactive_product():
    p = Product("Orange", 0.8, 0)
    p.deactivate()
    return p

@pytest.fixture
def store(product_apple, product_banana, inactive_product):
    return Store([product_apple, product_banana, inactive_product])

# --- Store Tests ---

def test_add_product(store):
    new_product = Product("Kiwi", 2.0, 5)
    store.add_product(new_product)
    assert new_product in store.product_list

def test_remove_product(store, product_apple):
    store.remove_product(product_apple)
    assert product_apple not in store.product_list

def test_remove_product_not_found_raises(store):
    p = Product("NotExist", 1.0, 1)
    with pytest.raises(ValueError):
        store.remove_product(p)

def test_get_total_quantity(store):
    assert store.get_total_quantity() == 30  # 10 + 20

def test_get_all_products(store):
    active = store.get_all_products()
    assert all(p.is_active() for p in active)
    assert len(active) == 2  # Apple and Banana only

def test_order_success(store, product_apple, product_banana):
    total = store.order([
        (product_apple, 2),  # 2 x 1.0
        (product_banana, 4)  # 4 x 0.5
    ])
    assert total == 2 + 2
    assert product_apple.get_quantity() == 8
    assert product_banana.get_quantity() == 16

def test_order_with_error(store, product_apple, product_banana):
    product_banana._quantity = 1  # Force error
    total = store.order([
        (product_apple, 2),
        (product_banana, 10)  # Too many
    ])
    assert total == 2.0
    assert product_banana.get_quantity() == 1
