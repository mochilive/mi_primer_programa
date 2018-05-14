
number_to_guess = 2

user_number = int(input("Primer intento, dime un numero: "))

if user_number == number_to_guess:
    print("Exacto mi numero era {}" .format(number_to_guess))
else:
    print("Perdiste, te quedan cuatro intentos.")
    user_number_dos = int(input("Segundo intento, dime un numero: "))
    if user_number_dos == number_to_guess:
        print("ganaste, mi numero era el {}".format(number_to_guess))
    else:
        print("perdiste de nuevo, te quedan tres intentos.")
        user_number_tres = int(input("Tercer intento, dime un numero: "))
        if user_number_tres == number_to_guess:
            print("ganaste, mi numero era el {}".format(number_to_guess))
        else:
            print("perdiste de nuevo, te quedan dos intentos")
            user_number_cuatro = int(input("Cuarto intento, dime un numero: "))
            if user_number_cuatro == number_to_guess:
                print("ganaste, mi numero era el {}".format(number_to_guess))
            else:
                print("Perdiste de nuevo, solo te queda un intento")
                user_number_cinco = int(input("Ultimo intento, dime un numero: "))
                if user_number_cinco == number_to_guess:
                    print("Ganaste, mi numero era el {}".format(number_to_guess))
                else:
                    print("lo siento pero no lo acertaste ni una vez, se te acabaron los intentos")
                    print("-PERDISTE-")