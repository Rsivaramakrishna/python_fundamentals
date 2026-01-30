#to import modules this is the syntax in python
#importing  modules
#syntax: import module_name

import math
import numpy

#importing from a module
#syntax: from math import factorial

from math import factorial
print(factorial(5))
#output: 120

#aliasing imports
#syntax: from <module_name> import <method/function> as <alias_name>
#eg: from math import factorial as fact

from math import factorial as fact
print(fact(5))
output:120

