class Employee:
    language="Py"  #This is class attribute
    Salary=100000

ankit=Employee() #  Object created 
ankit.language="Java" #This is an instance object attribute
print(ankit.language, ankit.Salary)
# Note:
# Instance object is preffered over the class attribute
