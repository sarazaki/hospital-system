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
        self.patients = {}        # P1, P2, ...
        self.staff_members = {}  # S1, S2, ...

    def __repr__(self):
        return (f"Department Name : {self.name}, "
                f"Patients: {len(self.patients)}, "
                f"Staff Members: {len(self.staff_members)}")

    def add_patient(self, patient):
        patient_id = f"P{patient.id}"

        if patient_id in self.patients:
            return "The Patient Already Exists."

        self.patients[patient_id] = patient
        return "Patient Added Successfully!"

    def add_staff(self, staff_member):
        staff_id = f"S{staff_member.id}"

        staff_member.department = self.name

        if staff_id in self.staff_members:
            return "Staff Member Already Exists."

        self.staff_members[staff_id] = staff_member
        return "Staff Member Added Successfully!"
