# Solving a problem by creating object is one of the most popular approaches in programming .This is called the object oriented programming.
# This concept focuses on using reusable code(DRY principle)

#Class:
#  A class is a blueprint for creating object.

class Employee:
    # name="Ankit"
    language="Py"  #This is class attribute
    Salary=100000

ankit=Employee() #  Object created 
ankit.name="Ankit"  #This is an instance object attribute
print(ankit.name, ankit.Salary)

nayan=Employee()
nayan.name="Nayan"
print(nayan.name,nayan.language,nayan.Salary)

# Here name is object attribute and salary and lang are class attribute as they directly belong to the class..

# Modelling a problem in OOPs:
# Noun->Class->Employee
# Adjective->Attribites->name,lang,salary
# Verbs-> Methods ->getsalary(), increment()