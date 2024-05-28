class UsernameCodyException(Exception):
    def __init__(self, username):
        self.username = username
        self.message = "El nombre de usuario no puede ser 'Cody'"

    def __str__(self):
        return f"{self.message}: {self.username}"


class UsernameLenException(Exception):
    def __init__(self, username):
        self.username = username
        self.message = "El nombre de usuario debe tener al menos 5 caracteres"

    def __str__(self):
        return f"{self.message}: {self.username}"


def validar_username(username):
    if username == "Cody":
        raise UsernameCodyException(username)
    if len(username) < 5:
        raise UsernameLenException(username)
    return username


try:
    print(validar_username("Cody"))
except UsernameCodyException as error:
    print(error)
except UsernameLenException as error:
    print(error)


def pedir_int():
    check = False
    while not check:
        try:
            num = int(input("Introduce un numero: "))
        except ValueError:
            # No es obligatorio definir el tipo de excepción,
            # pero eso haría más difícil depurar el error.
            print("Eso no es un numero.")
        except TypeError:
            # También pueden programarse diferentes acciones según el tipo de error que surja.
            print("Ha surgido un error inesperado.")
        else:
            # En caso de que no se dé una excepción,
            # podemos introducir aquí otra acción, como modificar la condición de un while.
            print("Efectivamente has introducido un numero.")
            check = True
            return num
        finally:
            # Esta parte del código se ejecutará si hay o no excepción.
            print("Has usado la función pedir_int().")


print(f"Has introducido el numero: {pedir_int()}")