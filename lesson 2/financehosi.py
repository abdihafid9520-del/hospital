from hosi import services
consultaion=float(1000)

def finance(choice):
    if choice==1:
        total=consultaion+1000
        print("total is",total)
    elif choice==2:
        total=consultaion+4000
        print("total is", total)
    elif choice==3:
        total=consultaion+5000
        print("total is",total)
    else: print("invaled choice")
    return choice
   
