

patients = []


def add_patient():
    patient_id = input("Enter patient ID: ")
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    department = input("Enter department: ")
    phone = input("Enter phone number: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "department": department,
        "phone": phone
    }

    patients.append(patient)
    print("Patient added successfully!")


def view_patients():
    if not patients:
        print("No patients found.")
        return

    print("\n--- Patients List ---")
    for patient in patients:
        print("---------------------")
        print(f"ID: {patient['id']}")
        print(f"Name: {patient['name']}")
        print(f"Age: {patient['age']}")
        print(f"Gender: {patient['gender']}")
        print(f"Department: {patient['department']}")
        print(f"Phone: {patient['phone']}")


def search_patient():
    search_id = input("Enter patient ID to search: ")

    for patient in patients:
        if patient["id"] == search_id:
            print("\nPatient found:")
            print("---------------------")
            print(f"ID: {patient['id']}")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Department: {patient['department']}")
            print(f"Phone: {patient['phone']}")
            return

    print("Patient not found.")

