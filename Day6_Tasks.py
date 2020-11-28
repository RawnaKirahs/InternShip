TASK#1
  Write a program to loop through a list of numbers and add +2 to every value to elements in list
  
set=[3,6,9,12,15]
for i in range (0,len(set)):
    set[i]+=2
    print(*set)
    
    
TASK#2
  Write a program to get the below pattern
  54321
  4321
  321
  21
  1
  
n=int(input('Enter the num : '))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()
    
    
TASK#3
  Python Program to Print the Fibonacci sequence
  
n=int(input('Enter the n value : '))
a=0
b=1
c=0
count=1
print("Fibo series is : ",end="  ")
while(count<=n):
    print(c,end="  ")
    count+=1
    a=b
    b=c
    c=a+b
    
    
TASK#4
  Explain Armstrong number and write a code with a function
  
num=int(input('Enter the num : '))
n=num

def armstrong(num):
    sum1=0
    num2=num
    count=0
    while(num>0):
        count=count+1
        num=num/10
    while(num2>0):
        rem=num2%10
        sum1+=rem**count
        num2/=10
    return sum1
a=armstrong(num)

if(n==a):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
    
    
TASK#5
  Write a program to print the multiplication table of 9
  
number=9
for i in range(1,11):
    print("%d * %d = %d"%(number,i,number*i))
    
    
TASK#6
  Check if a program is negative or positive
  
n=int(input("Enter a num :"))
if n>0:
    print("Positive Number")
else:
    print("Negative Number")
    
    
TASK#7
  Write a program to convert the number of days to ages
  
day=int(input("Enter Days :"))
age=day/365
print("AGE = ",age)


TASK#8
  Solve Trigonometry problem using math function write a program to solve using math function
  
import math
sum=math.sin(90)+math.cos(90)+math.cos(180)
print(sum)


TASK#9
  Create a calculator only on a code level by using if condition (Basic arithmetic calculation)
  
print("ARITHMETIC CALCULATOR")
print("1.ADD || 2.SUBTRACT || 3.MULTIPLY || 4.DIVIDE")
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
