a=int(input("enter any number"))
i=0
while a>0:
	r=a%10
	i=(i*10)+r
	a=a//10
while i>0:
	c=i%10
	d=c**2
	i=i//10
	print(d,end=" ")
	#squares of reverse of any numbers
i=5
while i>=0:
	print(i)
	i=i-1
i=1
while i<=5:
	print(i)
	i=i+1