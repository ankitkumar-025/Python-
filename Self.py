class Employee:
    language="Py"  #This is class attribute
    Salary=100000
    def getinfo(self): # Method Created
        print(f"The language is {self.language}. The salary is {self.Salary}")


ankit=Employee() #  Object created 
ankit.language="Java" #This is an instance object attribute
print(ankit.language, ankit.Salary)
ankit.getinfo()
# Employee.getinfo(ankit)