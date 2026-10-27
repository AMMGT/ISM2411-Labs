"""Reusable pricing functions; rates are decimals (for example, 0.07 for 7%)."""


def calculate_tax(amount, tax_rate):
    """Return the tax for an amount at the given decimal tax rate."""
    return amount * tax_rate


def apply_discount(amount, discount_rate):
    """Return the amount after applying the given decimal discount rate."""
    return amount * (1 - discount_rate)


def final_price(amount, tax_rate, discount_rate):
    """Apply a discount, then calculate tax on the discounted amount."""
    discounted_amount = apply_discount(amount, discount_rate)
    return discounted_amount + calculate_tax(discounted_amount, tax_rate)


if __name__ == "__main__":
    price = 100
    tax_rate = 0.07
    discount_rate = 0.10
    print(f"Original price: ${price:.2f}")
    print(f"Tax: ${calculate_tax(apply_discount(price, discount_rate), tax_rate):.2f}")
    print(f"Discounted price: ${apply_discount(price, discount_rate):.2f}")
    print(f"Final price: ${final_price(price, tax_rate, discount_rate):.2f}")
