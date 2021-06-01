a= 10
i= 1
while i<=a:
	b=6
	guess= int(input('enter your guess'))
	i= i+1
	if guess>b:
		print('guess bada hai')
	elif guess<b:
		print('guess chota hai')
	else:
		print("barabar hai")
		break
    #guess the number
i=1
while i<=10:
	num=int(input("enter number "))
	i=i+1
print(num)
#take user input and ask for ten numbers
i=1
while i<=5:
	print("*" *i)
	i=i+1
#print * pattern
i=40
while i<=755:
	if i%100==57:
		print(i)
	if i%100==75:
		print(i)
	i=i+1
#print 57 and 75 in the end
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
while(count <= n):
  print(sum)
  count += 1
  a = b
  b = sum
  sum = a + b

