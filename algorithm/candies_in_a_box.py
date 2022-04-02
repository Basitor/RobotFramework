x = 9
y = 5
z = 4

a = x + z - y
b = y + z - x
c = x + y - z

if a * b * c <= 0:
    print("Impossible")
else:
    print(a // 2, 0, a // 2)
    print(0, b // 2, b // 2)
    print(c // 2, c // 2, 0)
