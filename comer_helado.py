
apetece_helado_input = input("Te apetece un helado? (Si / No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado_input = True

elif apetece_helado_input == "NO":
    apetece_helado = False

else:
    print("No se lo que me has dicho, asi que lo tomare como un NO")
    apetece_helado = False


puede_permitirselo = tiene_dinero_input == "SI" or esta_su_tia_input == "SI"
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if apetece_helado and puede_permitirselo and esta_el_senor_helados:
    print("Pues comete un helado")
else:
    print("Pues nada")
