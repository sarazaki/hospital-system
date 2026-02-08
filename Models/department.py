"""
This Class Represents a department within a hospital.

Attributes:
    name(str): Name of the department.
    patients(list): List of patients assigned to this department.
    staff_members(list): List of staff members working in this department.    
"""

class Department():
    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.staff_members = {}

    def __repr__(self):
        return f"Department Name : {self.name}, Patients: {len(self.patients)}, Staff_Members: {len(self.staff_members)}"

    def add_patient(self, patient):
        """
        This Function adds a patient to the department.
        
        Args:
            patient (Patient): The patient object to be added.
        """
        if patient.id in self.patients:
            return "The Patient Already Exists."
        else:
            self.patients[patient.id] = patient
            return "Patient Added Successfully!"

    def add_staff(self, staff_member):
        """
        This Function Adds a staff member to the department.
        
        Args:
            staff_member (Staff): The staff member object to be added.
        """
        # Assign department automatically
        staff_member.department = self.name

        if staff_member.id in self.staff_members:
            return "Staff Member Already Exists."
        else:
            self.staff_members[staff_member.id] = staff_member
            return "Staff Member Added Successfully!"
