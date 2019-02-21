"""
Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.

devolver_pares([1, 2, 3, 4, 5, 6])
[2, 4, 6]
"""

def devolver_pares(lista_numeros):
    lista_numeros = []
    lista_pares = []
    for item in lista_numeros:
        if item % 2 == 0:
            lista_pares.append(item)

    return lista_pares

print(devolver_pares(1,2,3,4,5,6,7,8))
