# class AdmissionForm:

#     total_students = 0

#     def __init__(self, course, fees):
#         self.__course = course
#         self.fees = fees
#         AdmissionForm.total_students += 1

#     def greeting(self):
#         return "Welcome to College"

#     def getcourse(self):
#         print(f"You are enrolled in {self.__course}")

#     def setcourse(self, course):
#         self.__course = course


# student1 = AdmissionForm("BTech", 25000)
# print(student1.getcourse(), student1.fees)


# student2 = AdmissionForm("BCA", 20000)
# print(student2.getcourse(), student2.fees)

# print(student2.greeting())


# class Enroll:
#     # pass

#     def greeting(self):
#         return "Welcome to class"

# class Exam(AdmissionForm,Enroll):
#     def ExamStart(self):
#       print("Exam Start")
      

# student3 = Enroll()
# # print(student3.getcourse(), student3.fees)
# print(student3.greeting())

# student3.__course = "BTech"
# student3.fees = 40000

# student1.setcourse("BBA")
# # print(student3.getcourse(), student3.fees)
# print(AdmissionForm.total_students)
# print(student1.getcourse(), student1.fees)
# print(isinstance(student1, AdmissionForm))
# print(isinstance(student1, Enroll))

# applicant = Exam("BCA",10000)
# print(applicant.ExamStart())
# print(applicant.greeting())


class A:
  def __init__(self, name):
    self.name = name
    
class B(A):
  def __init__(self, name, gender):
    super().__init__(name)
    self.gender = gender
    
sample = B("Karan", "Male")
print(sample.name)
print(sample.gender)


from abc import ABC, abstractmethod
class GTU(ABC):
  @abstractmethod
  def inst_code(self):
    pass
# a = GTU()
  
class LD(GTU):
  def msg(self):
    print("Welcome to LD")
  
  def inst_code(self):
    print("Institute cod is 101")
sample = LD

class VGEC(GTU):
  def msg(self):
    print("Welcome to VGEC")
  
  def inst_code(self):
    print("Institute cod is 102")
sample = VGEC()

class Admission:
  def __init__(self, college):
    self.college = college
    
  def inst_code(self):
    return self.college.inst_code()

print(sample.msg())
print(sample.inst_code())

s1 = Admission(LD())
print(s1.inst_code())