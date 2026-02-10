class Student:
    college_name='ABC College'

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    
    @classmethod
    def change_college(cls,new_name):
        cls.college_name=new_name

    def is_pass(marks):
        if marks >= 35:
            print('Pass')
        else:
            print('Fail')

    def display(self):
        print(f"Name of the  student is {self.name}")
        print(f"Roll number of the  student is {self.roll_no}")

s1=Student("Ria","123AS")
s2=Student("Tia","456AC")

s1.display()
s2.display()

print(Student.college_name)

Student.change_college("XYZ College")

print(s1.college_name)

Student.is_pass(40)
Student.is_pass(30)





