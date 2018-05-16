

pokemon_elegido = input("¿Contra quien quieres luchar? (Squirtle / Charmander / Bulbasaur): ").upper()

""" contrincantes """

squirtle = "SQUIRTLE"
charmander = "CHARMANDER"
bulbasaur = "BULBASAUR"

"""Vidas"""

live_pikachu = 100
live_enemic = 0

ataque_pokemon = 0

if pokemon_elegido == squirtle:
    live_enemic = 90
    nombre_pokemon = "SQUIRTLE"
    ataque_pokemon = 8
elif pokemon_elegido == charmander:
    live_enemic = 80
    nombre_pokemon = "CHARMANDER"
    ataque_pokemon = 7
elif pokemon_elegido == bulbasaur:
    live_enemic = 100
    nombre_pokemon = "BULBASAUR"
    ataque_pokemon = 10

print("Vida Inicial de PIKACHU: {}" .format(live_pikachu))
print("Vida inicial del enemigo: {}" .format(live_enemic))

while live_pikachu > 0 and live_enemic > 0:

    select_atack = input("Que ataque vas a usar? (chispazo / bola voltio): ").upper()


    if select_atack == "CHISPAZO":
        print("Chispazo quitara 10 de vida al enemigo")
        live_enemic -= 10
    elif select_atack == "BOLA VOLTIO":
        print("Bola voltio quitara 12 de vida al enemigo")
        live_enemic -= 12

    print("vida del {}: {}".format(pokemon_elegido, live_enemic))

    print("{} te hace un ataque de {} de daño" .format(nombre_pokemon, ataque_pokemon))
    live_pikachu -= ataque_pokemon

    print("Vida de PIKACHU: {}".format(live_pikachu))

if live_enemic <= 0:
    print("Ganador: pikachu con {} puntos de vida" .format(live_pikachu))


print("El combate ha terminado")