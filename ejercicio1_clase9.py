
#Crea un programa que sea capaz de contar espacios, puntos y comas en una string introducida por el usuario.

frase_del_usuario = input("Introduce una frase cualquiera: ")

lista_vocales = ["a","e", "i", "o","u"]
espacio = " "

n_vocales = 0
n_consonantes = 0
n_espacios = 0

for caracter in frase_del_usuario:
    if caracter in lista_vocales:
        n_vocales += 1
    elif caracter == espacio:
        n_espacios += 1
    else:
        n_consonantes += 1

print("El número de vocales es {}".format(n_vocales))
print("El número de consonantes es {}".format(n_consonantes))
print("El número de espacios es {}".format(n_espacios))

