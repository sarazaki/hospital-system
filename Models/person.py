class Person:

    _id_counter = 1

    def __init__(self, name, age):

        self.id = Person._id_counter
        Person._id_counter += 1

        self.name = name
        self.age = age
