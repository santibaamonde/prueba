
# Crear un programa que cambia las vocales por su numero de aparición. Por ejemplo la string “aurora boreal” se
# convertiría en “12r3r4 b5r67l”

string_usuario = "Introduce la frase que quieras"
vocales = ["a","e","i","o","u"]
valores_a_sustituir = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

for letra in string_usuario:
    if letra in vocales:
        string_usuario_2 = string_usuario.replace("letra", "1")

print(string_usuario_2)
