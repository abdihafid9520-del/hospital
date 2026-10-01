number1=int(input("enter number 1"))
patners=input(str("enter patners"))
number2=int(input("enter number2"))
sigh=("+","-","*","/")
if sigh=="+":
    print(number1+number2)
elif sigh=="-":
    print(number1-number2)
elif sigh=="*":
    print(number1+number2)
elif sigh=="/":
    if number2==0:
     print("invaled if the nummber is 0")
    print(number1/number2)
