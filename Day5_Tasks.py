TASKS :
1)Create a function getting two integer inputs from user. & print the following:

    Addition of two numbers is +value
    Subtraction of two numbers is +value
    Division of two numbers is +value
    Multiplication of two numbers is +value

2. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree


TASK#1 :

def arithmetic(a,b):
    print("Addition = ",a+b)
    print("Subtraction = ",a-b)
    print("Multiplication = ",a*b)
    print("Division = ",a/b)
x=int(input("First Num = "))
y=int(input("Second Num = "))
arithmetic(x,y)


TASK#2

def covid(name,temp=98):
    print("Patient Name : ",name)
    print("Temperature : ",temp)
a=input("Enter the patient's name : ")
covid(a)
