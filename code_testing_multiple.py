string="hello world"
word_count=len(string.split())
print(word_count)

import random

random_number = random.randint(1, 10)
print(random_number)

string="hello world"
new_string="".join(string.split())
print(new_string)

string = "racecar"
if string == string[::-1]:
    print("String is a palindrome!")

string="hello world"
new_string="".join(set(string))
print(new_string)

square=lambda x:x**2
result=square(5)
print(result)

add=lambda x,y:x+y
result=add(3,4)
print(result)

my_list=[1,2,3,4,5]
result=list(map(lambda x:x**2,my_list))
print(result)

my_list=[1,2,3,4,5,6,7,8,9,10]
result=list(filter(lambda x:x%2==0,my_list))
print(result)

from functools import reduce
my_list=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,my_list)
print(result)

a=[1,2,3]
b=a
print(a is b,a==b)

