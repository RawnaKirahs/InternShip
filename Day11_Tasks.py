TASK  # 1
  Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

print("CAPITALS")
list1 = ["TamilNadu", "UP", "AP"]
list2 = ["Chennai", "Lucknow", "Hyderabad"]
list3 = list3 = list(zip(list1, list2))
print(list3)


TASK  # 2
  First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.
  
list1 = ["TamilNadu", "Kerala", "Assam", "Bihar", "AP", "UP", "Punjab", "Rajasthan"]
range = list(range(1, 8))
list = list(zip(list1, range))
print(list)


TASK  # 3
  Using sorted() function, sort the list in ascending order.

list = [5, 6514, 4, 62, 651, 651, 655, 154]
list.sort()
print("SORTED LIST = ", list)


TASK  # 4
  Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

set = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def odd(n):
    if (n % 2) == 0:
        return False
    else:
        return True
oddfilter = filter(odd, set)
print("ODD NUMBERS : ", list(oddfilter))
