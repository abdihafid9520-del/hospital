greeting = "Welcome to Customer service system"

title  = "Register Customer "
action = "Calculate"
status = "Check customer status"
exit = "Exit"

omputerrepai = 2000
customer_name=input(str(" what is u name"))
age=input(str("your age"))
phone=input(str("enter phone number"))
location=input(str("enter your location"))

service_choice=input(str("we have service like internt,printing, computer repair,training"))
if service_choice=="internt":
    print("choice 1")
elif service_choice=="printing":
    print("choice 2")
elif service_choice=="computer repair":
    print("choice 3")
elif service_choice=="training":
    print("choice 4")
service_pricing=input(str("price for choice 1,choice 2,choice 3,choice 4"))
if service_pricing=="choice 1":
    print("5000")
elif service_pricing=="choice 2":
    print("3000")
elif service_pricing=="choice 3":
    print("4000")
elif service_pricing=="choice 4":
    print(" 60000")

if service_choice==1:
    quantity=int(input("number of moth"))
elif service_choice==2:
    quantity=int(input("number of pages"))
elif service_choice==3:
    quantity=int(input("number of devices"))
elif service_choice==4:
    quantity=int(input("number of sessions"))
    total_bill= service_pricing(service_choice,quantity)
    





















