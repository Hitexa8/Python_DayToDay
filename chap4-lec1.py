s="Python"
print(s[0])
print(s[5])
print(s[-1])
print(s[-2])
print(s[-7])
print(s[40])

# Slicing
# [stat:stop:]
s='Hello World'
print(s[0:6])
print(s[2:3])
print(s[0:-1])
print(s[:])
print(s[0:7])
print(s[2:-1])
print(s[:-2])
print(s[1:-1])
print(s[-1:-5])
print(s[2:])

# [stat:stop:step]
s='hello world'
print(s[0:6:2])
print(s[2:4:2])
print(s[2::-1])
print(s[:-1:3])
print(s[::2])
print(s[::-2])
print(s[:-2:2])
print(s[-1:-5:-2])
print(s[1:-5:3])
print(s[:-2:3])

s='hi'
id(s)
del(s)
# id(s)----->gives NameError: name 's' is not defined

dir(s)
help(len)

s='python'
dir(s)
s.
x='\n\nhello'
print(len(x))

s='python'
t='java'
print(s+t)
print(s+t*3)
'z' in t """output:-false"""
'j' in t """output:-true"""

s='python'
for index,value in enumerate(s):
    print(f"The index is {index}and value is {value}")

# common function
s='python'
print(min(s))
print(max(s))
print(sorted(s))
print(len(s))

s.capitalize
help(s.capitalize)

s='python'
print(s.capitalize())
print(s)
print(s.upper())
print(s.lower())
print(s.isupper())
print(s.islower())
a='jAva'
print(a.swapcase())

# count()
s='python is a programming language'
# help(s.count)
# s.count('o')
# s.count('o',1)--->2
# s.count('o',5,-1)

# Find()
s='python is a programming language'
# help(s.find)
print(s.find('o'))
print(s.find('o',5))
print(s.find('o',5,-1))
# Return -1 on failure.

# Index()
s='python is a programming language'
# help(s.index)
print(s.index('o'))
print(s.index('o',5))
print(s.index('o',5,-1))
# Raises ValueError when the substring is not found.

s='Python'
print(s.isalpha())
print(s.isnumeric())
print(s.isalnum())

# help(s.replace)
s='python is python'
print(s.replace('python','java',-1))
print(s.replace('python','java',1))
print(s.replace('python','java',0))
print(s.replace('py','java',-1))
print(s.replace(' ','java',-1))

# help(s.split)
s='python is a programming language , machine,learning'
print(s.split())
print(s.split(',',2))
print(s.split('is'))
print(s.split('language',-1))

# help(s.join)
'.'.join(['ab','cd','ef'])
'🎄'.join(['chri','st','mas'])

