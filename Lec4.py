
for i in range(1,101):
    for j in range(1,101):
        if(i**2-2*(j**2))==1:
            print(i,j)
    

# WRITE A PROGRAM THAT GIVES AMOUNT OF CHANGE FOR ONE DOLLAR AND IT PRINTS OUT DENOMINATION THAT WILL BE NEEDED FOR THE CHANGE.
dollar=float(input("Enter the amount "))
temp=dollar
quarter=25
dime=10
nickel=5
penny=1
if temp<1:
    temp=temp*100
    Q=int(temp/25)
    temp=(temp-(Q*25))
    D=int(temp/10)
    temp=(temp-(D*10))
    N=int(temp/5)
    temp=(temp-(N*5))
    P=int(temp)
    print("Number of quarter is",Q,"\nNumber of dime is",D,"\nNumber of nickel is",N,"\Number of penny is",P)

        

""""Suppose you put 1 rupees in bank on 1st day(monday) and every day from next day(tuesday to sunday) 
you put in one rupees more than the day before and on every subsequence monday you will put one 
rupees more than the previous monday if you have number n find the total amount of money you have
in the bank at the end of nth day."""

days=int(input("Enter numbers of days "))
sum=0
monday=1
sunday=7
weeks=days//7
days%=7
for i in range(weeks):
    for j in range(monday,sunday+1):
        sum=sum+j
    monday=monday+1
    sunday=sunday+1
for i in range(days):
    sum=sum+monday
    monday=monday+1
print(sum)

"""ask user for 10 test score 
1)print out the avg of the score
2)print out the second largest score
3)if any score is greater than 100 then after all scores have been enter print a msg warning that a value over 100 has been enter 
4)drop the lowest 2 score and print the avg of rest of them"""
sum=0
count=0
count1=0
for i in range(1,11):
    score=int(input("Enter score "))
    if(score>100):
            count=count+1
    else:
        sum=sum+score
        if(score>count1):
            secondlargest=count1
            count1=score
            count2=count1
        if(score<count2):
            lowest=count2
            count2=score
avg=(sum)/10
print("average is",avg)
print("second largest is",secondlargest)
print("you entered a",count,"score greater than 100")
print("lowest is",lowest,count2)

