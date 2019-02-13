
# Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.

lista_mixta = ["hola", 0, float, 5, "adios", "me", 78, 100, "h"]

lista_strings = []
lista_enteros = []

for elemento in lista_mixta:
    if type(elemento) == str:
        lista_strings.append(elemento)
    elif type(elemento) == int:
        lista_enteros.append(elemento)

print(lista_strings)
print(lista_enteros)
