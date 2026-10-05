mensagem = input()
crib = input()

tam_msg = len(mensagem)
tam_crib = len(crib)

posicoes_validas = 0

for i in range(tam_msg - tam_crib + 1):
    valido = True
    for j in range(tam_crib):
        if mensagem[i + j] == crib[j]:
            valido = False
            break
            
    if valido:
        posicoes_validas += 1

print(posicoes_validas) 