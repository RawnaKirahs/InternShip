TASK#1
  List down all the error types and check all the errors using a python program for all errors
  
#TYPES OF ERROR IN PYTHON
TypeError is thrown when an operation or function is applied to an object of an inappropriate type.
KeyError is thrown when a key is not found.
IndexError is thrown when trying to access an item at an invalid index.
ImportError is thrown when a specified function can not be found.
StopIteration is thrown when the next() function goes beyond the iterator items.
ValueError is thrown when a function's argument is of an inappropriate type
ModuleNotFoundError is thrown when a module could not be found.


TASK#2
  Design a simple calculator app with try and except for all use cases
  
print("ARITHMETIC CALCULATOR")
print("1.ADD || 2.SUBTRACT || 3.MULTIPLY || 4.DIVIDE")
try:
    select=int(input("Select from 1,2,3,4 :    "))
    n1=int(input("Enter first num : "))
    n2=int(input("Enter second num : "))
    if select==1:
        print(n1, " + ",n2," = ",n1+n2)
    elif select==2:
        print(n1, " - ",n2," = ",n1-n2)
    elif select==3:
        print(n1, " * ",n2," = ",n1*n2)
    elif select==4:
        print(n1, " / ",n2," = ",n1/n2)
    else:
        print("INVALID")
except NameError:
    print("Please use a number")
except SyntaxError:
    print("Please use a number")
except TypeError:
    print("Please use a number")
except AttributeError:
    print("Please use a number")
except ValueError:
    print("Please use a number")
    
    
TASK#3
  Print one message if the try block raises a NameError and another for other errors
  
try:
    print(a)
except NameError:
    print("Variable not defined")
except:
    print("Something went wrong")
    
    
TASK#4
  When try-except scenario is not required?
  
Basically in try-except:

The try block lets you test a block of code for errors.
The except block lets you handle the error.

When we dont require to check or validate a code, we ned not use tr-except.


TASK#5
  Try getting an input inside the try catch block
  
try:
    n=input("Enter an integer : ")
    n=int(n)
    print("It is an interger")
except ValueError:
    print("Not an integer")
