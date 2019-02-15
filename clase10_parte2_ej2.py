
# Crear un programa que le repita al usuariotodo lo que dice pero con todas las vocales cambiadas por i.

string_usuario = input("Introduce la frase que quieras: ")

string_modificada_1 = string_usuario.replace("a", "i")
string_modificada_2 = string_modificada_1.replace("e", "i")
string_modificada_3 = string_modificada_2.replace("o", "i")
string_modificada_final = string_modificada_3.replace("u", "i")

print(string_modificada_final)




