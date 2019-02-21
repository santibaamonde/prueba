"""
Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).
numero_en_rango(10, 1, 100) # Devuelve True
numero_en_rango(101, 1, 100) # Devuelve False
"""

def numero_en_rango (numero,rango_min,rango_max):

    if numero > rango_min and numero < rango_max:
        numero_en_rango = True
    else:
        numero_en_rango = False
    return numero_en_rango

print(numero_en_rango(2,1,8))
print(numero_en_rango(3,-13,123123))
print(numero_en_rango(0,43,100))
