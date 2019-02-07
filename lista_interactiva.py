
mi_lista = []
inmput_usuario = ""
inmput_usuario = input("¿Qué necesitas comprar? (escribe FIN para salir): ")

while inmput_usuario != "FIN":
    mi_lista.append(inmput_usuario)
    inmput_usuario = input("¿Qué necesitas comprar? (escribe FIN para salir): ")

largo_lista = len(mi_lista)
indice_actual = 0

while indice_actual < largo_lista:
    print("Tengo que comprar {}".format(mi_lista[indice_actual]))
    indice_actual += 1

print("Esta es la lista de la compra")
