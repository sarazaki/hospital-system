"""
Staff Module
------------
This module is responsible for managing staff members in the hospital system.
It includes:
- Staff class

Staff types are handled using the 'role' attribute
(e.g., Doctor, Nurse, Admin, Technician)
"""

from .person import Person


class Staff(Person):
    """
    Represents a staff member in the hospital.
    Inherits from Person and adds staff-specific attributes.
    """

    def __init__(self, name: str, age: int, role: str, department: str, salary: float):
        """
        Initialize a staff object.
        """
        super().__init__(name, age)

        self.role = role
        self.department = department
        self.salary = salary

    def display_info(self):
        """
        Display all information of the staff member.
        """
        print(f"Staff ID   : {self.id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Role       : {self.role}")
        print(f"Department : {self.department}")
        print(f"Salary     : {self.salary}")
