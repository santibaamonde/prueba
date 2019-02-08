
# Crea un programa que muestre por pantalla la tabla de multiplicar de un número introducido por el usuario, pero invertida, comenzando desde el 10.

numero_tabla = int(input("De que número quieres la tabla de multiplicar invertida?: "))

indice = 9

lista_multiplos = range(1,11)

while indice == int(lista_multiplos[indice]):
        print("{} x {} = {}".format(numero_tabla, lista_multiplos[indice], numero_tabla * lista_multiplos[indice]))
        indice -= 1


