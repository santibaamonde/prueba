
# Crea un programa que cuente los elementos de la lista de números introducida por el usuario. Está prohibido utilizar la función len() para resolver el problema.

lista_usuario = []
numero_del_usuario = input("Dime un número para comenzar así tu lista: ")

while numero_del_usuario != "FIN":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Eso no es un número, dime un número: ")
    lista_usuario.append(int(numero_del_usuario))
    numero_del_usuario = input("Dime un número para continuar o escribe FIN para terminar: ")

print("Tu lista es {}".format(lista_usuario))

largo_lista = 0

for numero in lista_usuario:
    if numero != None:
        largo_lista += 1

print("El largo de tu lista es de {}".format(largo_lista))
