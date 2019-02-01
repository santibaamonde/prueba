user_number = int(input("Adivina un numero del 1 al 10: "))
number_to_guess = 2

if number_to_guess == user_number:
    print("A la primera")

else:
    user_number_1 = int(input("Has fallado, prueba con otro numero: "))
    if user_number_1 == number_to_guess:
        print("Has ganado")
    else:
        user_number_2 = int(input("Prueba con otro numero: "))
        if user_number_2 == number_to_guess:
            print("Has ganado")
        else:
            user_number_3 = int(input("Prueba de nuevo: "))
            if user_number_3 == number_to_guess:
                print("Has ganado")
            else:
                user_number_4 = int(input("Te doy un ultimo intento: "))
                if user_number_4 == number_to_guess:
                    print("Iba siendo hora")
                else:
                    print("Te has quedado sin oportunidades")



