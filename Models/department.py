"""
This Class Represents a department within a hospital.

Attributes:
    name(str): Name of the department.
    patients(list): List of patients assigned to this department.
    staff_members(list): List of staff members working in this department.    
"""

class Department:
    def __init__(self,name):
        self.name = name
        self.patients = []
        self.staff_members = []
        
    def __repr__(self):
        return f"Department Name : {self.name}, Patients: {len(self.patients)}, Staff_Members: {len(self.staff_members)}"  
    
    def add_patient(self,patient):
        """
        This Function adds a patient to the department.
        
        Args:
            patient (Patient): The patient object to be added.
        """    
        if patient not in self.patients:
            self.patients.append(patient)
            return "Patient Added Successfully!"
        else:
            return "The Patient Already Exists."
        
    def add_staff(self,staff_member):
        """
        This Function Adds a staff member to the department.
        
        Args:
            staff_member (Staff): The staff member object to be added.
        """
        if staff_member not in self.staff_members:
            self.staff_members.append(staff_member)
            return "Staff Member Added Successfully!"
        else:
            return "Staff Member Already Exists."