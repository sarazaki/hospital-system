"""
Staff Module
------------
This module is responsible for managing staff members in the hospital system.
It includes:
- Staff class
- Functions to add, view, search, and remove staff members

Staff types are handled using the 'role' attribute
(e.g., Doctor, Nurse, Admin, Technician)
"""

from person import Person

# List to store all staff members
staff_list = []


class Staff(Person):
    """
    Represents a staff member in the hospital.
    Inherits from Person and adds staff-specific attributes.
    """

    def __init__(self, staff_id: int, name: str, age: int,role: str, department: str, salary: float):
        """
        Initialize a staff object.
        """
        super().__init__(name, age)

        self.staff_id = staff_id
        self.role = role
        self.department = department
        self.salary = salary

    def display_info(self):
        """
        Display all information of the staff member.
        """
        print(f"Staff ID   : {self.staff_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Role       : {self.role}")
        print(f"Department : {self.department}")
        print(f"Salary     : {self.salary}")


def add_staff(staff: Staff):
    """
    Add a new staff member to the staff list.
    """
    staff_list.append(staff)
    print("Staff member added successfully.")


def view_all_staff():
    """
    Display all staff members in the hospital.
    """
    if not staff_list:
        print("No staff members found.")
        return

    for staff in staff_list:
        staff.display_info()
        print("-" * 40)


def search_staff_by_id(staff_id: int):
    """
    Search for a staff member using staff ID.
    """
    for staff in staff_list:
        if staff.staff_id == staff_id:
            staff.display_info()
            return
    print("Staff member not found.")


def remove_staff(staff_id: int):
    """
    Remove a staff member from the staff list using staff ID.
    """
    for i, staff in enumerate(staff_list):
        if staff.staff_id == staff_id:
            del staff_list[i]
            print("Staff member removed successfully.")
            return
    print("Staff member not found.")


def view_staff_by_role(role: str):
    """
    Display staff members filtered by role.
    """
    found = False
    for staff in staff_list:
        if staff.role.lower() == role.lower():
            staff.display_info()
            print("-" * 40)
            found = True

    if not found:
        print("No staff members found with this role.")
