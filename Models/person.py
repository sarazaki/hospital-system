"""
Person Module
-------------
This module defines the Person class, which represents a basic individual
in the system. Each person has a unique ID, a name, and an age.
"""

class Person:
    """
    Represents a person with basic personal information.

    Attributes:
        id (int): Unique identifier for each person.
        name (str): Person's full name.
        age (int): Person's age.
    """

    _id_counter = 1  # Class-level counter to generate unique IDs

    def __init__(self, name: str, age: int):
        """
        Initialize a new Person object.

        Args:
            name (str): The person's name.
            age (int): The person's age.
        """
        self.id = Person._id_counter
        Person._id_counter += 1

        self.name = name
        self.age = age

    def view_info(self) -> str:
        """
        Return the person's information as a formatted string.

        Returns:
            str: A string containing the person's ID, name, and age.
        """
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}"
