voters={
    "name":input("enter u full name"),
    "age":int(input("enter u age")),
    "id_number":int(input("enter u id number"))
}

if voters["age"] >=18:
    print("registration succesfull!")
    print("voters details")
    print(f"name:{voters['name']}")
    print(f"age:{voters['age']}")
    print(f"id_number:{voters['id_number']}")
else:
    print("grow up ,next u will be part of us") 
