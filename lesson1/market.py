name="Naivas"

served_by = input(str("Enter Cashier name"))

product1=input(str("item 1"))
price_product1 = int(input("Enter price for 1st item "))

product2 = input(str("Item 2"))
price_product2 = int(input("Price 2"))

cash_give = int(input("Money given"))

total = price_product1 + price_product2

vat = (13*total)/100

balance = (cash_give - total) - vat

print("-----RECEIPT SUMMARY----")
print("name", name)
print("cashier name", served_by)
print("item 1", product1)
print("price", price_product1)
print("item 2",product2)
print("price",price_product2)
print("money given", cash_give)
print("total",total)
print("balance",balance)