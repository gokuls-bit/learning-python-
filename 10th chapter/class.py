class Employee:
    language = "Python"
    salary = 100000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary    
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"This language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, good morning!")


# Provide required arguments while creating objects
jatinder = Employee("Jatinder", 100000, "Python")
jatinder.greet()
jatinder.getInfo()
print(jatinder.name, jatinder.salary, jatinder.language)

samridhi = Employee("Samridhi", 100000, "TypeScript")
samridhi.getInfo()
print(samridhi.name, samridhi.salary, samridhi.language)
