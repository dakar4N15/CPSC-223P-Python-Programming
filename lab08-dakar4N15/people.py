# Name: William Sutanto
# Date: 4/5/2023
# File Purpose: Multiple people functions. Contain Person class, Faculty class that inherits from Person, and Student class that inherits from Person

#Define a class named Person
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

#Define a class named Faculty that inherits from Person
class Faculty(Person):
    def __init__(self, firstname, lastname, department):
        super().__init__(firstname, lastname)
        self.department = department

#Define a class named Student that inherits from Person
class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

    def set_class(self, classyear):
        self.classyear = classyear

    def set_major(self, major):
        self.major = major

    def set_advisor(self, advisor: Faculty):
        self.advisor = advisor