print("Welcome to Navgurukul Council members")
print("There are 10 council members")
Post=input( " Enter Post:Facility incharge,Disco,FM,,Outreach,Kitchen Co-ordinator,Cultural Incharge=")
if Post=="Facility incharge":
	print("Shweta and Shanti")
elif Post=="Disco":
	print("Bharti and Amrita")
elif Post=="FM":
	print("Neha")
elif Post=="Outreach":
	print("Rubina")
elif Post=="Kitchen Co-ordinator":
	print("Reena and Anzum")
elif Post=="Cultural Incharge":
	print("Alisha")
else:
	print("invalid post")
#print names of girls who are in post
i = 1
sum= 0
while(i <= 140):
    sum= sum+i
    if(sum% 3 == 0):
        print(sum)
    i= i+1
#Debug question no.2
i=1
sum=0
while i<=11:
	a=int(input("enter number "))
	sum=sum+a
	i=i+1
	avg=sum/11
if avg%5==0:
	print("divisible by 5")
else:
	print("not divisible")
#DIVISIBLE AND SUM OF 5
n= int(input('enter no.'))
i= 2
while i<=n:
	print(i**3)
	i= i+1
#Any number of cubes
num=int(input("enter the number"))
i = 0
while i<=10:
    if(num > 0):
        print("it is positive")
    elif(num < 0):
        print("it is negetive")
    else :
        print("zero")
    i = i + 1
    break
#Debug - 4
