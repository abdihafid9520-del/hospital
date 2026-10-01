def greet(name):
   return("hello",name)
message=greet("abdi")
print(message)

def product():
    name=input(str("enter name"))
    product1=input(str("enter product1 name"))
    product2=input(str("enter product2 name"))
    product_price1=int(input("price1"))
    product_price2=int(input("price 2"))
    total=product_price1+product_price2
    print("total",total)
    print("name",name)
print("thank your for coming")
product()