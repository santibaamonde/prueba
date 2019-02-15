"""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:
input = [1, 10, 70, 30, 50, 55]
multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 60, 55]
multiplos_siete = [70]
"""

lista_usuario = []
input_usuario = input("Dime un número para añadir a la lista o escribe FIN para terminar: ")

while input_usuario != "FIN":
    lista_usuario.append(int(input_usuario))
    input_usuario = input("Dime un número para añadir a la lista o escribe FIN para terminar: ")

print("Tu lista es {}".format(lista_usuario))

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for numero in lista_usuario:
    if numero % 2 == 0:
        multiplos_dos.append(numero)
    if numero % 3 == 0:
        multiplos_tres.append(numero)
    if numero % 5 == 0:
        multiplos_cinco.append(numero)
    if numero % 7 == 0:
        multiplos_siete.append(numero)

print("Los múltiplos de dos son: {}".format(multiplos_dos))
print("Los múltiplos de dos tres: {}".format(multiplos_tres))
print("Los múltiplos de dos cinco: {}".format(multiplos_cinco))
print("Los múltiplos de dos siete: {}".format(multiplos_siete))




