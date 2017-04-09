lista = [30,28,50,35,80,100,10,8,63,26,98,5]
tamanho_lista = len(lista)

#bubble sort
for i in range(tamanho_lista):
    troca = False
    for j in range(1,tamanho_lista - i):
        if lista[j] < lista[j - 1]:
           lista[j], lista[j - 1] = lista[j - 1], lista[j]
           troca = True
    if not troca:
        break
print ("A lista ordenada é: ")
print(lista)
