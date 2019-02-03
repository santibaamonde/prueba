
operacion_elegida = input("Que operacion quieres realizar? (multiplicar / dividir / sumar / restar): ")

print("A continuacion dime los numeros con los que deseas operar")

primer_numero = int(input("Primer numero: "))
segundo_numero = int(input("Segundo numero: "))

if operacion_elegida == "multiplicar":
    resultado = primer_numero * segundo_numero
    print ("El resultado de la multiplicacion es: {}".format(resultado))

elif operacion_elegida == "dividir":
    resultado = primer_numero / segundo_numero
    print ("El resultado de la division es: {}".format(resultado))

elif operacion_elegida == "sumar":
    resultado = primer_numero + segundo_numero
    print("El resultado de la suma es: {}".format(resultado))

elif operacion_elegida == "restar":
    resultado = primer_numero - segundo_numero
    print("El resultado de la resta es: {}".format(resultado))


