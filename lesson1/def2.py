def products():
    print("product1 :bag price:200")
    print("product2 :juice price: 100")
    print("product3 :yogurt price: 150")

def calculte_total():
    total=0
    while True:
        products()
        choice=int(input("choose the product u want to by"))
        if choice==0:
            print("invaled choice")
            break
        elif choice==1:
            quantity=int(input("select the product u want to choose:"))
            total=total+(200*quantity)
        elif choice==2:
            quantity=int(input("select the product u want to choose:"))
            total=total+(100*quantity)
        elif choice==3:
            quantity=int(input("select the product u want to choose"))
            total=total+(150*quantity)
        else:
            print(" invaled product")
            print("total price",total)
            return total
def payment(total):
    cash=int(input("cash give"))
    if cash>=total:
        balance=cash-total
        print("balance",balance)
    elif cash<=total:
        print("insufficient funds")
        print("your should add",total-cash)
def main():
    total=calculte_total()
    payment(total)
main()


        
            

        
    

