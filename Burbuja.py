def burbuja(lista):
    n = len(lista)
    for i in range(n):
        inter = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                inter = True
        if not inter:
            break
    return lista


lista = [64, 34, 25, 12, 22, 11, 90]
lista_o = burbuja(lista)
print("La lista ordenada es:", lista_o)
