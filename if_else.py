
number_to_guess = 2

user_number = int(input("Dime un numero: "))

if user_number == number_to_guess:
    print("Exacto mi numero era {}" .format(number_to_guess))
else:
    print("lo siento mi numero no es {}".format(user_number))
