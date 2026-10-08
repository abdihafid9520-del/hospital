from decimal import Decimal
from products import products
from shop_functions import display_products, get_quantity, basket_subtotal
from basket_functions import add_item, display_basket, remove_item
from payment_functions import calculate_discount, get_payment, print_receipt


def main():
    basket = {}
    print("Welcome to the Smart Shop Checkout System")

    while True:
        display_products()
        print("\nEnter a product code to add it, B to view basket, R to remove an item, or Q to pay.")
        choice = input("Your choice: ").strip().upper()

        if choice == "Q":
            break
        if choice == "B":
            display_basket(basket)
            continue
        if choice == "R":
            remove_item(basket)
            continue
        if choice not in products:
            print("Unknown choice. Please enter P01, P02, P03, B, R, or Q.")
            continue

        quantity = get_quantity()
        add_item(basket, choice, quantity)
        print(f"Added {quantity} {products[choice]['name']} to your basket.")

    if not basket:
        print("Basket is empty. No payment is needed.")
        return

    subtotal = basket_subtotal(basket).quantize(Decimal("0.01"))
    discount = calculate_discount(subtotal)
    total = subtotal - discount
    payment = get_payment(total)
    print_receipt(basket, subtotal, discount, total, payment)


if __name__ == "__main__":
    main()
