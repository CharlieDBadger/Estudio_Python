class Oficina:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.despachos = []

    def __str__(self):
        return f"{self.nombre} en {self.direccion}"

    def agregar_despacho(self, despacho):
        self.despachos.append(despacho)


class Despacho:
    def __init__(self, numero):
        self.numero = numero
        self.sillas = []
        self.mesas = []

    def __str__(self):
        return f"Despacho {self.numero} con {len(self.sillas)} sillas y {len(self.mesas)} mesas"

    def agregar_silla(self, silla):
        self.sillas.append(silla)

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)


class Mesa:
    def __init__(self, id, color, precio):
        self.id = id
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"Mesa {self.id} de color {self.color} vale {format(self.precio, '.2f')}"


class Silla:
    def __init__(self, id, color, precio):
        self.id = id
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"Silla {self.id} de color {self.color} vale {format(self.precio, '.2f')}"


# Uso
# Crear una oficina
oficina = Oficina("Oficina Principal", "Calle Falsa 123")

# Crear despachos
despacho1 = Despacho(1)
despacho2 = Despacho(2)

# Crear sillas
silla1 = Silla(1, "Blanca", 50)
silla2 = Silla(2, "Negra", 60)
silla3 = Silla(3, "Azul", 70)

# Crear mesas
mesa1 = Mesa(1, "Blanca", 100)
mesa2 = Mesa(2, "Negra", 110)
mesa3 = Mesa(3, "Azul", 120)

# Agregar sillas y mesas a los despachos
despacho1.agregar_silla(silla1)
despacho1.agregar_silla(silla2)
despacho2.agregar_silla(silla3)
despacho1.agregar_mesa(mesa1)
despacho1.agregar_mesa(mesa2)
despacho2.agregar_mesa(mesa3)

# Agregar despachos a la oficina
oficina.agregar_despacho(despacho1)
oficina.agregar_despacho(despacho2)

# Mostrar oficina
print(oficina)

# Mostrar despachos
for despacho in oficina.despachos:
    print(despacho)
    for silla in despacho.sillas:
        print(silla)


