a, b, c = map(int, input().split())

numeros_originais = [a, b, c]
numeros_ordenados = sorted(numeros_originais)

for num in numeros_ordenados:
    print(num)

print()

for num in numeros_originais:
    print(num) 