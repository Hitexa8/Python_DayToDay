x=[]
type(x)

x=[1,2,3,4]
print(x)

x[0]=100
print(x)

print(id(x[0]))
print(id(x[1]))

# it change variable value inplace
x[3]='hello'
print(x)

x=[6,3,1,2,9]
print(sorted(x))
# sorted does not change inplace
print(x)

del(x[1])
print(x)

x=[1,2,3,4,5]
y=[4,3,2,1]
print(x+y)

# slicing
print(x[0:6:2])
print(x[0:3])
print(x[-1])

# append
x.append(100)
print(x)

x.append((100,200))
print(x)

# extend
# x.extend(4)--->TypeError: 'int' object is not iterable
x.extend([100])

print(x)
x.extend('hello')
print(x)

x.extend([7,8,9])
print(x)

# insert
x.insert(3,'c#')
print(x)

# remove()
z=[1,2,3,4,2]
z.remove(2)
# z.remove(5)--->ValueError: list.remove(x): x not in list
print(z)

x=[1,2,3,4,5]
x.pop()
print(x)
x.pop(1)"""-->output 2"""
print(x)

# clear()
x.clear()
print(x)

x=[1,100,2,9]
x.sort()
print(x)

# index()
a=[33,6,23,21,2]
a.index(6)


# reverse()
x=[1,2,3,4,5]
x.reverse()
print(x)

# reversed
x=[1,2,3,4,5]
y=list(reversed(x))
print(y)

# copy()
x=[1,2,3]
y=x
y[1]=100
print(x)

y=x.copy()
y[2]=500
print(x)
print(y)

# CEASER CIPHER
string=input("Enter String")
intab='abcdefghijklmnopqrstuvwxyz'
outtab='defghijklmnopqrstuvwxyzabc'
table=string.maketrans(intab.upper(),outtab.upper())
print(string.translate(table))

def encrypt(key,message):
    message=message.upper()
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=""
    for letter in message:
        if letter in alpha:
            letter_index=(alpha.find(letter)-key)%xlen(alpha)
            result=result+alpha(letter_index)
        else:
            result=result+letter
    return result
message=input("Enter message ")
key=input("Enter key ")
print(encrypt(key,message))

  

#wap to count no.of words in given string without using split
string=input("Enter string ")
count=0
for i in string:
    if i==" ":
        count=count+1
count+=1
print(count)
