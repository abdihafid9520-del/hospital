product={"name":"bag", 
         "price":100
         }
print(f"we sell{product['name']}")



def calculate_total(quantity):
    quantity=int(input("quantity?"))
    total=product['price']*quantity
    print(f"your total is {total}")
    return total
calculate_total(0)