class Persona:
    # Atributo de clase
    raza = "Humano"
    faccion = "Imperio"

    def __init__(self, nombre, apellido, afiliacion):
        # Atributo de objeto de la instancia Marine
        self.nombre = nombre
        self.apellido = apellido
        self.afiliacion = afiliacion
        # Se pueden definir atributos por defecto en una objeto instancia
        self.vivo = "Afirmativo"

    def presentacion(self):
        """
        Este es un metodo de instancia, accedemos a los Atributos de Instancia del Objeto.
        :return:
        """
        print(f"Saludos, mi nombre es {self.nombre} {self.apellido}.")

    @staticmethod
    def soy_un():
        print("Soy una persona.")

    @classmethod
    def identificar_raza(cls):
        """
        Los metodos de clase pueden acceder a los Atributos de Clase.
        :return:
        """
        print(f"Raza: {cls.raza}")

    @staticmethod
    def orar():
        print("La persona empieza a Orar.")

    @classmethod
    def modificar_gobierno(cls, nuevo_gobierno):
        cls.faccion = nuevo_gobierno


class Milicia:
    
    def __init__(self, rango, especialidad, ataque, defensa):
        self.rango = rango
        self.especialidad = especialidad
        self.ataque = ataque
        self.defensa = defensa
        self.estado = "Activo"

    @staticmethod
    def soy_un():
        print("Soy parte de la milicia.")

    def modificar_rango(self, rango_nuevo):
        """
        Este es un metodo de instancia, modifica un Atributo de Instancia.
        :param rango_nuevo:
        :return:
        """
        print(f"Paso del rango {self.rango} a {rango_nuevo}.")
        self.rango = rango_nuevo


class Marine(Persona, Milicia):

    def __init__(self, nombre, apellido, afiliacion, rango, especialidad, ataque, defensa, capitulo):
        # Envía los atributos 'nombre' y 'apellido' al constructor padre.
        # super().__init__(nombre, apellido, afiliacion) >>> En caso de tener un solo padre bastaría con el super()
        Persona.__init__(self, nombre, apellido, afiliacion)
        Milicia.__init__(self, rango, especialidad, ataque, defensa)
        self.capitulo = capitulo

    def orar(self):
        """
        Método sobreescrito
        :return:
        """
        print("El marine levanta una oración al Emperador.")

    @classmethod
    def modificar_gobierno(cls, nuevo_gobierno):
        cls.faccion = nuevo_gobierno

    def modificar_rango(self, rango_nuevo):
        print(f"El Marine {self.nombre} {self.nombre} ha pasado de {self.rango} a {rango_nuevo}")
        self.rango = rango_nuevo

    def soy_un(self):
        print("Soy un Marine Espacial.")

    def __str__(self):
        return f"- FICHA TÉCNICA DEL MARINE ESPACIAL -\n" \
               f"Raza: {self.raza}\n" \
               f"Facción: {self.faccion}\n" \
               f"Vivo: {self.vivo}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Apellido: {self.apellido}\n" \
               f"Afiliación: {self.afiliacion}\n" \
               f"Capitulo: {self.capitulo}\n" \
               f"Estado: {self.estado}\n" \
               f"Rango: {self.rango}\n" \
               f"Especialidad: {self.especialidad}\n" \
               f"Ataque: {self.ataque}\n" \
               f"Defensa: {self.defensa}\n"


# HERENCIA
'''
Clase padre
'''
humano_estandar = Persona("Igni", "Proteus", "Civil")
'''
Clase Hija
'''
marine_estandar = Marine("Malneus", "Kalgar", "Marines Espaciales", "Capitan", "Estratega", 80, 70, "Ultramarines")

# METODO DE INSTANCIA HEREDADO
'''
Metodo que accede a valores de instancia
'''
humano_estandar.presentacion()
marine_estandar.presentacion()

# METODO DE CLASE HEREDADO
'''
Metodo de Clase que puede acceder a los atributos de clase... 
'''
Persona.identificar_raza()
'''
Estos metodos se heredan igual que los atributos de clase de su clase padre, 
pero es necesario colocar la anotacion @classmethod...
'''
Marine.identificar_raza()
'''
pueden acceder a los atributos de clase propios o heredados, este será el mismo que el propio,
a menos que el atributo sea modificado en la clase hija...
'''
print(Marine.faccion)
'''
Sin embargo, cuando se manipulan los atributos de clase, solo lo hacen con la clase que la instancia... 
El objeto o la clase Marine únicamente puede modificar el atributo de clase heredado en la clase Marine, 
pasa lo mismo con la clase Persona.
# En el metodo 'modificar_gobierno(nuevo_gobierno)'
# Se modifica el atributo de la clase Marine, no el que hereda de Persona
'''
marine_estandar.modificar_gobierno("Imperio Secundus")
print(Persona.faccion)
print(Marine.faccion)

# METODO ESTATICO HEREDADO SOBREESCRITO
'''
Metodo Estatico del padre que es heredado y no puede acceder a los atributos de clase o de instancia
'''
Persona.orar()
'''
Este metodo está heredado y sobreescrito, no es necesario que lleve la anotacion @staticmethod
'''
marine_estandar.orar()

# METODO DE INSTANCIA HEREDADO Y SOBREESCRITO DE UNA SEGUNDA CLASE PADRE
'''
Metodo exclusivo de la clase Milicia
'''
marine_estandar.modificar_rango("General")

# METODO ESTATICO CON EL MISMO NOMBRE HEREDADO DE DOS CLASES PADRE, APLICA PARA LOS METODOS DE CLASE Y DE INSTANCIA
'''
Cuando dos clases padre tienen un metodo con el mismo nombre, se prioriza a la primera clase heredada.
'''
Persona.soy_un()
Milicia.soy_un()
marine_estandar.soy_un()

# DETERMINAR CLASES PADRE
print(Marine.__mro__)

# POLIMORFISMO
'''
En Python el tipo de la variable es definido por el tipo del objeto que guarda, 
entonces siempre se va a llamar a los todos de ese objeto, 
sin embargo si hereda el metodo, se irá escalando hasta encontrar el metodo hasta la clase donde lo herede.
'''
Persona.soy_un()
Milicia.soy_un()
marine_estandar.soy_un()

# METODOS ESPECIALES
'''
Son métodos predefinidos con nombres especiales que se utilizan para 
realizar operaciones específicas en objetos de una clase.
'''
print(marine_estandar)
