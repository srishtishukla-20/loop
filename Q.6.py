# 1.Perfect Number
# 2.Factorial Number
# 3.Any Armstrong number
# 4.Strong Number
# 5.Happy Number
# 6.Magic Number
# 7.Harshad Number
num = int(input("Enter the number: ")) 
sum = 0 
a= num 
while (a> 0): 
    b= a% 10 
    sum=sum+ b** 3 
    a=a//10
if (num == sum): 
    print("Armstrong number") 
else: 
    print("Not an Armstrong number")
#armstrong number without using length
num = int(input("Enter a number"))
sum = 0
i= num
order=len(str(num))
while i> 0:
   digit = i% 10
   sum = sum+digit**order
   i=i// 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
#armstrong using length
num = int(input("Enter a number"))
sum = 0
i= num
while i>0:
   digit = i% 10
   sum = sum+digit**3
   i=i// 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
# armstrong number without using length from 100 to 500
n =int(input("Enter any number: "))
sum=0
i=1
while i<n:
	if n%i==0:
		sum = sum + i
	i=i+1
if (sum == n):
 	print(n," is a Perfect number!")
else:
  print(n," is not a Perfect number!")
#perfect number
num= int(input('enter no.'))
sum= 0
i= num
while i>0:
	digit= i%10
	sum= sum+digit
	i= i//10
if num%sum==0:
	print(num,'it is harshad no.')
else:
	print(num,'it is not harshad no.')
# harshad Number
n=int(input("enter number"))
a=n
sum=0
while n>0:
	i=1
	f=1
	b=n%10
	while i<=b:
		f=f*i
		i=i+1
	sum=sum+f
	n=n//10
if a==sum:
		print("strong num")
else:
		print("not strong num")
#strong number
n=int(input("enter number"))
i=1
a=1
while i<=n:
	a=a*i
	i=i+1
print(a)
#Factorial NUmber