from .person import Person

"""
This class represents a patient in the hospital system.
It inherits from the Person class and extends it by adding
a medical record specific to the patient.
"""

class Patient(Person):

    def __init__(self, name: str, age: int, medical_record: str):
        """
        Initializes a Patient object.

        :param name: The name of the patient
        :param age: The age of the patient
        :param medical_record: The medical history and current condition of the patient
        """
        # Call the constructor of the parent class (Person)
        # to initialize common attributes like name and age
        super().__init__(name, age)

        # Initialize the patient-specific attribute
        self.medical_record = medical_record

    def view_record(self):
        """
        Returns the medical record of the patient.

        :return: A string containing the patient's medical record
        """
        return self.medical_record
