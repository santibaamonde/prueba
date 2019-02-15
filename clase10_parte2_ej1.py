
# Crear un programa que cambie todas las ‘A’ o ‘a’ por la string ‘VACA’ de una string introducida por el usuario.

string_usuario = input("Introduce la frase que quieras: ")

string_modificada_1 = string_usuario.replace("A", "VACA")
string_modificada_final = string_modificada_1.replace("a", "VACA")

print(string_modificada_final)