"""Starting with any positive integer replace the number by sum of the sqaure of its digit
and repeat the process until the number is euqal to 1 or it loops endlessly which does
not include 1.
For eg: 7--->49--->97---->130---->10---->1 """
def CheckHappyNumber(num):
    square=0
    flag=0
    num2=num
    while num!=1 and num!=4:
        sum=0
        while(num>0):
            k=num%10
            square=k**2
            sum=sum+square
            num=num//10
        num=sum
        if num==1:
                flag=1
    if flag==1:
        print(num2,"is happy number")
    else:
        print(num2,"is not happy number")
    
for i in range(1,101):
    CheckHappyNumber(i)

# 1729=1^3+12^3+9^3+10^3 ramanujan number
for i in range(1,21):
    for j in range(1,21):
        if i==j:
            continue
        else:
            num=i**3+j**3
        for k in range(1,21):
            for l in range(1,21):
                if k==i or k==j or l==i or l==j:
                    continue
                else:
                    num2=k**3+l**3
                if num==num2:
                    print(num)
              
        

# Pascal Traingle
def solve(n):
    for i in range(n+1):
        for j in range(n-i):
            print(" ",end="")
        c=1
        for j in range(1,i+1):
            print(c," ",sep="",end="")
            c=c*(i-j)//j
        print()
n=5
solve(n)

""""(QB-191) WAP that enters a single digit integer number and produce all possible 6 digit combination for 
which product of their digit is equal to the enter number"""
num=int(input("Enter number"))
for i in range(1,10):
    for j in range(1,10):
         for k in range(1,10):
            for l in range(1,10):
                for m in range(1,10):
                    for n in range(1,10):
                        if(i*j*k*l*m*n)==num:
                            print(i,j,k,l,m,n,sep="")
                        


"""Newton method:you first guess what squareroot might be and then how close your guess.
Suppose you want the root of and guess is a current guess ans this guess can be improved by the formula
guess=0.5(guess+x/guess)
this guess as the next guess
The program should promt the user to find square and no. of times to improve the guess"""
x=int(input("Enter number"))
guess=x/2
for i in range(1,11):
    guess=0.5*(guess+(x/guess))
print(guess)
    