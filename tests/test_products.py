import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


# --- Product Fixtures ---

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


# --- Product Tests ---

def test_product_initialization(product_apple):
    assert product_apple.name == "Apple"
    assert product_apple.price == 1.0
    assert product_apple.get_quantity() == 10
    assert product_apple.is_active() is True
    assert product_apple.get_promotion() is None


def test_invalid_product_name():
    with pytest.raises(ValueError, match="Name must be a string type and not be empty."):
        Product("", 1.0, 5)


def test_invalid_product_price():
    with pytest.raises(ValueError, match="Price must be a positive number."):
        Product("Test", -1.0, 5)


def test_invalid_product_quantity():
    with pytest.raises(ValueError, match="Quantity must be a positive integer number."):
        Product("Test", 1.0, -5)


def test_get_quantity_type_error(product_apple):
    product_apple._quantity = "ten"
    with pytest.raises(TypeError, match="Value should be integer type."):
        product_apple.get_quantity()


def test_product_activate_deactivate(product_apple):
    product_apple.deactivate()
    assert not product_apple.is_active()
    product_apple.activate()
    assert product_apple.is_active()


def test_product_set_quantity_deactivates_when_zero(product_apple):
    product_apple.set_quantity(0)
    assert product_apple.get_quantity() == 0
    assert not product_apple.is_active()


def test_product_set_quantity_reactivates(product_apple):
    product_apple.deactivate()
    product_apple.set_quantity(5)
    assert product_apple.get_quantity() == 5
    assert product_apple.is_active()


def test_product_str(product_banana):
    output = str(product_banana)
    assert "Banana" in output
    assert "Price: $0.50" in output
    assert "Quantity: 20" in output
    assert "Active: True" in output
    assert "Promotion" not in output


def test_product_buy_reduces_quantity(product_apple):
    price = product_apple.buy(3)
    assert price == pytest.approx(3.0)
    assert product_apple.get_quantity() == 7
    assert product_apple.is_active()


def test_product_buy_deactivates_when_zero():
    p = Product("Single", 10, 1)
    price = p.buy(1)
    assert price == pytest.approx(10.0)
    assert p.get_quantity() == 0
    assert not p.is_active()


def test_product_buy_too_much_raises(product_apple):
    with pytest.raises(ValueError, match="Sorry! We have 10 products in stock."):
        product_apple.buy(100)


def test_product_buy_negative_quantity(product_apple):
    with pytest.raises(ValueError, match="Quantity must be a positive integer number."):
        product_apple.buy(-2)


def test_product_buy_inactive_raises(product_apple):
    product_apple.deactivate()
    with pytest.raises(ValueError, match="Product Apple is not active."):
        product_apple.buy(1)


def test_product_set_promotion(product_apple):
    promotion = PercentDiscount("20% Off", 20)
    product_apple.set_promotion(promotion)
    assert product_apple.get_promotion() == promotion
    assert str(product_apple) == "Apple, Price: $1.00, Quantity: 10, Active: True, Promotion: 20% Off"


def test_product_set_invalid_promotion(product_apple):
    with pytest.raises(ValueError, match="Promotion must be a Promotion object or None."):
        product_apple.set_promotion("Invalid")


def test_product_buy_with_promotion(product_apple):
    promotion = PercentDiscount("20% Off", 20)
    product_apple.set_promotion(promotion)
    price = product_apple.buy(2)
    assert price == pytest.approx(1.6)  # 2 * 1.0 * (1 - 0.2)
    assert product_apple.get_quantity() == 8


def test_product_comparison(product_apple, product_banana):
    assert product_apple > product_banana  # 1.0 > 0.5
    assert product_banana < product_apple  # 0.5 < 1.0
    assert not (product_apple < product_banana)
    assert not (product_banana > product_apple)


def test_product_comparison_invalid_type(product_apple):
    with pytest.raises(TypeError, match="Can only compare with another Product."):
        product_apple > 1.0
    with pytest.raises(TypeError, match="Can only compare with another Product."):
        product_apple < "invalid"


# --- NonStockedProduct Tests ---

def test_non_stocked_product_initialization(non_stocked_product):
    assert non_stocked_product.name == "Software License"
    assert non_stocked_product.price == 99.99
    assert non_stocked_product.get_quantity() == 0
    assert non_stocked_product.is_active()


def test_non_stocked_set_quantity_raises(non_stocked_product):
    with pytest.raises(ValueError, match="Non-stocked products must have quantity 0."):
        non_stocked_product.set_quantity(1)


def test_non_stocked_buy_with_promotion(non_stocked_product):
    promotion = SecondHalfPrice("Second Half Price")
    non_stocked_product.set_promotion(promotion)
    price = non_stocked_product.buy(2)
    assert price == pytest.approx(149.985)  # 99.99 + (99.99 * 0.5)
    assert non_stocked_product.get_quantity() == 0
    assert non_stocked_product.is_active()


def test_non_stocked_str(non_stocked_product):
    output = str(non_stocked_product)
    assert "Software License (Non-Stocked)" in output
    assert "Price: $99.99" in output
    assert "Active: True" in output
    assert "Promotion" not in output


def test_non_stocked_comparison(non_stocked_product, product_apple):
    assert non_stocked_product > product_apple  # 99.99 > 1.0
    assert product_apple < non_stocked_product  # 1.0 < 99.99


# --- LimitedProduct Tests ---

def test_limited_product_initialization(limited_product):
    assert limited_product.name == "Shipping Fee"
    assert limited_product.price == 5.99
    assert limited_product.get_quantity() == 100
    assert limited_product.max_quantity == 1
    assert limited_product.is_active()


def test_limited_product_buy_too_much_raises(limited_product):
    with pytest.raises(ValueError, match="Cannot purchase more than 1 of Shipping Fee in a single order."):
        limited_product.buy(2)


def test_limited_product_buy_with_promotion(limited_product):
    promotion = ThirdOneFree("Buy 2 Get 1 Free")
    limited_product.set_promotion(promotion)
    price = limited_product.buy(1)
    assert price == pytest.approx(5.99)  # No discount for 1 item
    assert limited_product.get_quantity() == 99


def test_limited_product_str(limited_product):
    output = str(limited_product)
    assert "Shipping Fee (Limited)" in output
    assert "Price: $5.99" in output
    assert "Quantity: 100" in output
    assert "Max per order: 1" in output
    assert "Active: True" in output


def test_limited_product_comparison(limited_product, product_apple):
    assert limited_product > product_apple  # 5.99 > 1.0
    assert product_apple < limited_product  # 1.0 < 5.99