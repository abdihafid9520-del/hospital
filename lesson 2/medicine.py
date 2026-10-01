def choose_medicine(choice):
    """Return the name and price of the selected medicine."""
    medicines = {
        1: ("Paracetamol", 100),
        2: ("Amoxicillin", 250),
        3: ("Cough syrup", 300),
    }
    return medicines.get(choice)
