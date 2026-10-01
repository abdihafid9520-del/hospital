name=input(str("busseness name"))
served=int(input("number customer served"))
cash=float(input("cash sales"))
mobile=(float(input("money cost")))
total_sale = (cash + mobile) * served
averrage=total_sale/served
print("       ")
print("bussness name",name)
print("customers",served)
print("total sales", total_sale)
print("averrage",averrage)