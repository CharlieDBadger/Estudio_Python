import modulos_propios


stock_total = [{"Lacteos": [
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1}]},
               {"Carnes": [
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1}]},
               {"Harinas":
                    [{"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1},
                    {"Nombre": "Producto1", "Precio": 1}]}]

carrito = [{"Nombre": "Laptop", "Precio": 1000.00, "unds": 1}]
carritovacio = []

lacteos = [{"Nombre": "Yogurt", "Precio": 1.00, "unds": 10}, {"Nombre": "Leche", "Precio": 1.20, "unds": 10}]
carnes = [{"Nombre": "Res", "Precio": 1.00, "unds": 5}, {"Nombre": "Pollo", "Precio": 0.80, "unds": 7},
          {"Nombre": "Cerdo", "Precio" : 0.90, "unds": 10}]
panaderia = [{"Nombre": "Barra", "Precio": 0.50, "unds": 10}, {"Nombre": "Especial", "Precio": 1.20, "unds": 5}]

stock = [lacteos, carnes, panaderia]


menu = ["Añadir producto", "Quitar producto", "Pagar", "Salir"]
categorias = ["Lacteos", "Carnes", "Panadería"]
indicaciones = "+ Bienvenido al SuperChar +\n" \
               "Seleccione una categoría"

seleccion = 0

while seleccion != len(menu):
    seleccion = modulos_propios.seleccion_opcion_match(menu, indicaciones)

    match seleccion:
        case 1:
            # SELECCION CATEGORIA
            almacen = stock[modulos_propios.seleccion_opcion_index(categorias, "Seleccione una Categoría:")]

            # MOSTRAR PRODUCTOS DE LA CATEGORÍA
            producto_seleccionado = None
            i = 0
            print(f"Los productos disponibles: ")
            for producto in almacen:
                i += 1
                nombre = producto ['Nombre']
                precio = producto['Precio']
                unds = producto['unds']
                print(f"[{i}] {nombre} - Precio: € {precio} - unds: {unds}")

            # ESCOGER UN PRODUCTO ESPECIFICO
            producto_check = False
            while not producto_check:
                # ENTRA A UN CONTROL DE EXCEPCION EN CASO DE QUE METAN UN STRING Y NO UN INT
                try:
                    numero_producto = int(input("Escoja una opción: "))-1
                    # CONTROLA QUE LA SELECCION ESTÉ DENTRO DEL RANGO DE LOS PRODUCTOS PRESENTADOS
                    if 0 <= numero_producto <= len(almacen)-1:
                        producto_check = True

                        # SE SACA LA INFORMACION DEL PRODUCTO
                        producto_seleccionado = almacen[numero_producto]

                        nombre_producto = producto_seleccionado["Nombre"]
                        unds_disponibles = producto_seleccionado["unds"]
                        precio_und = producto_seleccionado["Precio"]

                        # SE VA A PREGUNTAR POR LAS UNIDADES A COMPRAR,
                        # HASTA QUE LA CANTIDAD ESTÉ DENTRO DEL STOCK DISPONIBLE
                        disponibilidad_check = False
                        while not disponibilidad_check:
                            try:
                                unds_a_comprar = int(input("¿Cuantas unidades desea añadir? "))

                                # SE EVALUA LA DISPONIBILIDAD DEL PRODUCTO
                                if unds_disponibles == 0:
                                    print("No hay unidades disponibles")
                                    disponibilidad_check = True
                                elif 1 <= unds_a_comprar <= unds_disponibles:
                                    disponibilidad_check = True

                                    precio_total = round((unds_a_comprar * precio_und), 2)
                                    producto_seleccionado["unds"] = unds_disponibles - unds_a_comprar
                                    producto_comprado = {"Nombre": nombre_producto, "Precio": precio_total,
                                                        "unds": unds_a_comprar}

                                    carrito.append(producto_comprado)

                                elif unds_a_comprar > unds_disponibles:
                                    print(f"Excedes el numero de unidades disponibles ({unds_disponibles}).")
                                else:
                                    print(f"{unds_disponibles} unidades disponibles.")
                            except ValueError:
                                print("Debes ingresar un número.")

                    else:
                        print(f"Ingrese una opcion entre 1 y {len(almacen)}.")
                except ValueError:
                    print("Debes ingresar un número.")

            # ESTADO ACTUAL DEL CARRITO
            print(carrito)
        case 2:
            if len(carrito) != 0:
                indicaciones_quitar = "¿Cual producto deseas sacar del carrito?"
                seleccion_quitar = None
                check_quitar = False
                while seleccion_quitar != len(carrito):
                    seleccion_quitar = modulos_propios.seleccion_opcion_index_salir(carrito, indicaciones_quitar)
                    if 0 <= seleccion_quitar <= len(carrito)- 1:

                        producto_a_quitar = carrito[seleccion_quitar]
                        print(f"Articulo: {carrito[seleccion_quitar]} removido.")
                        carrito.remove(producto_a_quitar)
                        print(f"Contenido de carrito actual:")
                        if len(carrito) != 0:
                            for producto in carrito:
                                print(producto)
                                continue
                        else:
                            print("Has vaciado el carrito.")
                            continue
            else:
                print("Carrito vacío.")
        case 3:
            pass