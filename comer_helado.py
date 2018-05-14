
apetece_helado_input = input("te apetece un helado? (si / no): ")
tienes_dinero_input = input("tienes dinero para comprarlo? (si / no ): ")
esta_senor_helados_input = input("¿esta el señor de los helados? (si / no): ")
esta_tu_tia_input = input("estas con tu tia? (si / no): ")

apetece_helado = apetece_helado_input == "si"
puede_permitirselo = tienes_dinero_input == "si" or esta_tu_tia_input == "si"
esta_senor_helados = esta_senor_helados_input == "si"

if apetece_helado and puede_permitirselo and esta_senor_helados:
    print("Pues comete un helado")
else:
    print("pues nada")