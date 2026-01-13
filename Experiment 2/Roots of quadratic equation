# Write your code here...

import math

a, b, c = map(float, input("Enter the 3 cofficients").split())
d = (b*b) - (4*a*c)

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print(f"root1 = {r1:.2f}")
    print(f"root2 = {r2:.2f}")

elif d == 0:
    r = (-b + math.sqrt(d)) / (2*a)
    print(f"root1 = root2 = {r:.2f}")

else:
    real = -b / (2*a)
    img = math.sqrt(-d) / (2*a)
    print(f"root1 = {real:.2f}+{img:.2f}i")
    print(f"root2 = {real:.2f}-{img:.2f}i")
