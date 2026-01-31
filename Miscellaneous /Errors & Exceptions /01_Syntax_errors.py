#SYNTAX ERRORS
#Syntax errors are parsing errors which occur when the code is not adhering to Python Syntax.  

if True print("Hello")

#output: syntaxerror: invalid syntax
#When there is a syntax error, the program will not execute even if that part of code is not used

print("Hello")  
  
def greet():  
    print("World"
        
#OUTPUT : SyntaxError: unexpected EOF while parsing
#Notice that in the above code, the syntax error is inside the greet function, which is not used in rest of the code.
