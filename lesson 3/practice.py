second=int(input("Enter your numbers "))
operator = input("Enter your opertoar")
first=int(input("Enter second number "))

def calculator(first,operator,second):
    if operator=="+":
        return first+second
    elif operator=="-":
        return first-second
    elif operator=="*":
        return first*second
    elif operator=="/":
        if second==0:
            return"error: u cannot divid by zero"
        return first/second
    return "error:choose +,-,*or/"


ans = calculator(first, operator, second)
print(ans)