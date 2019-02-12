
# Crea un programa que calcule la media de los elementos de la lista de números introducida por el usuario (media = suma de todos los numeros / numero de numeros )

lista_usuario = []
numero_del_usuario = input("Dime un número para comenzar así tu lista: ")

while numero_del_usuario != "FIN":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Eso no es un número, dime un número: ")
    lista_usuario.append(int(numero_del_usuario))
    numero_del_usuario = input("Dime un número para continuar o escribe FIN para terminar: ")

print("Tu lista es {}".format(lista_usuario))

indice = 0
suma_lista = 0

while len(lista_usuario) > indice:
    suma_lista += int(lista_usuario[indice])
    indice += 1

print("La suma de los números de tu lista es {}".format(suma_lista))

media_lista = suma_lista / len(lista_usuario)

print("La media artimética de los números de tu lista es {}".format(media_lista))
