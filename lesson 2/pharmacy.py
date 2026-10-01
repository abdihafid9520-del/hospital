from medicine import choose_medicine
from pharmacyfinance import calculate_bill
from pharmacytax import calculate_tax


print("--- PHARMACY ---")
print("1. Paracetamol - 100")
print("2. Amoxicillin - 250")
print("3. Cough syrup - 300")

choice = int(input("Choose medicine (1-3): "))
quantity = int(input("Enter quantity: "))

selected_medicine = choose_medicine(choice)

if selected_medicine is None:
    print("Invalid medicine choice.")
elif quantity <= 0:
    print("Quantity must be greater than zero.")
else:
    name, price = selected_medicine
    bill = calculate_bill(price, quantity)
    tax = calculate_tax(bill)
    total = bill + tax

    print("Medicine:", name)
    print("Bill:", bill)
    print("Tax:", tax)
    print("Total to pay:", total)
