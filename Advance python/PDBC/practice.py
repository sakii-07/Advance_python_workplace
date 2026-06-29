class Student:

    def __init__(self,n):
        self.name = n

    def getname(self):
        print(self.name)
        print("Student class function called")

class Teacher:

    def __init__(self,n):
        self.name = n
        
    def getname(self):
        print(self.name)
        print("Teacher class function called")


class college(Teacher,Student):
    def __init__(self,n):
        self.name = n

c = college("Sakshi")
c.getname()
print(college.mro())


