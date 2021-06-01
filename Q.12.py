n= int(input(" Please Enter the Maximum Value : "))
sum= 0
i=2
while i<=n:
    if i% 2 == 0:
        print(i)
        sum = sum + i
    i=i+1
print( sum)
#sum of even from user
n= int(input(" Please Enter the Maximum Value : "))
sum= 0
i=1
while i<=n:
    if i% 2 != 0:
        print(i)
        sum = sum + i
    i=i+1
print( sum)
#sum of odd numbers