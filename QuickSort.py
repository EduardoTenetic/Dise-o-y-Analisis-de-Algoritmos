def rapido(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izq = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    dere = [x for x in lista if x > pivote]
    return rapido(izq) + medio + rapido(dere)


lista = [3, 6, 8, 10, 1, 2, 1]
lista_o = rapido(lista)
print("La lista ordenada es:", lista_o)
