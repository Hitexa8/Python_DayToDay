# Fibonnaci Series
# a,b,c are first,second and third term
a=0
b=0
c=1
for i in range(1,21):
    if i==18:
        print("18th number is:",a)
    sum=a+b+c
    a=b
    b=c
    c=a+b
    c=sum

"""Strong number:In number theory a number is strong when the sum of its
individual digits each raise to the factorial power is the number itself."""
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
for i in range(1,501):
    number=i
    tempnumber=number
    sum=0
    while tempnumber>0:
        count=tempnumber%10
        fac=factorial(count)
        sum=sum+fac
        tempnumber=tempnumber//10
    if sum==number:
        print(f"Strong number is {number}")

"""Amicable number:these numbers are the pair of number whose factors and 
accordingly their sum is the other number in the pair.
for eg factor of 220:-1,2,4,5,10,11,20,22,44,55,220(not include 220)and sum of
of factor of 220 is 284 and sum of factors of 284:-1,2,71,142,84 is 220"""
for i in range(1,501):
    sum=0
    sum1=0
    number=i
    for j in range(1,number):
        if(number%j==0):
            sum=sum+j
    number2=sum
    for k in range(1,number2):
        if(number2%k==0):
            sum1=sum1+k
    number3=sum1
    if(number==number3 and number!=number2):
        print(f"Amicable number is {number} and {number2}")
            

"""WAP that computes the net amount of bank account based on a transaction log from console input"""
deposit=500
total=deposit
balance=0
withdraw=0
ans=0
while(ans!=3):
    print("What you have to do: enter (1) for withdraw (2) for deposit (3) for exit")
    ans=int(input("Enter your answer "))
    if ans==1:
        amount=int(input("Enter amount you want to withdraw"))
        if(withdraw<total):
            balance=deposit-amount
        else:
            print("Insufficiant balance")
        print("Your current balance is",balance)
    elif ans==2:
        amount=int(input("Enter amount you want to deposit"))
        balance=deposit+amount
        print("Your current balance is",balance)
    else:
        break
print("Total balance is:",balance)

# Chronic number
for i in range(1,11):
    j=i+1
    print(i*j)

# print the pattern
wh=4
wl=4
pc=wh-1
for x in range(0,wh+1):
    for y in range(0,(wh*wl*2)):
        if(y%(wh*2)==pc):
            print("/",end="")
        elif(y%(wh*2)==wh+x):
            print("\\",end="")
        else:
            print(" ",end="")
    pc-=1
    print()

