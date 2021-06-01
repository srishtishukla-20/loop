#Print multiplication table of 24, 50 and 29 using loop.

i=1
while i<=10:
	print(i*24)
	i=i+1
	
	
i=1
while i<=240:
	if i%24==0:
		print(i)
	i=i+1
	
	
i=1
while i<=10:
	print(24,"x",i,"=",i*24)
	i=i+1
	
	
i=1
while i<=240:
	print(i+23)
	i=i+24
	
	
i=0
while i<=240:
	if i!=0:
		print(i)
	i=i+24
	
	
i=240
k=9
while k>=0:
	print(i-(24*k))
	k=k-1