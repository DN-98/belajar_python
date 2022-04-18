
# ? calling a function
# Function definition is here
def printme( str ):   
    "This prints a passed string into this function"   
    print(str)   
    return
# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# ? required argument
# Function definition is here
def printme( str ):   
    "This prints a passed string into this function"   
    print(str)   
    return
# Now you can call printme function
printme("test")

# Function definition is here
def printme( str ):   
    "This prints a passed string into this function"   
    print(str)   
    return
# Now you can call printme function
printme(str = "Hacktiv8")


# ? default argument
# Function definition is here
print("\nDefault argument\n")
def printinfo( name, age = 26 ):   
    "This prints a passed info into this function"   
    print("Name: ", name)   
    print("Age: ", age)   
    return
# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

# * ini jika parameters sudah urut
#// print("tanpa_var")  

# ? variable length argument 
print("\nvariable length argument\n")
def functionname(a, *args_tambahan ):   
    "function_docstring"   
    print(a)
    print(args_tambahan)
    return 
functionname("ini formal arg", 1,2,3,"bebas")

# ? The Anonymous Functions
print("\nThe Anonymous Functions\n")
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2
# def sum(arg1, arg2): 
#     return arg1 + arg2
# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

# ? return statement
# Function definition is here
def sum(arg1, arg2):    
    # Add both the parameters and return them."    
    total = arg1 + arg2    
    total2 = total + arg1    
    print("Inside the function : ", total)    
    return total2
    
# Now you can call sum function
total = sum(10, 20)
print("Outside the function : ", total)


# ? global variable vs local variable

total = 0  #This is global variable
def sum( arg1, arg2 ):   
    total = arg1 + arg2 # Here total is local variable.   
    print("Inside the function local total : ", total)   
    return total

sum( 10, 20 )
print("Outside the function global total : ", total)

