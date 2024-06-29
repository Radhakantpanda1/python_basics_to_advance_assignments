import math
import calendar

# 1ans.  km to miles
dist_in_km=float(input("Enter the distance in km-"))
dist_in_miles=dist_in_km/1.6
print("Distance in miles=",dist_in_miles)

# 2 ans.      celsius to Fahrenheit
temp_in_celsius=float(input("Enter temperature in celsius-"))
Fahrenheit=(9/5)*temp_in_celsius+32
print('Temperature in Fahrenheit', Fahrenheit)

# 3ans calender
year=2024
month=6
print(calendar.month(year,month))


# 4ans roots of quadratic equation
print("Enter the values of a , b,c in form ax2 + bx +c=0")
a=float(input("Enter the value of a-"))
b=float(input("Enter the value of b-"))
c=float(input("Enter the value of c-"))
discriminant=pow(b,2)-4*a*c
if(discriminant>0):
    print("Real and different roots-")
    root1=(-b+math.sqrt(discriminant))/2*a
    root2=(-b-math.sqrt(discriminant))/2*a
    print("Roots are -", root1,root2)
elif(discriminant==0):
    print('Real and equal roots exist')
    root=-b/2*a
    print("Root=",root)
else:
    print('No real roots exists')

# 5ans
x=int(input("Enter x-"))
y=int(input("Enter y-"))
x=x^y
y=x^y
x=x^y
print('x=',x)
print("y=",y)