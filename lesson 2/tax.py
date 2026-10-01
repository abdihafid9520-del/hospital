from financehosi import finance
def taxation(choice):
    if choice>=1000:
        tax=0
        print("no tax")
    elif choice>=3000:
        tax=choice*0.05
        total = tax + choice
        print("tax is",tax)
        print("Total payable plus tax is ", total)

    elif choice>=5000:
        tax=choice*0.09
        total = tax + choice
        print("tax is ",tax)
        print("Total payable plus tax is ", total)
    elif choice>=6000:
        tax=choice*0.10
        total = tax + choice
        print("tax is ",tax)
        print("Total payable plus tax is ", total)
    else:print("invaled")
    return choice





