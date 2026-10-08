from decimal import Decimal, InvalidOperation
from products import products


def calculate_discount(subtotal):
    # Every complete KSh 1,000 earns another 5 percentage points off.
    rate = min(int(subtotal // Decimal("1000")) * 5, 100)
    return (subtotal * Decimal(rate) / Decimal("100")).quantize(Decimal("0.01"))


def get_payment(amount_due):
    while True:
        try:
            payment = Decimal(input(f"Amount due is KSh {amount_due:.2f}. Enter payment: KSh "))
            if not payment.is_finite() or payment < 0:
                print("Enter a valid non-negative amount.")
            elif payment < amount_due:
                print("Insufficient payment. Please enter the full amount due or more.")
            else:
                return payment.quantize(Decimal("0.01"))
        except InvalidOperation:
            print("Please enter a valid amount, such as 1500 or 1500.50.")


def print_receipt(basket, subtotal, discount, total, payment):
    print("\n" + "=" * 38)
    print("             SMART SHOP RECEIPT")
    print("=" * 38)
    for code, quantity in basket.items():
        product = products[code]
        line_total = product["price"] * quantity
        print(f"{product['name']} ({code}) x {quantity}: KSh {line_total:.2f}")
    print("-" * 38)
    print(f"Subtotal: KSh {subtotal:.2f}")
    print(f"Discount: -KSh {discount:.2f}")
    print(f"Total:    KSh {total:.2f}")
    print(f"Paid:     KSh {payment:.2f}")
    print(f"Change:   KSh {payment - total:.2f}")
    print("Thank you for shopping!")
    print("=" * 38)
