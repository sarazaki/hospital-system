from Models.department import Department


class Hospital:
    """
    Represents the main hospital system.
    Manages departments, patients, and staff.
    """

    def __init__(self, name: str):

        self.name = name
        self.departments = {}


    # ===============================
    # Department Management
    # ===============================

    def add_department(self, department: Department):

        if department.name in self.departments:
            return "Department already exists."

        self.departments[department.name] = department
        return "Department added successfully."


    def remove_department(self, name: str):

        if name not in self.departments:
            return "Department not found."

        del self.departments[name]
        return "Department removed."


    def get_department(self, name: str):

        return self.departments.get(name)


    def list_departments(self):

        return list(self.departments.values())


    # ===============================
    # System Info
    # ===============================

    def get_summary(self):

        summary = {
            "hospital_name": self.name,
            "total_departments": len(self.departments),
            "total_patients": sum(
                len(d.patients) for d in self.departments.values()
            ),
            "total_staff": sum(
                len(d.staff_members) for d in self.departments.values()
            )
        }

        return summary
