class Student:
    def __init__(self, name, age, sex, nationality):
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality = nationality

    def greeting(self):
        print(
            f"My name is {self.name} and I am {self.age} years old and I come from {self.nationality}")


s1 = Student("Moein", 31, "Male", "Iran")

s1.greeting()


class StudentBSBI:
    affiliation = "BSBI"

    def __init__(self, name, age, sex, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


s2 = StudentBSBI("moein", 31, "male", "Iran")
print(type(s2))
