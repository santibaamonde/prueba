"""
Crear un programa que encuentre el numero más grande de una lista (sin usar la función max).
"""

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,20,15,30,60,70]
numero_mas_grande = lista[0]

for numero in lista:
    if numero > numero_mas_grande:
        numero_mas_grande = numero

print("El número más grande de la lista es {}".format(numero_mas_grande))

