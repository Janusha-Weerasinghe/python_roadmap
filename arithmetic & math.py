friends = 4

#friends = friends +1
#friends += 1
#friends = friends -1
#friends -= 1
#friends = friends *4
#friends *= 4
#friends = friends /3
#friends /= 2
#friends = friends **2
#friends **= 2

#reminder = friends% 2


#print(friends)
#print(f"{friends:.2f}")
#print(reminder)
####################################################
#x = 3.14
#y = 4
#z = 5

#result = round(x)
# result = abs(y)
#result=pow(4,3)
#result= max(x,y,z)
#result = min(x,y,z)

#print(result)
#########################################

#  import math

#x= 9

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)
#print(result)

#######################################
# find the circumference of the circle

#import math

#radius = float(input("Enter the radius of the circle : "))

#circumference = 2 * math.pi * radius

#print(f"Your circumference is : {circumference:.2f}cm")

###################
#import math
#radius = float(input ("Enter the redius of the circle"))

#circumference = math.pi * pow(radius,2)

#print (f"Your circle circumference is: {round(circumference,2)}cm²")

##########################################
#c=((a)² + (b)²) power 1/2
import math
a = float(input("Enter Side A : "))
b = float(input("Enter Side B : "))

c = math.sqrt(pow(a,2)+ pow(b,2))

print (f"Side C= {c}")