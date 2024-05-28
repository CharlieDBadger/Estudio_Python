# SOLO ES POSIBLE AÑADIR ANOTACIONES A PARTIR DE LA PYTHON V3.11

class UsernameException(Exception):
    def __init__(self, username):
        self.username = username
        self.message = "Nombre de usuario Invalido."

    def __str__(self):
        return f"{self.message}: {self.username}"

    def is_valid_to_raise(self):
        return len(self.__notes__) > 0

    def show_notes(self):
        for note in self.__notes__:
            print(note)


def username_validation(username):
    username_error = UsernameException(username)
    if len(username) < 6:
        username_error.add_note("El nombre de usuario debe tener al menos 5 caracteres")
    if username.lower() == "cody":
        username_error.add_note("El nombre de usuario no puede ser 'Cody'")
    if "@" in username:
        username_error.add_note("El nombre de usuario no puede contener el caracter '@'")
    if username_error.is_valid_to_raise():
        raise username_error
    return username


try:
    username = "@cody"
    username_validation(username)
except UsernameException as error:
    print(error)
    error.show_notes()
