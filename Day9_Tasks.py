TASK#1
  Create a lambda function that multiplies argument x with argument y
  
x=lambda a,b:a*b
print(x(5,15))


TASK#2
  Write a Python program to create Fibonacci series to n using Lambda
  
from functools import reduce
fibo=lambda num : reduce(lambda x,_:x+[x[-1]+x[-2]],range(num-2),[0,1])
print(fibo(5))


TASK#3
  Write a Python program that multiply each number of given list with a given number 
  
n=[2,4,6,8,10]
mul=4
print("LIST = ",n)
print("Multiplier = ",mul)
ans=list(map(lambda number:number*mul,n))
print("Multiplied Answer : ")
print(' '.join(map(str,ans)))


TASK#4
  Write a Python program to find numbers divisible by 9 from a list of numbers 
  
n=[9,19,26,36,44,54]
print("LIST = ",n)
print(n)
ans=list(filter(lambda x:(x%9==0),n))
print("Numbers divisible by 9 : ")
print(ans)


TASK#5
  Write a Python program to count the even numbers in a given list of integers 
  
n=[1,2,3,4,5,6,7,8,9,10]
print("LIST = ",n)
print(n)
ans=len(list(filter(lambda x:(x%2==0),n)))
print("No of even numbers in list = ")
print(ans)
