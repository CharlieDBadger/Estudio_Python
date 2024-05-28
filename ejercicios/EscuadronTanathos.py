recluta1 = {"nombre": "Asrael", "legion": "Angeles Oscuros", "id": "67234", "ataque": 76}
recluta2 = {"nombre": "Miguel", "legion": "Angeles Sangrientos", "id": "35234", "ataque": 85}
recluta3 = {"nombre": "Tasarius", "legion": "Puños Imperiales", "id": "84435", "ataque": 50}
recluta4 = {"nombre": "Argel", "legion": "Ultramarines", "id": "13223", "ataque": 65}
recluta5 = {"nombre": "Tiburius", "legion": "Guardia de la Muerte", "id": "08943", "ataque": 90}

escuadron = [recluta1, recluta2]
refuerzos = [recluta3, recluta4, recluta5]

for recluta in refuerzos:
    escuadron.append(recluta)

menu = ["PROTOCOLO - FORMACIÓN DE ESCUADRON:",
        "1. Ingresar Recluta.",
        "2. Buscar Recluta por ID.",
        "3. Borrar Recluta.",
        "4. Mostrar reclutas.",
        "5. Salir."]

seleccion = 0

while seleccion != len(menu) - 1:

    # SELECCIÓN DE OPCIÓN: MENÚ
    checkSeleccion = False
    while not checkSeleccion:
        for opcion in menu:
            print(opcion)
        try:
            seleccion = int(input("Escoja una opción: "))
            if 1 <= seleccion <= len(menu) - 1:
                checkSeleccion = True
            else:
                print("Ingrese una opcion valida")
        except ValueError:
            print("Debes ingresar un número.")

    # seleccion = int(input("Escoja una opción: "))

    match seleccion:
        case 1:  # INGRESO RECLUTA

            # DOOMIE RECLUTA
            nuevoRecluta = {"nombre": None, "legion": None, "id": None, "ataque": None}
            datos = ("Nombre", "Legión", "ID / 5 digitos", "Ataque / 1 - 100")
            checkAtaque = False
            checkId = False

            # INGRESO DE RECLUTA
            for clave, dato in zip(nuevoRecluta.keys(), datos):

                # INGRESO DE DATO
                if clave != "id" and clave != "ataque":
                    checkNotEmpty = False
                    while not checkNotEmpty:
                        nuevoRecluta[clave] = input(f"Introduzca {dato}: ")
                        if nuevoRecluta[clave] == "":
                            print("El campo no puede quedar vacío.")
                        else:
                            checkNotEmpty = True

                # VALIDACIÓN ID
                elif clave == "id":
                    while not checkId:
                        nuevoRecluta[clave] = str(input(f"Introduzca {dato}:"))
                        if len(nuevoRecluta[clave]) != 5:
                            print("El ID debe ser de 5 digitos.")
                        else:
                            print("Verificación BBDD...")
                            for recluta in escuadron:
                                if nuevoRecluta[clave] == recluta["id"]:
                                    print("Este ID ya existe en la base de datos.")
                                    break
                                elif nuevoRecluta[clave] != recluta["id"]:
                                    '''
                                    print("Validando ID con el recluta",recluta["nombre"]) 
                                    '''
                                    checkId = True
                    else:
                        print("Verificación de ID completada.")

                # VERIFICACIÓN ATAQUE
                elif clave == "ataque":
                    while not checkAtaque:
                        try:
                            nuevoRecluta[clave] = int(input(f"Introduzca {dato}:"))
                            if 1 <= nuevoRecluta[clave] <= 100:
                                print("Ataque dentro de los parámetros.")
                                checkAtaque = True
                            else:
                                print("Debes ingresar un valor de ataque entre 1 - 100")
                        except ValueError:
                            print("Debes ingresar un número entero para el ataque.")

            if checkId and checkAtaque:
                print("Ingreso de Recluta exitoso.")
                escuadron.append(nuevoRecluta)

        case 2:  # BUSCAR RECLUTA POR ID

            # PROPORCIONAR ID PARA BUSQUEDA
            idBuscado = str(input("Introduzca el ID del Recluta que desea Buscar: "))
            idEncontrado = False

            # RECORRIENDO LISTADO DE RECLUTAS
            for recluta in escuadron:
                if idBuscado == recluta["id"]:
                    print("Recluta encontrado:")

                    print(f"Nombre: {recluta['nombre']}\n"
                          f"Legión: {recluta['legion']}\n"
                          f"ID: {recluta['id']}\n"
                          f"Ataque: {recluta['ataque']}")

                    idEncontrado = True
                    break
            if not idEncontrado:
                print("El Recluta que está buscando no se encuentra en este Escuadron.")

        case 3:  # REMOVER RECLUTA DEL ESCUADRON

            # PROPORCIONAR ID PARA REMOVER RECLUTA
            idBuscado = str(input("Introduzca el ID del Recluta que desea Remover del Escuadron: "))
            reclutaRemovido = False

            # RECORRIENDO LISTADO DE RECLUTAS
            for recluta in escuadron:
                print("Traza")
                print(idBuscado == recluta["id"])
                if idBuscado == recluta["id"]:
                    escuadron.remove(recluta)
                    print(f"Recluta {recluta['nombre']} ha sido removido del Escuadron")
                    reclutaRemovido = True
                    break
            if not reclutaRemovido:
                print("El Recluta que está buscando no se encuentra en este Escuadron.")

        case 4:  # MOSTRAR ESCUADRON

            # RECORRIENDO LISTA DE RECLUTAS
            print("Mostrando Reclutas dentro del Escuadron:")
            for recluta in escuadron:
                print(f"Recluta: {recluta['nombre']}\n"
                      f"Legion: {recluta['legion']}\n"
                      f"--------------------------")

        case 5:  # SALIR
            print("PROTOCOLO TERMINADO.")
            print("EL EMPERADOR PROTEGE.")
            break
