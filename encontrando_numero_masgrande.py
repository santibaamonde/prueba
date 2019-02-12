
# Pregunta al usuario una serie de 10 números, determina cuál es el más grande de los diez.

numeros_usario = []
numero_del_usuario = ""

while len(numeros_usario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print ("¡Número añadido!")

numero_grande = numeros_usario[0]

for numero in numeros_usario:
    if numero > numero_grande:
        numero_grande = numero

print("El número más grande es {}".format(numero_grande))

