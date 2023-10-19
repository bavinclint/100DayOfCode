a, b = 0, 1
n = 10
while a <= n:
    print(a)
    a, b = b, a
    a = a + b
