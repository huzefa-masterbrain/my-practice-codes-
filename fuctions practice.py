def greet():
    return "hello"
print(greet(),"glenn")
print(greet(),"sally")
def greet(lang):
    if lang=="es":
        return "hello"
    elif lang=="fr":
        return "bonjour"
    else:
        return "hello"
        print(greet('es'),'sally')
        print(greet('fr'),'michael')
        print(greet('en'),'glenn')
big=max('hello world')
print(big)
def addtwo(a,b):
    added=a+b
    return added
x=addtwo(3,5)
print(x)
n=5
while n>0:
    n=n-1
    print('blastoff!')
    print(n)
#     infinite loop if n=5 or any number above 0
n=-1
while n>0:
    print('lather')
    print('rinse')
    print('dry off')
    while True:
        line=input('>')
    if  line=='done':
     break
     print(line)
     print('done')
     while True:
         line=input('>')
         if line[0]=="#":
             continue
             if line=='done':
                 break
                 print(line)
                 print('done!')
for i in[5,4,3,2,1]:
    print(i)
    print('blastoff')
    friends=['joseph','glenn','sally']
    for friend in friends:
       print('happy new year:',friend)
       print('done')
print('before')
for thing in [9,41,12,3,74,15]:
    print(thing)
    print('after')
# finding the largest value
largest_so_far=-1
print('before',largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far=the_num
        print(largest_so_far,the_num)
        print('after',largest_so_far)
#  counting in a loop
zork=0
print('before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print(zork,thing)
    print('after',zork)
# summing in a loop
zork=0
print('before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+thing
    print(zork,thing)
    print('after',zork)
# finding the average in a loop
count=0
sum=0
print('before',count,sum)
for value in [9,41,12,3,74,15]:
    count=count+1
    sum=sum+value
    print(count,sum,value)
    print('after',count,sum,sum/count)
# filtering in a loop (> < =)
print('before')
for value in [9,41,12,3,74,15]:
    if value>20:
        print('large number',value)
        print('after')
# search using a boolean variable
found=False
print('before',found)
for value in [9,41,12,3,74,15]:
    if value==3:
        found=True
        print(found,value)
        print('after',found)
# how to find the smallest value
smallest_so_far=100
print('before',smallest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num<smallest_so_far:
        smallest_so_far=the_num
        print(smallest_so_far,the_num)
        print('after',smallest_so_far)
# finding the smallest value
smallest=None
print('before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
        print(smallest,value)
        print('after',smallest)
# we can convert number in a string into a number using int()
str1='hello'
str2='there'
bob=str1+str2
print(bob)
str3='123'
x=int(str3)+1
print(x)
# looking inside strings
fruit='banana'
letter=fruit[1]
print(letter)
x=3
w=fruit[x-1]
print(w)
# len fuctions
fruit='banana'
x=len(fruit)
print(x)
# looking index and len of letter
fruit='banana'
index=0
while index<len(fruit):
    letter=fruit[index]
    print(index,letter)
    index=index+1
    fruit='banana'
    for letter in fruit:
        print(letter)
index=0
print('----')
while index<len(fruit):
    letter=fruit[index]
    print(letter)
    index=index+1
# looping and counting letter 'a' which is in banana=3a
word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
        print(count)
    



