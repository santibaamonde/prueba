
#Crea un programa que sea capaz de contar la cantidad de letras mayúsculas en una string introducida por el usuario.

frase_del_usuario = input("Escribe la frase que quieras: ")

n_mayusculas = 0
espacio = " "

for caracter in frase_del_usuario:
    if caracter == espacio:
        n_mayusculas + 0
    elif caracter == caracter.upper():
        n_mayusculas += 1

print("El número de mayúsculas es {}".format(n_mayusculas))
