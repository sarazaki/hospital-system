from Core.hospital import Hospital
from Models.department import Department
from Models.patient import Patient
from Models.staff import Staff


def show_menu():

    print("\n===== Hospital Management System =====")
    print("1. Add Department")
    print("2. Add Patient")
    print("3. Add Staff")
    print("4. View Departments")
    print("5. Exit")


def main():

    hospital = Hospital("Smart Hospital")

    while True:

        show_menu()
        choice = input("Choose an option: ")

        # ===============================
        # Add Department
        # ===============================
        if choice == "1":

            name = input("Department name: ")

            dept = Department(name)

            print(hospital.add_department(dept))

        # ===============================
        # Add Patient
        # ===============================
        elif choice == "2":

            dept_name = input("Department name: ")

            dept = hospital.get_department(dept_name)

            if not dept:
                print("Department not found.")
                continue

            name = input("Patient name: ")
            age = int(input("Age: "))
            record = input("Medical record: ")

            patient = Patient(name, age, record)

            print(dept.add_patient(patient))

        # ===============================
        # Add Staff
        # ===============================
        elif choice == "3":

            dept_name = input("Department name: ")

            dept = hospital.get_department(dept_name)

            if not dept:
                print("Department not found.")
                continue

            name = input("Staff name: ")
            age = int(input("Age: "))
            role = input("Role: ")
            salary = float(input("Salary: "))

            staff = Staff(name, age, role, dept_name, salary)

            print(dept.add_staff(staff))

        # ===============================
        # View Departments
        # ===============================
        elif choice == "4":

            if not hospital.departments:
                print("No departments yet.")
                continue

            for dept in hospital.departments.values():

                print(f"\nDepartment: {dept.name}")

                print("Patients:")
                for p in dept.patients.values():
                    print(f"- {p.id} | {p.name}")

                print("Staff:")
                for s in dept.staff_members.values():
                    print(f"- {s.id} | {s.name} ({s.role})")

        # ===============================
        # Exit
        # ===============================
        elif choice == "5":

            print("System closed.")
            break

        else:
            print("Invalid choice.")


# Entry Point
if __name__ == "__main__":
    main()
