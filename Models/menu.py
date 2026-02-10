from Core.hospital import Hospital
from Models.department import Department
from Models.patient import Patient
from Models.staff import Staff


'''This module represents the main user interface (Menu System)
for the Hospital Management System.؛ to make it more easier for the user to navigate through different menus
1) Main Menu
2) Department Menu
3) Patient Menu
4) Staff Menu

'''
# Department Menu
def department_menu(hospital):

    while True:
        print("\n===== Department Menu =====")
        print("1. Add Department")
        print("2. View Departments")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Department name: ")
            dept = Department(name)
            print(hospital.add_department(dept))

        elif choice == "2":
            if not hospital.departments:
                print("No departments yet.")
            else:
                for dept in hospital.departments.values():
                    print(dept)

        elif choice == "3":
            break

        else:
            print("Invalid choice")



# Patient Menu   
def patient_menu(hospital):

    while True:
        print("\n===== Patient Menu =====")
        print("1. Add Patient")
        print("2. View Patients in Department")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
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

        elif choice == "2":
            dept_name = input("Department name: ")
            dept = hospital.get_department(dept_name)

            if not dept:
                print("Department not found.")
                continue

            if not dept.patients:
                print("No patients in this department.")
            else:
                for p in dept.patients.values():
                    print(f"{p.id} | {p.name} | {p.medical_record}")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


#  the staff Menu
def staff_menu(hospital):

    while True:
        print("\n===== Staff Menu =====")
        print("1. Add Staff")
        print("2. View Staff in Department")
        print("3. Back")

        choice = input("Choose: ")

        if choice == "1":
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

        elif choice == "2":
            dept_name = input("Department name: ")
            dept = hospital.get_department(dept_name)

            if not dept:
                print("Department not found.")
                continue

            if not dept.staff_members:
                print("No staff in this department.")
            else:
                for s in dept.staff_members.values():
                    print(f"{s.id} | {s.name} | {s.role} | {s.salary}")

        elif choice == "3":
            break

        else:
            print("Invalid choice")


# Main Menu

def main():

    hospital = Hospital("Smart Hospital")

    while True:
        print("\n========== Hospital System ==========")
        print("1. Departments")
        print("2. Patients")
        print("3. Staff")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            department_menu(hospital)

        elif choice == "2":
            patient_menu(hospital)

        elif choice == "3":
            staff_menu(hospital)

        elif choice == "4":
            print("System closed.")
            break

        else:
            print("Invalid choice")


# Entry Point
if __name__ == "__main__":
    main()