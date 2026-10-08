from decimal import Decimal
from products import products


def display_products():
    print("\nPRODUCT MENU")
    for code, product in products.items():
        print(f"{code}: {product['name']} - KSh {product['price']:.2f}")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                return quantity
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a whole number.")


def basket_subtotal(basket):
    return sum(
        (products[code]["price"] * quantity for code, quantity in basket.items()),
        Decimal("0.00"),
    )
