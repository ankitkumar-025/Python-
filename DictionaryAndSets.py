# Ḍictionaries are collection of key value pairs..
# d={) Empty Dictionary
marks={
    "ankit":100,
    "ankit1":23
}
# print(marks,type(marks))
# print(marks["ankit"])
# print(marks["ankit1"])
# Properties of python Dictionaries:
# It is unorderd.mutable,indexed, Cnnot contain dupicate keys.
# Dictionary    Methods:

# print(marks.items())# List the items of dictionaries
# print(marks.keys())
# print(marks.values())
# marks.update({"ankit":99})
# print(marks) 
print(marks.get("ankit2")) #Prints None

# print(marks["ankit2"]) # returns an error

# SETS IN PYTHON:
# Set is a collection of non-repetative elements:
# s=set() #Empty set
# In set element does not repeat..

# print(type(s)) 
# SET METHODS:--
s={1,23,456,42,5,563,5,1}
s.add(67)
print(s,type(s))
# s.remove()
# OPERATIONS ON SET:
s2={2,3,45,6,1,2}
s3={2,3,421,344,53}
print(s2.union(s3))
print(s2.intersection(s3))# Common values..






