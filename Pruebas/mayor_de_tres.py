n1 = int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Tercer numero: "))

if n1 > n2 and n1 > n3:
    resultado = n1
    print("El mayor es: {}".format(resultado))

elif n2 > n1 and n2 > n3:
    resultado = n2
    print("El mayor es: {}".format(resultado))

elif n3 > n1 and n3 > n2:
    resultado = n3
    print("El mayor es: {}".format(resultado))