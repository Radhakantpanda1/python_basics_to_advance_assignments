print(type(None)) #<class 'NoneType'>

def add():
    s=3+5

print(add())

x=20
def modify_x():
   global x
   x=30
modify_x()
print(x)
