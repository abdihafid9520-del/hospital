from datetime import date

student={
    "name":input(str("enter u name")),
    "year of bath":int(input("enter of bath"))
}
age=date.today().year - student["year of bath"]

if age<18:
    print("your are to young to proceed")
elif age>18:
    print("your may proceed with your education")

