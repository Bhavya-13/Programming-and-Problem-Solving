d = int(input())
m = int(input())
y = int(input())

valid = True

if m<1 and m>12:
	valid = False
elif m in [1,3,5,7,8,10,12]:
	maxdays = 31

elif m in [4,6,9,11]:
	maxdays = 30

elif m == 2:
	if(y%400 == 0) or (y%4==0 and y%100!=0):
		maxdays = 29
	else:
		maxdays = 28
	
if valid:
	if d<1 or d>maxdays:
		valid = False

if valid:
	d += 1

	if d> maxdays:
		d=1
		m += 1

		if m > 12:
			m=1
			y+=1

	print(f"{d:02d}-{m:02d}-{y}")

else:
	print("Invalid Date")
