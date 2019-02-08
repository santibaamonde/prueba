
# Modifica el programa de la tabla de multiplicar para que sólo muestre los resultados cuando son múltiplos de 2

numero_tabla = int(input("De que número quieres la tabla de multiplicar?: "))

for multiplo in range (1,11):
    if multiplo%2 == 0:
        print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))


