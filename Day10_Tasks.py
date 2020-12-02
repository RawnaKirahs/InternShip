TASK#1
  Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
  
import re
a= input("Enter Text: ")
ans=re.sub("[A-Za-z0-9"], '', a)
if len(ans) == 0:
print("It contains only alphabets")
else:
print("It contains other than alphabets")


TASK#2
  Write a Python program that matches a word containing 'ab'.
  
import re
def check(a):
        patterns = '\a*b.\a*'
        if re.search(patterns,  a):
                return 'a and b are found in the text'
        else:
                return('a and b are not found in the text')

print(check("Python Internship"))
print(check("Python Internship program be useful"))


TASK#3
  Write a Python program to check for a number at the end of a word/sentence.
  
import re
def end(string):
    a = re.compile(r".*[0-9]$")
    if a.match(string):
        return 'Number is present at the end'
    else:
        return 'Number is not present at the end'

print(end('Anwar'))
print(end('Anwar1'))


TASK#4
  Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
  
import re
set= re.finditer(r"([0-9]{1,3})", "These are the numberss 1, 12, 13,12,13 and 345")
print("The Numbers of length 1 to 3 are")
for n in set:
     print(n.group(1))
     
     
TASK#5
  Write a Python program to match a string that contains only uppercase letters
  
import re
def match(a):
    pattern = '[A-Z]+$'

    if re.search(pattern, a):
        return ('It contains only upper case')
    else:
        return ('It does not not contain upper case only')


print(match("ANWAR"))
print(match("Anwar"))
