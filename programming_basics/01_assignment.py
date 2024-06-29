import math
import random
# 1 ans.
print("Hello Python")

#2ans
def division(x,y):
    return x/y
def addition(x,y):
    return x+y
print(division(3,9))
print(addition(25,36))

# 3ans
print("Enter the sides of a triangle")
a=int(input("Enter the side a-"))
b=int(input("Enter the side b-"))
c=int(input("Enter the side c-"))
s=(a+b+c)/2
if (a+b>c and b+c > a and a+c >b):
    area=s*(s-a)*(s-b)*(s-c)
    area=math.sqrt(area)
    print(area)
else:
    print("Sides are not of a triangle-")

# 4ans.
x=int(input("Enter x-"))
y=int(input("Enter y-"))
x=x^y
y=x^y
x=x^y
print('x=',x)
print("y=",y)

# 5ans.
print("Random number=",random.randint(3,99))

