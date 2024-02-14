def identificar_cuadrilatero(lados):
    # Verificar si es un cuadrado
    if len(set(lados)) == 1:
        return "Cuadrado"
    # Verificar si es un rectángulo
    elif len(set(lados)) == 2:
        return "Rectángulo"
    # Si no es cuadrado ni rectángulo, es otro tipo de cuadrilátero
    else:
        return "Otro cuadrilátero"

def main():
    while True:
        lados = []
        for i in range(4):
            lado = float(input(f"Ingrese la medida del lado {i+1}: "))
            lados.append(lado)
        
        tipo = identificar_cuadrilatero(lados)
        print("El cuadrilátero ingresado es:", tipo)
        print("Ingrese las medidas de otro cuadrilátero o presione Ctrl+C para salir.\n")

if __name__ == "__main__":
    main()

