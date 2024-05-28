from abc import ABC, abstractmethod


class Vehiculo(ABC):

    def __init__(self, matricula, marca, modelo, anio, tamanio):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tamanio = tamanio

    @abstractmethod
    def arrancar(self):
        print("Arrancando.")

    @abstractmethod
    def frenar(self):
        print("Frenando.")


class VehiculoMotorizadoInterface(ABC):

    @abstractmethod
    def encender_motor(self):
        print("Motor encendido.")

    @abstractmethod
    def apagar_motor(self):
        print("Motor apagado.")


class VehiculoElectricoInterface(ABC):

    @abstractmethod
    def cargar_bateria(self):
        print("Batería cargada.")

    @abstractmethod
    def descargar_bateria(self):
        print("Batería descargada.")


class Coche(Vehiculo, VehiculoMotorizadoInterface):

    def __init__(self, matricula, marca, modelo, anio, tamanio, puertas, combustible):
        super().__init__(matricula, marca, modelo, anio, tamanio)
        self.puertas = puertas
        self.combustible = combustible

    def arrancar(self):
        print("El coche está arrancando.")

    def frenar(self):
        print("El coche está frenando.")

    def encender_motor(self):
        print("El motor del coche está encendido.")

    def apagar_motor(self):
        print("El motor del coche está apagado.")


class CocheElectrico(Vehiculo, VehiculoElectricoInterface):

    def __init__(self, matricula, marca, modelo, anio, tamanio, velocidad_carga):
        super().__init__(matricula, marca, modelo, anio, tamanio)
        self.velocidad_carga = velocidad_carga

    def arrancar(self):
        print("El coche está arrancando.")

    def frenar(self):
        print("El coche está frenando.")

    def cargar_bateria(self):
        print("Batería cargada.")

    def descargar_bateria(self):
        print("Batería descargada.")


class Moto(Vehiculo, VehiculoMotorizadoInterface):

    def __init__(self, matricula, marca, modelo, anio, tamanio, cilindrada):
        super().__init__(matricula, marca, modelo, anio, tamanio)
        self.cilindrada = cilindrada

    def arrancar(self):
        print("La moto está arrancando.")

    def frenar(self):
        print("La moto está frenando.")

    def encender_motor(self):
        print("El motor de la moto está encendido.")

    def apagar_motor(self):
        print("El motor de la moto está apagado.")


class Sidecar(Vehiculo):

    def __init__(self, matricula, marca, modelo, anio, tamanio, pasajeros):
        super().__init__(matricula, marca, modelo, anio, tamanio)
        self.pasajeros = pasajeros

    def arrancar(self):
        print("El sidecar está arrancando.")

    def frenar(self):
        print("El sidecar está frenando.")


class Bicicleta(Vehiculo):

    def __init__(self, matricula, marca, modelo, anio, tamanio, marchas):
        super().__init__(matricula, marca, modelo, anio, tamanio)
        self.marchas = marchas
        self.ruedas_infladas = True

    def arrancar(self):
        print("La bicicleta está arrancando.")

    def frenar(self):
        print("La bicicleta está frenando.")

    def inflar_ruedas(self):
        self.ruedas_infladas = True  # Añade esta línea
        print("Ruedas infladas.")


class Garaje:

    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.motos = []
        self.coches = []
        self.bicicletas = []
        self.capacidad_motos = 2
        self.capacidad_coches = 2
        self.capacidad_bicicletas = 2

    def __str__(self):
        return f"Garaje {self.nombre} en {self.direccion}"

    def ingresar_vehiculo(self, vehiculo):
        if isinstance(vehiculo, Coche) or isinstance(vehiculo, CocheElectrico):
            if len(self.coches) < self.capacidad_coches:
                self.coches.append(vehiculo)
                print(f"Coche {vehiculo.matricula} ingresado")
            else:
                raise LimiteVehiculosException("No hay espacio para más coches.")
        elif isinstance(vehiculo, Moto):
            if len(self.motos) < self.capacidad_motos:
                self.motos.append(vehiculo)
                print(f"Moto {vehiculo.matricula} ingresada")
            else:
                raise LimiteVehiculosException("No hay espacio para más motos.")
        elif isinstance(vehiculo, Bicicleta):
            if len(self.bicicletas) < self.capacidad_bicicletas:
                self.bicicletas.append(vehiculo)
                print(f"Bicicleta {vehiculo.matricula} ingresada")
            else:
                raise LimiteVehiculosException("No hay espacio para más bicicletas.")
        elif isinstance(vehiculo, Sidecar):
            if vehiculo.tamanio != "grande":
                if len(self.coches) < self.capacidad_coches:
                    self.coches.append(vehiculo)
                    print(f"Sidecar {vehiculo.matricula} ingresada")
                else:
                    raise LimiteVehiculosException("No hay espacio en el parqueadero de coches.")
            else:
                raise LimiteTamanioException
        else:
            print("Vehículo no soportado.")


class LimiteVehiculosException(Exception):
    def __init__(self, message="No hay espacio para más vehículos."):
        self.message = message
        super().__init__(self.message)


class LimiteTamanioException(Exception):
    def __init__(self, message="No hay espacio para vehículos de este tamaño."):
        self.message = message
        super().__init__(self.message)


garaje = Garaje("Garaje de Emilio", "Calle Del Muerto 123")


coche1 = Coche("1234ABC", "Ford", "Fiesta", 2010, "mediano", 5, "gasolina")
coche2 = Coche("7156CBD", "Chevrolet", "Titan", 2010, "mediano", 5, "gasolina")
coche3 = Coche("7867UIO", "Honda", "Spark", 2010, "mediano", 5, "gasolina")


moto1 = Moto("5678DEF", "Yamaha", "FZ", 2015, "pequeno", 250)
moto2 = Moto("8973OPK", "Honda", "C200", 2015, "pequeno", 250)
moto3 = Moto("3647IJK", "Harley", "ZX", 2015, "pequeno", 250)


bicicleta1 = Bicicleta("91011GHI", "Orbea", "Orca", 2018, "pequeno", 22)
bicicleta2 = Bicicleta("1415MNO", "Orbea", "Ballena", 2018, "pequeno", 22)
bicicleta3 = Bicicleta("1617PQR", "ZX", "Mastin", 2018, "pequeno", 22)

sidecar1 = Sidecar("1213JKL", "Harley Davidson", "Electra Glide", 2015, "grande", 2)
sidecar2 = Sidecar("1415MNO", "Harley Davidson", "Electra Glide", 2015, "mediano", 2)

# COCHES

try:
    garaje.ingresar_vehiculo(coche1)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(coche2)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(coche3)
except LimiteVehiculosException as e:
    print(e.message)

# MOTOS

try:
    garaje.ingresar_vehiculo(moto1)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(moto2)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(moto3)
except LimiteVehiculosException as e:
    print(e.message)


# BICICLETAS

try:
    garaje.ingresar_vehiculo(bicicleta1)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(bicicleta2)
except LimiteVehiculosException as e:
    print(e.message)

try:
    garaje.ingresar_vehiculo(bicicleta3)
except LimiteVehiculosException as e:
    print(e.message)

# SIDECAR

try:
    garaje.ingresar_vehiculo(sidecar1)
except LimiteVehiculosException as e:
    print(e.message)
except LimiteTamanioException as e:
    print(e.message)


try:
    garaje.ingresar_vehiculo(sidecar2)
except LimiteVehiculosException as e:
    print(e.message)
except LimiteTamanioException as e:
    print(e.message)



