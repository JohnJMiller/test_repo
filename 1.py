#Euler Question 1
n=999
sum = 0
while n>0:
    if n%3 == 0:
        sum=sum + n
        n=n-1
    elif n%5 == 0:
        sum=sum + n
        n=n-1
    else:
        sum = sum
        n=n-1
print sum