# Person class

class Person:
    def __init__(self, id, email, firstName, middleName, lastName, bd, age, job, lastLogin):
        self.id = id
        self.email = email
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.birthdate = bd
        self.age = age
        self.job = job
        self.fullName = firstName + (middleName if middleName!="None" else ' ') + lastName
        self.lastLogin = lastLogin