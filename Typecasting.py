# Typecasting = the process of covering a variable from one data type to another
#               str(), int() , float(), boll()
# To handle the user inputs
name= "janusha"
age = 26
gpa = 3.6
is_student = True

print(type(is_student))

gpa= int(gpa)
print(gpa)

age = float(age)
print(age )

age =str(age)
age += "1"
print (age)


name = bool(name)
print(name)
#if the name variable is empty it will give the output "False"