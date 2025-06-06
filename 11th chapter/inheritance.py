# # single inheritance
# class Employee:
#     company = "maichudaoltd"
#     def show(self):
#         print(f"the name is {self.name}and the salary is {self.salary}")
# # 
# class Programmer(Employee):
#     company = "maichudaoltdinfo"
#     def showLanguge(self):
#         print(f"the language is {self.language} and the salary is {self.salary} and the name is {self.name}")
# a = Employee()
# b = Programmer()
# print(a.company, b.company)

# multiple inheritance

# class Employee:
#     company = "maichudaoltd"
#     def show(self):
#         print(f"the company is {self.company} ")

# class coder:
#     language = "python"
#     def printLanguage(self):
#         print(f"the language is {self.language}")


# class Programmer(Employee, coder):
#     company = "maichudaoltdinfo"
#     def showLanguge(self):
#         print(f"the language is {self.language}  and the company is {self.company}")
# a = Employee()
# b = Programmer()

# b.show()
# b.printLanguage()
# b.showLanguge()

# multilevel inheritance

# class Employee:
#     a = 1

# class programmer(Employee):
#     b= 2

# class Manager(programmer):
#     c = 3

# o = Employee()
# print (o.a)
# print (o.b)  # This will raise an AttributeError since 'b' is not defined in Employee

# o = programmer()
# print(o.a,o.b,o.c)  # This will work, as 'a' is inherited from Employee


# class method 
# class Employee:
#     a = 1
#     @classmethod
#     def show(self):
#         print(f"the class attribute of a is {self.a}")

# e = Employee()
# e.a = 45  # This creates an instance attribute 'a', shadowing the class attribute

# e.show()

#  property decorator
class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.ename  # Make sure this is defined before calling e.name

e = Employee()
e.a = 45   # This creates an instance variable 'a', but class variable 'a' remains 1
e.ename = "Gokul"  # Now we can use the @property safely

# Testing the methods
e.show()           # Output: The class attribute of a is 1 (still uses class variable)
print(e.name)      # Output: Gokul
# This creates an instance attribute 'a', shadowing the class attribute

 # This will still work, as 'a' is inherited from Employee

