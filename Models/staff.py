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

# List to store all staff members
staff_list = []


class Staff:
    """
    Staff Class
    -----------
    Represents a staff member in the hospital.
    """

    def __init__(self, staff_id, name, age, role, department, salary):
        """
        Initialize a staff object.

        Parameters:
        staff_id (int): Unique ID for the staff member
        name (str): Staff member name
        age (int): Staff member age
        role (str): Staff role (Doctor, Nurse, Admin, Technician)
        department (str): Department name
        salary (float): Monthly salary
        """
        self.staff_id = staff_id
        self.name = name
        self.age = age
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


def add_staff(staff):
    """
    Add a new staff member to the staff list.

    Parameters:
    staff (Staff): Staff object to be added
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


def search_staff_by_id(staff_id):
    """
    Search for a staff member using staff ID.

    Parameters:
    staff_id (int): ID to search for
    """
    for staff in staff_list:
        if staff.staff_id == staff_id:
            staff.display_info()
            return
    print("Staff member not found.")


def remove_staff(staff_id):
    """
    Remove a staff member from the staff list using staff ID.

    Parameters:
    staff_id (int): ID of the staff member to remove
    """
    for staff in staff_list:
        if staff.staff_id == staff_id:
            staff_list.remove(staff)
            print("Staff member removed successfully.")
            return
    print("Staff member not found.")


def view_staff_by_role(role):
    """
    Display staff members filtered by role.

    Parameters:
    role (str): Role to filter by (Doctor, Nurse, Admin, Technician)
    """
    found = False
    for staff in staff_list:
        if staff.role.lower() == role.lower():
            staff.display_info()
            print("-" * 40)
            found = True

    if not found:
        print("No staff members found with this role.")
