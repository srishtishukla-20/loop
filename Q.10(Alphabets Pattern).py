i=65
while i<=69:
	j=65
	while j<=69:
		print(chr(i),end=" ")
		j=j+1
	print()
	i=i+1
#Pattern of ABCD in square form
i=65
while i<=69:
	j=65
	while j<=i:
		print(chr(j),end=" ")
		j=j+1
	i=i+1
	print()
# pattern of alphabets
i=65
while i<=69:
	j=69
	while j>=i:
		print(chr(i),end=" ")
		j=j-1
	i=i+1
	print()
# pattern from AAAAA
i=65
while i<=69:
	j=69
	while j>=i:
		print(chr(j),end=" ")
		j=j-1
	i=i+1
	print()
# EDCBA reverse pattern
i=69
while i>=65:
	j=65
	while j<=i:
		print(chr(j),end=" ")
		j=j+1
	i=i-1
	print()
# ABCDE front pattern
i=69
while i>=65:
	j=65
	while j<=i:
		print(chr(i),end=" ")
		j=j+1
	i=i-1
	print()
# EEEEE reverse pattern
i=1
while i<=5:
	j=5
	while j>=i:
		print(" ",end=" ")
		j=j-1
	s=1
	while s<=i:
		print(chr(i+64),end=" ")
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
		print(chr(64+i),end=" ")
		s=s+1
	i=i-1
	print()
#pattern
i=5
while i>=1:
	j=i
	while j<=5:
		print(" ",end=" ")
		j=j+1
	s=1
	while s<=i:
		print(chr(64+s),end=" ")
		s=s+1
	i=i-1
	print()

