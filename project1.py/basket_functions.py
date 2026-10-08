from products import products
from shop_functions import basket_subtotal


def add_item(basket, code, quantity):
    basket[code] = basket.get(code, 0) + quantity


def display_basket(basket):
    print("\nCURRENT BASKET")
    if not basket:
        print("Basket is empty.")
        return
    for code, quantity in basket.items():
        product = products[code]
        line_total = product["price"] * quantity
        print(f"{code} {product['name']} x {quantity} = KSh {line_total:.2f}")
    print(f"Basket subtotal: KSh {basket_subtotal(basket):.2f}")


def remove_item(basket):
    if not basket:
        print("Basket is empty; there is nothing to remove.")
        return
    display_basket(basket)
    code = input("Enter product code to remove (or Enter to cancel): ").strip().upper()
    if not code:
        return
    if code in basket:
        del basket[code]
        print("Item removed from basket.")
    else:
        print("That product is not in your basket.")
