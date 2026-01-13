# write your code here...

a = int(input("Enter first Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and a > c:
    big = a

elif b > c and b > a:
    big = b

elif c > a and c > b:
    big = c

print("The biggest number among them is", big)
