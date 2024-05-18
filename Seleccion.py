def selec(lista):
    for i in range(len(lista)):
        indice_min = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_min]:
                indice_min = j
        lista[i], lista[indice_min] = lista[indice_min], lista[i]
    return lista

lista = [64, 25, 12, 22, 11]
lista_o = selec(lista)
print("La lista ordenada es:", lista_o)
