N = int(input())

fibo = []
a, b = 0, 1

for _ in range(N):
    fibo.append(str(a))
    a, b = b, a + b

print(" ".join(fibo)) 