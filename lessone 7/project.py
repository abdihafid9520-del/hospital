patients = {}

while True:
    print("\n1. Add patient")
    print("2. View all patients")
    print("3. Search for a patient")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        condition = input("Enter condition: ")

        patients[patient_id] = {
            "name": name,
            "condition": condition
        }
        print("Patient added.")

    elif choice == "2":
        if not patients:
            print("No patients recorded.")
        else:
            for patient_id, details in patients.items():
                print(
                    f"ID: {patient_id} | "
                    f"Name: {details['name']} | "
                    f"Condition: {details['condition']}"
                )

    elif choice == "3":
        patient_id = input("Enter patient ID to search: ")

        if patient_id in patients:
            details = patients[patient_id]
            print(f"Name: {details['name']}")
            print(f"Condition: {details['condition']}")
        else:
            print("Patient not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")