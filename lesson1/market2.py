name="east mart"
served_by=input(str("casheir name"))
product1=input(str("item 1"))
product_price1=int(input("price for item 1"))

product2=input(str("item 2"))
product_price2=(int(input("prive for item 2")))

cash_given=int(input("money given"))

total=(product_price1+product_price2)

vat=(13*total)/100


balance=(cash_given - total)-vat

print("          ")
print("name", name)
print("casheir name")
print("item1",product1)
print("price",product_price1)
print("item2",product2)
print("price",product_price2)
print("money given",cash_given)
print("total" , total)
print("balance", balance)
if balance==500:
    print("your point are",101)
elif balance ==300:
    print("your point are",50)
else: print("not eligible")
    



