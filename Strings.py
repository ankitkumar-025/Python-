#Strings
# String is a  sequence of characters enclosed in quotes.

name="Ankit"
name='Ankit'
name='''Ankit'''

#String Slicing:
# A string in python can be sliced for getting a part of the strings.

# String is immutable means once it declared it not changed...

# slicing=name[ind_start:ind_end] # First index included ,last index is not included

name="Ankit"
nameshort=name[0:3]#start from index 0 all way till 3 (excluding 3)
print(nameshort)
charcter=name[1]
print(charcter)

#Negative Slicing:
name1="Nayan"
print(name1[-4:-1])
print(name1[1:4])
print(name1[:4])# 0 to 4 ..[0:4]
print(name1[1:])#1 to length ...is same as print(name[1:5])

#Slicing with skip value"
a="123456789"
print(a[1:5:2])
print(a[1:5])
word="amazing"
print(word[1:6:2])
print(word[1:6])

#String Functions:
# 1.len()function:--> This function returns the length of the strings..
name2="Ankit kumar"
print(len(name2))

#2 var_name.endswith():=>This finction tells that whether the variable is ends with "rry" or not..
name3="harry"
print(name3.endswith("rry"))
name5="ankit"
print(name5.endswith("it"))
# Same as var_name.startswith()

#var_name.capitalize()->>only capital 1st character..
print(name5.capitalize())

#4 var_name.replace("old word","new word")
name="hello python"
print(name.replace("python","world"))

#5.upper()
name="ankit"
print(name.upper())
#6.lower()
name1="NAYAN"
print(name1.lower())