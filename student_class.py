class Student:

    def __init__(self, name, major):

        self.name = name

        self.major = major

    def introduce(self):

        print("My name is", self.name)

        print("My major is", self.major)

student1 = Student("Eri", "IT")

student1.introduce()