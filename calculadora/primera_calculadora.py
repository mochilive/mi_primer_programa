
operacion_seleccionada = input("Que operacion quieres realizar? (Suma / Resta / Division / Multiplicacion): ").upper()

if operacion_seleccionada == "SUMA":
    print("Preparemos la {}".format(operacion_seleccionada))
    primer_numero = int(input("Dime el primer numero: "))
    segundo_numero = int(input("Dime el segundo numero: "))
    resultado = primer_numero + segundo_numero
    print("El resultado de la {} es: {}".format(operacion_seleccionada, resultado))

elif operacion_seleccionada == "RESTA":
    print("Preparemos la {}".format(operacion_seleccionada))
    primer_numero = int(input("Dime el primer numero: "))
    segundo_numero = int(input("Dime el segundo numero: "))
    resultado = primer_numero - segundo_numero
    print("El resultado de la {} es: {}".format(operacion_seleccionada, resultado))

elif operacion_seleccionada == "DIVISION":
    print("Preparemos la {}".format(operacion_seleccionada))
    primer_numero = int(input("Dime el primer numero: "))
    segundo_numero = int(input("Dime el segundo numero: "))
    resultado = int(primer_numero  / segundo_numero)
    print("El resultado de la {} es: {}".format(operacion_seleccionada, resultado))

elif operacion_seleccionada == "MULTIPLICACION":
    print("Preparemos la {}".format(operacion_seleccionada))
    primer_numero = int(input("Dime el primer numero: "))
    segundo_numero = int(input("Dime el segundo numero: "))
    resultado = primer_numero * segundo_numero
    print("El resultado de la {} es: {}".format(operacion_seleccionada, resultado))