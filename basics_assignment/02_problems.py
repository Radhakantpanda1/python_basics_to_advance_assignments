#3ans
print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)
print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)
print( not 0)
print( not 1)

# 4 ans
print((5 > 4) and (3 == 5)) # false
print(not (5 > 4)) #false
print((5 > 4) or (3 == 5))#true
print(not ((5 > 4) or (3 == 5)))#false
print((True and True) and (True == False))#false
print((not False) or (not True))#true

# 7ans
spam = 0

if spam == 10:
    print('eggs')

if spam > 5:
    print('bacon')

else:
    print('ham')
    print('spam')
    print('spam')

# 8 ans
spam=int(input("Enterthe number-"))
if spam==1:
    print(1)
elif spam==2:
    print("Hello")
else:
    print("Greetings!")

#12ans
# using for loop
for i in range (0,11):
    print(i)

# using while loop
i=0
while i<11:
    print(i)
    i+=1

for j in range(10):
    print(j)