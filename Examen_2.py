def espiral(esp):
    matriz = [[0] * esp for _ in range(esp)]
    mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    mov_actual = 0
    fila, columna = 0, 0
    for i in range(1, esp * esp + 1):
        matriz[fila][columna] = i
        sig_fila, sig_columna = fila + mov[mov_actual][0], columna + mov[mov_actual][1]
        if 0 <= sig_fila < esp and 0 <= sig_columna < esp and matriz[sig_fila][sig_columna] == 0:
            fila, columna = sig_fila, sig_columna
        else:
            mov_actual = (mov_actual + 1) % 4
            fila, columna = fila + mov[mov_actual][0], columna + mov[mov_actual][1]
    for fila in matriz:
        print(" ".join("{:3}".format(numero) for numero in fila))
def main():
    while True:
        print("Presiona 0 para salir")
        n = int(input("Ingrese el número del cuadrado: "))
        if n == 0:
            print("Adio")
            break
        try:
            espiral(esp)
        except Exception as err:
            print("No se pudo completar la impresión de la espiral. Error:", err)

if __name__ == "__main__":
    main()