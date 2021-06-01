i= 0
while i<=4:
	j= 1
	while j<=5:
		print(j, end= ' ')
		j= j+1
	i= i+1
	print()
# square pattern from 1,2,3,4,5
i= 5
while i>=1:
	j= 5
	while j>=1:
		print(i,end= ' ')
		j= j-1
	print()
	i= i-1
# square pattern using decrement
i= 1
while i<=5:
	j= 1
	while j<=i:
		print(i,end= ' ')
		j= j+1
	print()
	i= i+1
# pattern triangle from left
i=1
while i<=5:
	j=5
	while j>=i:
		print(i,end=" ")
		j=j-1
	i=i+1
	print()
#pattern from left from 1
i=1
while i<=5:
	j=1
	while j<=i:
		print(j,end=" ")
		j=j+1
	i=i+1
	print()
#pattern 
i=5
while i>=0:
	j=1
	while j<=i:
		print(j,end=" ")
		j=j+1
	i=i-1
	print()
#pattern from 12345
i=5
while i>=1:
	j=1
	while j<=i:
		print(i,end=" ")
		j=j+1
	i=i-1
	print()
#pattern from 55555
i=1
while i<=5:
	j=5
	while j>=i:
		print(j,end=" ")
		j=j-1
	i=i+1
	print()
# 54321 pattern
i= 1
while i<=15:
	if i%5==0:
		print(i,end= ' \n')
	else:
		print(i,end= ' ')
	i= i+1
#op:1 2 3 4 5 
#6 7 8 9 10 
#11 12 13 14 15
i= 1
while i<=5:
	j= 1
	while j<=i:
		print()
		print(j,end=  '   ')
		j= j+1
	print()
	i= i+1
#pattern
i= 1
while i<=5:
	j= 1
	while j<=i:
		print()
		print(i,end=  '   ')
		j= j+1
	print()
	i= i+1
#pattern in seperate line
i=1
while i<=5:
	j=5
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=1
	while s<=i:
		print(s,end=" ")
		s=s+1
	i=i+1
	print()
#triangle from right
i=5
while i>=1:
	j=i
	while j<=5:
		print(" ",end=" ")
		j=j+1
	s=1
	while s<=i:
		print(i,end=" ")
		s=s+1
	i=i-1
	print()
#triangle from right reverse
i=5
while i>=1:
	j=i
	while j<=5:
		print(" ",end=" ")
		j=j+1
	s=1
	while s<=i:
		print(s,end=" ")
		s=s+1
	i=i-1
	print()
# triangle from right 12345
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
        print(row, end='')
        stars -= 1

    print()
	#pyramid 
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
        print(stars, end='')
        stars -= 1

    print()
i=0
j=12
while j<=24:
	k=i
	while k<=j:
		print(k,end=" ")
		k=k+4
	print()
	i=i+4
	j=j+4
	"""0 4 8 12 
4 8 12 16 
8 12 16 20 
12 16 20 24"""
i=1
x=5
while x>=1:
	y=x
	while y>=1:
		print(" ",end=" ")
		y=y-1
	x=x-1
	z=i
	while z>=1:
		print(z,end=" ")
		z=z-1
	i=i+2
	print()
#pattern
m=1
i=5
while i<=25:
	j=i
	while j>=m:
		print(j,end = " ")
		j=j-1
	print()
	i=i+5
	m=m+5
#spiral reverse
m=5
i=1
while i<=25:
	j=i
	while j<=m:
		print(j,end = " ")
		j=j+1
	print()
	i=i+5
	m=m+5
#spiral
i=1
while i<=5:
    print(str(i)*i)
    i=i+1
#pattern in one loop



