def mezcla(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        mitad_izq = lista[:mitad]
        mitad_dere = lista[mitad:]

        mezcla(mitad_izq)
        mezcla(mitad_dere)

        i = j = k = 0

        while i < len(mitad_izq) and j < len(mitad_dere):
            if mitad_izq[i] < mitad_dere[j]:
                lista[k] = mitad_izq[i]
                i += 1
            else:
                lista[k] = mitad_dere[j]
                j += 1
            k += 1

        while i < len(mitad_izq):
            lista[k] = mitad_izq[i]
            i += 1
            k += 1

        while j < len(mitad_dere):
            lista[k] = mitad_dere[j]
            j += 1
            k += 1
    return lista

lista = [12, 11, 13, 5, 6, 7]
lista_o = mezcla(lista)
print("La lista ordenada es:", lista_o)