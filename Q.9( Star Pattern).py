a= int(input('enter no.'))
row = 0
while(row <a):
    row += 1
    spaces = a - row

    counter = 0
    while(counter < spaces):
        print(" ", end='')
        counter += 1

    stars = 2*row-1
    while(stars > 0):
        print("*", end='')
        stars -= 1

    print()
#Pyramid from user
i= 0
while i<=5:
	j= 0
	while j<=5:
		print('*', end= ' ')
		j= j+1
	i= i+1
	print()
# square pattern...
i=5
while i>=1:
	j=1
	while j<=i:
		print("*",end=" ")
		j=j+1
	i=i-1
	print()
#triangle from left starting from reverse
i=5
while  i>=1:
	print("* "*i)
	i=i-1
#triangle
i=1
while i<=6:
	j=1
	while j<=i:
		print("*",end=" ")
		j=j+1
	print()
	i=i+1
i=1
while i<=5:
	j=5
	while j>=i:
		print("*",end=" ")
		j=j-1
	print()
	i=i+1
#triangle from left
i=1
while i<=6:
	print("* "*i)
	i=i+1
i=5
while i>=0:
	print("* "*i)
	i=i-1
#triangle from  left
i= 5
while i>=1:
	j= 1
	while j<=5:
		print("*"*j,end=  '  ')
		j= j+1
	print()
	i= i-1
#pattern
i=1
while i<=5:
	j=5
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=0
	while s<=j:
		print("*",end=" ")
		s=s+1
	i=i+1
	print()
#space triangle from right
i=1
while i<=5:
	j=5
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=0
	while s<=j:
		print("*  ",end=" ")
		s=s+1
	i=i+1
	print()
#pyramid
i=5
while i>=1:
	j=i
	while j<=5:
		print(" ",end=" ")
		j=j+1
	s=1
	while s<=i:
		print("*",end=" ")
		s=s+1
	i=i-1
	print()
	#Triangle from right reverse
i=1
while i<=4:
	j=1
	while j<=4:
		if (j==1 or j==4 ) or (i==1 or i==4):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		j=j+1
	print()
	i=i+1
#Holow square
i=1
while i<=5:
	j=1
	while j<=5:
		if (j==1 or j==5) or (i==1 or i==5):
			print("*",end=" ")
		else:
			print("#",end=" ")
		j=j+1
	print()
	i=i+1
#Hollow square inside $
r=0
while r<=6:
    c=0
    while c<=4:
        if ((c==0)and(r!=0 and r!=3 and r!=4 and r!=5 and r!=6) or(c==1 or c==2)and(r!=1 and r!=2 and r!=4 and r!=5) or (c==3)and (r!=1 and r!=2 and r!=4 and r!=5) or (c==4)and(r!=0 and r!=1 and r!=2 and r!=3 and r!=6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        c=c+1
    print()
    r=r+1
# Pattern of S
r=0
while r<=5:
	c=0
	while c<=6:
		if ((c==0 or c==4 and r!=0) or (r==0 or r==3) and (c>0 and c<4)):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
# Patten of A
r=1
while r<=7:
	c=0
	while c<=7:
		if ((c==1 or c==6 or r==c ) and (c>0 and c<4) or (r==1 and c==5) or (r==2 and c==4) or c==5):
			print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
#Pattern of M
r=0
while r<5:
	c=0
	while c<=5:
		if ((c==1 or c==5 or r==c ) and  (c>0 and c<4 )  or (c==4)):
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
#Pattern of N
r= 0
while r<=5:
	c= 0
	while c<=3:
		if (c==0 or r==5):
			print('*',end=' ')
		else:
			print(' ',end= ' ')
		c= c+1
	print()
	r= r+1
#Pattern L
r= 0
while r<=5:
	c= 0
	while c<=4:
		if (c==2 or r==0):
			print('*',end=' ')
		else:
			print(' ',end= ' ')
		c= c+1
	print()
	r= r+1
# pattern T
r=0
while r<5:
	c=0
	while c<=4:
		if r==0 or c==2 or r==4:
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		c=c+1
	print()
	r=r+1
# Pattern I
c=0
while c<=4:
	r=0
	while r<=4:
		if r==0 or c==2 or c==0 or c==4:
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		r=r+1
	print()
	c=c+1
# Pattern E
c=0
while c<=4:
	r=0
	while r<=4:
		if r==0 or c==2 or c==0 :
		   print("*",end=" ")
		else:
			print(" ",end=" ")
		r=r+1
	print()
	c=c+1
# Pattern F
i=1
while i<=5:
    print(str(i)*i)
    i=i+1
#pattern in one loop











