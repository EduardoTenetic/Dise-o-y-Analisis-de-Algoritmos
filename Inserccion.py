def inser(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

lista = [12, 11, 13, 5, 6]
lista_o = inser(lista)
print("La lista ordenada es:", lista_o)
