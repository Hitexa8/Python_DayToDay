# TO PRINT A PATTERN
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

n=4
for i in range(1,n+1):
    for k in range(1,i+1):
        if(i%2==0):
            print("#",end="")
        else:
            print("*",end="")
    print()

# TO CHECK ARMSTRONG NUMBER
n=153
temp=n
temp1=n
sum=0
count=0
while temp>0:
    count+=1
    temp=temp//10
    
while temp1>0:
    r=temp1%10
    sum=sum+(r**count)
    temp1=temp1//10
    
if(sum==n):
    print("armstrong number")
else:
    print("not armstrong")

# TO PRINT PRIME NUMBER
n=int(input("Enter the number prime number"))
for i in range(2,n):
    if(n%i==0):
        print(i,"is not prime number")
    else:
         print(i,"is prime number")



def greet():
    print("Hello World")
greet()

def add(x,y):
    
    """
    This function adds 2 number
    parameters
    x(int)=first integer
    y(int)=second integer
    returns:sum of x and y

    """
    sum=x+y
    return sum
add(3,1)

add

add.__doc__

def greet(name,greeting="Hello"):
    print(greeting,name)
greet("Alice","good moring")

def greet(greeting="Hello"):
    print(greeting)
greet("Hii")

# WRITE A FUNCTION TO ACCEPT A NUMBER TO CEHCK IF IT IS ODD OR EVEN.
n=int(input("Enter number to check "))
def oddoreven(n):
    if(n%2==0):
        print("Number is even")
    else:
        print("Number is odd")
oddoreven(n)

# CALCULATOR
def calculator(x,y,choice):
    if(choice==1):
        return x+y
    elif(choice==2):
        return x-y
    elif(choice==3):
        return x*y
    elif(choice==4):
        return x/y
num1=int(input("Enter number 1 "))
num2=int(input("Enter number 2 "))
choice=int(input("Enter your choice:(1) for addition, (2) for subtraction, (3) for multiplication, (4) for division"))
calculator(num1,num2,choice)

