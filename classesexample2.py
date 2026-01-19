# class Studentdetails:
#     def __init__(self , name , mark):
#         self.name=name
#         self.mark=mark
#     def marks(self):
#         if self.mark>=90:
#             print("Grade:A")
#         elif self.mark>70:
#             print("Grade:B")
#         elif self.mark>50:
#             print("Grade:C")
#         else:
#             print("failed")  
#     def student_info(self):
#         print(f"name:{self.name} mark:{self.mark}")        
# Student1=Studentdetails("liza",80)
# Student2=Studentdetails("riza",90)
# Student1.student_info()
# Student1.marks()    
# Student2.student_info()
# Student2.marks() 
# 

# class Employee:
#     company = "ABC crop"  

#     def __init__(self , name , position):
#         self.name=name
#         self.position=position

# emp1=Employee("Afa","Manager")
# emp2=Employee("Sajidha","Developer")  

# print(emp1.company)
# print(emp2.company)

# print(emp1.name)
# print(emp2.name)   
# 
# 
# class Employee:
#     class company: 

#      def __init__(self , cname , location ):
#         self.cname=cname
#         self.location=location

#     def __init__(self,name,salary,cname,location):
#        self.name=name
#        self.salary=salary
#        self.company = Employee.company(cname , location )

#     def display_employee(self):
#        print(f"name: {self.name}, salary: {self.salary}, company:{self.company.cname}, location:{self.company.location}")
# emp= Employee("afa", 50000 , "xyx crop", "london",c1 )  
# emp.display_employee()  
# 
# 
# class Company:
#     def __init__(self, cname, location):
#       self.cname = cname
#       self.location = location
# class Employee:
#     def __init__(self, name, salary, cname, location):
#       self.name = name
#       self.salary = salary
#       self.company = Company(cname, location) # object created here
#     def display_employee(self):
#        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company.cname}, Location: {self.company.location}")
# emp = Employee("John", 50000, "XYZ Corp", "London")
# emp.display_employee()

# class Engine:
#     def __init__(self, model):
#       self.model = model
# class Car:
#     def __init__(self, model):
#       self.engine = Engine(model) # Engine created inside → tight
# car = Car("V6")
# print("Engine model before deleting Car:", car.engine.model)
# del car
# try:
#  print(car.engine.model)
# except Exception as e:
#  print("Error:", e) # Engine no longer exists


   



class Studentdetails:
    marks_info={"students1":{

    }
           }
    def __init__(self , name , mark):
        self.name=name
        self.mark=mark
    def marks(self):
        if self.mark>=90:
            print("Grade:A")
        elif self.mark>70:
            print("Grade:B")
        elif self.mark>50:
            print("Grade:C")
        else:
            print("failed")  
    def student_info(self):
        print(f"name:{self.name} mark:{self.mark}")        
Student1=Studentdetails("liza",80)
Student2=Studentdetails("riza",90)
Student1.student_info()
Student1.marks()    
Student2.student_info()
Student2.marks()


       
   
        

          
             
        

