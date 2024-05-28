class CustomException(Exception):
    def __init__(self, message="Custom Exception1"):
        self.message = message
        super().__init__(self.message)


class CustomException2(Exception):
    def __init__(self, message="Custom Exception2"):
        self.message = message
        super().__init__(self.message)


class CustomException3(Exception):
    def __init__(self, message="Custom Exception3"):
        self.message = message
        super().__init__(self.message)

# LAS SIGUIENTES FUNCIONALIDADES DE EXCEPCIONES SOLO ESTAN DISPONIBLES DESDE LA PYTHON V3.11
# EXCEPCIONES AGRUPADAS

# TRATAMIENTO GRUPAL
try:
    raise ExceptionGroup(
        "Un grupo de excepciones",
        [CustomException("Excepción 1"), CustomException2("Excepción 2"), CustomException3("Excepción 3")]
    )
except ExceptionGroup as group:
    print(group)

# TRATAMIENTO INDIVIDUAL A PARTIR DEL GRUPAL.
try:
    raise ExceptionGroup(
        "Un grupo de excepciones",
        [CustomException("Excepción 1"), CustomException2("Excepción 2"), CustomException3("Excepción 3")]
    )
except CustomException as error:
    print(error)
except CustomException2 as error:
    print(error)
except CustomException3 as error:
    print(error)
