
apetece_helado_input = input("te apetece un helado? (si / no): ").upper()
tienes_dinero_input = input("tienes dinero para comprarlo? (si / no ): ").upper()
esta_senor_helados_input = input("¿esta el señor de los helados? (si / no): ").upper()
esta_tu_tia_input = input("estas con tu tia? (si / no): ").upper()

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tienes_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_senor_helados = esta_senor_helados_input == "SI "

if apetece_helado and puede_permitirselo and esta_senor_helados:
    print("Pues comete un helado")
else:
    print("pues nada")