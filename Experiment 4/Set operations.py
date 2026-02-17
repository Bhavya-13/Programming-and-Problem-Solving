# Type Content here...
a = set(map(int, input("Set A: ").split()))
b = set(map(int, input("Set B: ").split()))

u = a | b
print(f"Union: {u}")

i = a & b
print(f"Intersection: {i}")

d = a - b
print(f"Difference: {d}")
