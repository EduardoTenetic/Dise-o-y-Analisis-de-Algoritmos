def heap(lista, n, i):
    mayor = i
    izq = 2 * i + 1
    dere = 2 * i + 2

    if izq < n and lista[i] < lista[izq]:
        mayor = izq

    if dere < n and lista[mayor] < lista[dere]:
        mayor = dere

    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heap(lista, n, mayor)

def monticulo(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heap(lista, n, i)

    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heap(lista, i, 0)

    return lista

lista = [12, 11, 13, 5, 6, 7]
lista_o = monticulo(lista)
print("La lista ordenada es:", lista_o)
