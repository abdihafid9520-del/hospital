destination=input(str("your destination"))
distance=float(input("how much distance"))
fuell=float(input("efficiency"))
price=float(input("fuel price"))

print("       ")
print("destination", destination)
print("fuel needed",(distance/fuell))
print("fuell cost",(fuell*price))
