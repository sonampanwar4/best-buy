import pytest
from products import Product

@pytest.fixture
def product_apple():
    return Product("Apple", 1.0, 10)

@pytest.fixture
def product_banana():
    return Product("Banana", 0.5, 20)

# --- Product Tests ---

def test_product_initialization(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.price == 1.0
    assert product_apple.get_quantity() == 10

def test_invalid_product_name():
    with pytest.raises(ValueError):
        Product("", 1.0, 5)

def test_invalid_product_price():
    with pytest.raises(ValueError):
        Product("Test", -1.0, 5)

def test_invalid_product_quantity():
    with pytest.raises(ValueError):
        Product("Test", 1.0, -5)

def test_get_quantity_type_error(product_apple):
    product_apple._quantity = "ten"
    with pytest.raises(TypeError):
        product_apple.get_quantity()

def test_product_activate_deactivate(product_apple):
    product_apple.deactivate()
    assert not product_apple.is_active()
    product_apple.activate()
    assert product_apple.is_active()

def test_product_show(product_banana):
    output = product_banana.show()
    assert "Banana" in output
    assert "Price" in output
    assert "Quantity" in output

def test_product_buy_reduces_quantity(product_apple):
    price = product_apple.buy(3)
    assert price == 3.0
    assert product_apple.get_quantity() == 7

def test_product_buy_deactivates_when_zero():
    p = Product("Single", 10, 1)
    p.buy(1)
    assert p.get_quantity() == 0
    assert not p.is_active()

def test_product_buy_too_much_raises(product_apple):
    with pytest.raises(ValueError):
        product_apple.buy(100)

def test_product_buy_negative_quantity(product_apple):
    with pytest.raises(ValueError):
        product_apple.buy(-2)
