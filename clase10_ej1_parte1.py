
# Dada una lista de strings, devolver una lista con el largo de cada string.

lista_strings = ["Hola", "Adios", "Soy", "Patata"]
lista_largos = []

for palabra in lista_strings:
    lista_largos.append(len(palabra))

print(lista_largos)