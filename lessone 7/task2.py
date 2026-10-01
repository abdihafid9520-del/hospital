from datetime import date

student = {
    "name": input("Enter your name: "),
    "birth_year": int(input("Enter your birth year: "))
}

age = date.today().year - student["birth_year"]

if age < 18:
    print("You are too young to proceed to learn.")
else:
    print("You may proceed to learn.")
