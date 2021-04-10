# 
# Example file for variables
#

# Declare a variable and initialize it

f=0 
print(f) 


# re-declaring the variable works

f="tushar"
print(f)


# ERROR: variables of different types cannot be combined

print("hello there, " + str(123)) 


# Global vs. local variables in functions

def someFunction():
    global f
    f="kitten"
    print(f)

someFunction()
print(f)

del f
print(f)


