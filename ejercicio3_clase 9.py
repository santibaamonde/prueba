
#Crea un programa que muestre por pantalla una lista de todas las vocales que aparecen en una string introducida por el usuario

frase_del_usuario = input("Introduce una frase cualquiera: ")

lista_vocales = ["a","e","i","o","u"]
lista_vocales_frase_usuario = []

for caracter in frase_del_usuario:
    if caracter in lista_vocales:
        lista_vocales_frase_usuario.append(caracter)

print("Vocales = {}".format(lista_vocales_frase_usuario))

