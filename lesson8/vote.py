voter = {
    "name": input("Enter your full name: "),
    "age": int(input("Enter your age: ")),
    "national_id": input("Enter your national ID: "),
}

if voter["age"] >= 18:
    print("\nRegistration successful!")
    print("Voter details:")
    print(f"Name: {voter['name']}")
    print(f"Age: {voter['age']}")
    print(f"National ID: {voter['national_id']}")
else:
    print("\nRegistration not completed: you must be at least 18 years old.")