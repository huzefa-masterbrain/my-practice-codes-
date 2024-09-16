s='monty python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])
# string concatenation
a='hello'
b=a+'there'
print(b)
c=a+' '+'there'
print(c)
fruit='banana'
if 'n' in fruit:
    print('found it!')
    if 'nan' in fruit:
        print('banana')
        if 'b' in fruit:
            print('banana')
# string comparison
'''if word=='banana':
    print('all right,banana.')
    if word<'banana':
        print('your word,' 'word +''come before banana.')
    elif word ('your word,' 'word +''come before banana.')
    else:
        print('all right,banana.')'''
# lowering case
greet ='HELLO BOB'
zap=greet.lower()
print(zap)
print('Hi There'.lower())
# finding function
fruit='banana'
pos=fruit.find('na')
print(pos)
aa=fruit.find('2')
print(aa)
# uppercase
greet='hello bob'
nnn=greet.upper()
print(nnn)
# replace function
greet='hello bob'
wstr=greet.replace('bob','jane')
print(wstr)
# replacing letter
wstr=greet.replace('o','x')
print(wstr)
# stripping whitespace
# lstrip() and rstrip() remove wnitespace at the left or right
# strip() remove both beginning and ending whitespace
greet='  petrol tank  '
greet.lstrip()
print(greet)
greet='  5 core  '
greet.rstrip()
print(greet)
greet='  white board  '
greet.strip()
print(greet)
line='please have a nice day'
line.startswith('please')
print(line)
# parsing and extracting
data='from stephen.marquard@uct.ac.za sat jan 5 09:14:16 2008'
atpos=data.find('@')
print(atpos)
sppos=data.find(' ',atpos)
print(sppos)
host=data[atpos+1:sppos]
print(host)
# breaking word to new line down
stuff='hello\nword!'
print(stuff)
stuff='x\ny'
print(stuff)
stuff='xy'
len(stuff)
print(stuff)
