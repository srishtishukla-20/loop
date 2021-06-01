i=1
count=0
user_num=int(input("enter number"))
while i<=user_num:
	if user_num%i==0:
		count=count+1
	i=i+1
if count==2:
	print("prime number")
else:
	print("not prime")
#prime number from user
a=int(input("enter number "))
i=2
while i<a:
	if a%i==0:
		print(a,"is not a prime number")
		break
	i=i+1
else:
	print(a,"is a prime number ")
#prime number
num= 1
while num<=100:
	   count= 0
	   i= 2
	   while (i<=num//2):
	   	if num%i==0:
	   		count= count+1
	   		break
	   	i= i+1
	   if (count==0 and num!=1):
	   	print(num, end= ' ')
	   num= num+1
	#1 to 100 prime numbers
#Without break 1 to 100 prime no.num= 1
while num<=100:
	   count= 0
	   i= 2
	   while (i<=num//2):
	   	if num%i==0:
	   		count= count+1
	   	i= i+1
	   if (count==0 and num!=1):
	   	print(num)
