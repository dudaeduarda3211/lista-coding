n = int(input())

resposta = []

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        resposta.append("FizzBuzz")
    elif i % 3 == 0:
        resposta.append("Fizz")
    elif i % 5 == 0:
        resposta.append("Buzz")
    else:
        resposta.append(str(i))

print(resposta) 