#Namespaces 
#A namespace is a collection of currently defined names along with information about the object that the name references.
#It ensures that names are unique and won’t lead to any conflict.

def greet_1():
    a = "Hello"
    print(a)
    print(id(a))
print("Namespace - 1")
greet_1()
print("Namespace - 2")
greet_2()

''' 
OUTPUT: 

Namespace - 1
Hello
140639382368176
Namespace - 2
Hey
140639382570
'''

#Types of namespaces
#As Python executes a program, it creates namespaces as necessary and forgets them when they are no longer needed.
'''
Different namespaces are:
1.Built-in
2.Global
3.Local

Built-in Namespace
Created when we start executing a Python program and exists as long as the program is running.

This is the reason that built-in functions like id(), print() etc. are always available to us from any part of the program.

Global Namespace
This namespace includes all names defined directly in a module (outside of all functions). 

It is created when the module is loaded, and it lasts until the program ends.

Local Namespace
Modules can have various functions and classes.

A new local namespace is created when a function is called, which lasts until the function returns.
'''

#Global variables
#In Python, a variable defined outside of all functions is known as a global variable.

x = "Global Variable"
print(x)
def foo():
   print(x)
foo()

#eg-2:

def foo():
   print(x)
x = "Global Variable"
foo()

#Local Variables
#In Python, a variable defined inside a function is a local variable.

#This variable name will be part of the Local Namespace which will be created when the function is called and lasts until the function returns.

def foo():
   x = "Local Variable"
   print(x)

foo()
print(x)


#Local import

def foo():
   import math
   print(math.pi)

foo()
print(math.pi)

#Local variables & global variables

x = "Global Variable"

def foo():
    x = "Local Variable"
    print(x)

print(x)
foo()
print(x)

#modifying global variables

x = "Global Variable"

def foo():
    global x    
    x = "Global Change"
    print(x)

print(x)
foo()
print(x)

