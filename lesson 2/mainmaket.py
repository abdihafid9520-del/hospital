from super import product
product_1=int(input("product one price "))
product_2=int(input("product two price "))
product_3=int(input("product three price "))
total=product(product_1,product_2,product_3)
cash=int(input("Enter your cash"))
balance=cash-total
print("total",total)
print("balance",balance)