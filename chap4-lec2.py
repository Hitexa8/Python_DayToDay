# help(s.strip)
s=' python '
print(s.strip())
s='ss hello ss'
print(s.strip('ss'))
print(s.strip(' ss'))

intab='aeiou'
outtab='12345'
my='This is a string function'
table=my.maketrans(intab,outtab)
print(my.translate(table))
print(table)

help(my.maketrans)

import string
a_string="!hi $wha?t is [h]like?"
new_string=a_string.translate(str.maketrans(" "," ",string.punctuation))
print(new_string)
string.punctuation

str.capitalize('python')

x=()
type(x)

x=1,2,3
print(x)
type(x)

y=x
x=(3,4,5)
print(y)

x=(6)
print(type(x))
x=(6,)
print(type(x))

x=(1,2,3)
# x[1]=100-->TypeError
# print(x[5])--->IndexError
print(x[-1])

x=('python',[8,4,6],(1,2,3))
print(x[2][0])
print(x[0][3])
x[1][1]=100
print(x)

x=(1,2,3)
help(x)

dir(x)
help(x.index)

x=(1,2,3,4,5)
x.index(4)

x=(1,2,3,4,5,4)
print(x.count(4))
# x.count(40)-->gives 0
help(x.count)

# concat
x=(1,2,3)
y=(4,5,6)
print(x+y)

# comparison
# 1)==
x=(1,2,3)
y=(1,2,3)
print(x==y)

# 2)!=
x=(1,2,3)
y=(1,2,3)
print(x!=y)

# 3)<
x=(1,2,3)
y=(1,2,4)
print(x<y)
# if the elements are equal then it will check the length.
x=(4,4,3,5)
y=(4,4,3)
print(x<y)

# Commn function
x=(1,2,3)
print(len(x))
x=(1,2,[1,2,3])
print(len(x))

x=(1,2,3,'f','g',4)
# max(x)---->TypeError:'>' not supported between instances of 'str' and 'int'

for i in range(0,256):
    print(chr(i))

x=('abc','bc','c','deee')
sorted(x)
print(sorted(x,key=len,reverse=True))

help(sorted)
