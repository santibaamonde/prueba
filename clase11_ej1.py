"""
Escribe una función que encuentr el número más grande entre 3 números
"""

def mas_grande_tres(numero_uno,numero_dos,numero_tres):
    lista_numeros = []
    lista_numeros.append(numero_uno)
    lista_numeros.append(numero_dos)
    lista_numeros.append(numero_tres)
    numero_mas_grande = max(lista_numeros)

    return numero_mas_grande


print(mas_grande_tres(5,80,9))
print(mas_grande_tres(5,80,765123671892673))
print(mas_grande_tres(-7,0,123))