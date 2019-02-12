
# Crea un programa que encuentre el número más pequeño de una serie de números introducidos por el usuario.

numeros_usario = []
numero_del_usuario = input("Dime un número para crear una serie o escribe FIN para terminar: ")

while numero_del_usuario != "FIN":
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Eso no es un número, dime un número: ")
    numeros_usario.append(int(numero_del_usuario))
    numero_del_usuario = input("Dime un número para crear una serie o escribe FIN para terminar: ")

print("Serie creada! Tu serie es: {}".format(numeros_usario))

numero_pequeno = numeros_usario[0]

for numero in numeros_usario:
    if numero < numero_pequeno:
        numero_pequeno = numero

print("El número más pequeño de la serie es {}".format(numero_pequeno))
