
numero_adivinar = int(input("Dime un numero que quieras que otro trate de adinivar: "))
numero_adivinador = int(input("Intenta adivinar el numero que ha pensado la otra persona: "))

while numero_adivinar != numero_adivinador:
    numero_adivinador = int(input("Has fallado, prueba otro numero: "))

print("Has ganado")
