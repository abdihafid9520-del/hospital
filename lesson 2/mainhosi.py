from hosi import services
from financehosi import finance
from tax import taxation
print("frist service is xray")
print("second service is lab test")
print("thrid service is blood test")
patient1=int(input("choose u services"))
cash=int(input("enter cash"))
service_choice=services(patient1)
balance=finance(service_choice)
taxes=taxation(balance)
print(taxes)
