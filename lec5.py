# Write a program to reduce the number into fraction
numerator=int(input("Enter numerator "))
denominator=int(input("Enter denominator "))
def findfraction(numerator,denominator):
    i=1
    while i<=numerator and i<=denominator:
        if(numerator%i==0 and denominator%i==0):
            divide=i
        i=i+1
    new_numerator=numerator//divide
    new_denominator=denominator//divide
    print(f"Ans of {numerator}/{denominator} in fraction is {new_numerator}/{new_denominator}.")
findfraction(numerator,denominator)

# Disarium number-A number is disarium if the sum of the digit raise to the respective position is the number.
num=int(input("Enter number to check "))
def check_disarium(num):
    temp=num
    temp1=num
    sum=0
    count=0
    while temp>0:
        count=count+1
        temp=temp//10
    while temp1>0:
        r=temp1%10
        sum=sum+(r**count)
        count=count-1
        temp1=temp1//10
    if(sum==num):
        print("Number is disarium")
    else:
        print("Number is not disarium")
check_disarium(num)

# Write a program that computes the value of a+aa+aaa+aaaa
num=int(input("Enter number between 1 to 9"))
sum=0
sum=num+(num*10)+num+(num*100)+(num*10)+num+(num*1000)+(num*100)+(num*10)+num
print(sum)

""" A collazt sequence is generated by repeated applying following rules to integer and then to each resulting integer in turn.
1)if even divide by 2
2)if odd multiply by 3 and add 1
this algo is tested on found to always reach 1 for +ve int"""
# Create a function that takes tow +ve integer a and b and returns the number a if it took fewer steps to reach 1 than b.
# a and b are two numbers
a=int(input("Enter number 1 "))
b=int(input("Enter number 2 "))
counter1=0
counter2=0
def collaztsequence(a,b):
    while a>1:
        if a%2==0:
            ans=a//2
            counter1+=1
        else:
            a=a*3+1
            counter1+=1
    while b>1:
        if b%2==0:
            ans1=b//2
            counter2+=1
        else:
            a=a*3+1
            counter2+=1
    if(a>b):
        print("print",a)
    else:
        print("print",b)

# Sn = a/(1-r) for infinite series
a=1
r=1/2
sum=int(a/(1-r))
print(sum)

# Harshad number is a positive number that is dvisible by the sum of its digit
def check_harshadnumber(num):
    temp=num
    sum=0
    while temp>0:
            r=temp%10
            sum=sum+r
            temp=temp//10
    if(num%sum==0):
        print(num,"Number is harshad number")
    else:
        print(num,"Number is not harshad number")
check_harshadnumber(18)

"""WAP THAT ASKS THE USERS FOR AN HOUR BETWEEN 1 AND 12.
ASK TO ENTER AM AND PM AND HOW MANY HOURS INTO THE FUTURE THEY WANT TO GO."""
current_time=int(input("Enter hours "))
am_or_pm=input("Enter AM OR PM of time that you enter ")
hours_ahead=int(input("How many hours ahead "))
totaltime=current_time+hours_ahead
if(totaltime>12):
    totaltime-=12
    am_or_pm="pm"
if totaltime>12 and am_or_pm=="pm":
        totaltime-=12
        am_or_pm="am"
print(totaltime,am_or_pm)

""" An integer is called square free if it is not divisible by any perfect square other than 1.
For instance 42 is square free number because 1,3,2,6,7 and non of them is perfect square but 45 is not square free.
Write a program to take input from user and check if it is square free or not"""