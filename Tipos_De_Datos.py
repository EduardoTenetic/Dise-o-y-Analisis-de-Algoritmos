x = 22
#Establece el valor de la variable
print ("x      = {: >6b}". format ( x ) )
#Imprime el valor de la variable en binario con 6 digitos.
print ("x & 4  = {: >3d} = {: >6b}". format ( x & 4 , x & 4) )
#Imprime el resultado de la operación AND entre x y 4 y luego imprime el mismo en binario con 6 digitos a la derecha
print ("x | 1  = {: >3d} = {: >6b}". format ( x | 1 , x | 1) )
#Imprime el resultado de la operación OR entre x y 1 y luego imprime el mismo resultado en formato binario con 6 digitos a la derecha.
print ("x ^ 4  = {: >3d} = {: >6b}". format ( x ^ 4 , x ^ 4) )
# Imprime el resultado de la operación XOR entre x y 4 luego imprime el mismo resultado en formato binario con 6 digitos a la derecha.
print ("x     = {: >3d} = {: >6b}". format ( x , ~ x ) )
# Imprime el valor de x y el complemento a uno de x en formato binario con 6 digitos a la derecha.
print ("x << 1 = {: >3d} = {: >6b}". format ( x << 1 , x << 1) )
# Imprime el resultado de desplazar los bits de x a la izquierda en 1 posicion y luego imprime el mismo resultado en formato binario con  6 dígitos y alineando a la derecha.
print ("x >> 2 = {: >3d} = {: >6b}". format ( x >> 2 , x >> 2) )
#Imprime el resultado de desplazar los bits de x a la derecha en 2 posiciones luego imprime el mismo resultado en formato binario con 6 dígitos y alineando a la derecha.