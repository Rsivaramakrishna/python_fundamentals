#EXCEPTIONS
# Even when a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it
#Errors detected during execution are called exceptions.   

'''
Example Scenario

We wrote a program to download a Video over the Internet.  

Internet is disconnected during the download
We do not have space left on the device to download the video

Example 1

Division Example
Input given by the user is not within expected values.  

'''
def divide(a, b):  
    return  a / b  

divide(5, 0)

#OUTPUT: ZeroDivisionError: division by zero

#example-2
  
def divide(a, b):  
    return  a / b  

divide("5", "10")

#OUTPUT: TypeError: unsupported operand type(s) for /: 'str' and 'str'

#example 3 

class Store:  
    def __init__(self):  
        self.items = {  
        "milk" : 20, "bread" : 30, }  
    
    def add_item(self, name, quantity):  
       self.items[name] += quantity  
 
s = Store()  
s.add_item('biscuits', 10)

#OUTPUT: 'biscuits'



