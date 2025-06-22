import pytest
from promotions import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree
from products import Product


# --- Promotion Fixtures ---

@pytest.fixture
def product_apple():
    return Product("Apple", 1.0, 10)


@pytest.fixture
def percent_discount():
    return PercentDiscount("20% Off", 20)


@pytest.fixture
def second_half_price():
    return SecondHalfPrice("Second Half Price")


@pytest.fixture
def third_one_free():
    return ThirdOneFree("Buy 2 Get 1 Free")


# --- Promotion Tests ---

def test_promotion_invalid_name():
    with pytest.raises(ValueError, match="Promotion name must be a non-empty string."):
        PercentDiscount("", 20)


def test_percent_discount_initialization(percent_discount):
    assert percent_discount.name == "20% Off"
    assert percent_discount.discount_percent == 20


def test_percent_discount_invalid_percent():
    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100."):
        PercentDiscount("Invalid", 0)
    with pytest.raises(ValueError, match="Discount percent must be between 0 and 100."):
        PercentDiscount("Invalid", 100)


def test_percent_discount_apply(product_apple):
    promotion = PercentDiscount("20% Off", 20)
    price = promotion.apply_promotion(product_apple, 2)
    assert price == pytest.approx(1.6)  # 2 * 1.0 * (1 - 0.2)


def test_percent_discount_negative_quantity(product_apple):
    promotion = PercentDiscount("20% Off", 20)
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        promotion.apply_promotion(product_apple, -1)


def test_second_half_price_apply(product_apple):
    promotion = SecondHalfPrice("Second Half Price")
    price = promotion.apply_promotion(product_apple, 3)
    assert price == pytest.approx(2.5)  # 2 full price + 1 half price = 2 * 1.0 + 0.5


def test_second_half_price_negative_quantity(product_apple):
    promotion = SecondHalfPrice("Second Half Price")
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        promotion.apply_promotion(product_apple, -1)


def test_third_one_free_apply(product_apple):
    promotion = ThirdOneFree("Buy 2 Get 1 Free")
    price = promotion.apply_promotion(product_apple, 3)
    assert price == pytest.approx(2.0)  # 2 paid items, 1 free = 2 * 1.0


def test_third_one_free_negative_quantity(product_apple):
    promotion = ThirdOneFree("Buy 2 Get 1 Free")
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        promotion.apply_promotion(product_apple, -1)