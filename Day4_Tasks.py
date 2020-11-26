Tasks : 
1.Write a program to create a list of n integer values and do the following
-Add an item in to the list (using function)
-Delete (using function)
-Store the largest number from the list to a variable
-Store the Smallest number from the list to a variable

2) Create a tuple and print the reverse of the created tuple

3) Create a tuple and convert tuple into list


#TASK1

set = [7,9,1,99,41,54]
set.append(2)       #ADDING
print(set)

set.remove(2)       #REMOVING
print(set)

set.sort()
print("Largest = ",set[-1])
Largest =  99     
print("Smallest = ",set[0])
Smallest =  1



#TASK2

set1=[1,3,5,7,9,11]
set2=reversed(set1)
print(tuple(set2))


#TASK3

set1=[2,4,6,8,10,12]
set2=list(set1)
print(set2)
