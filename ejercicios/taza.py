import random


class HotException(Exception):
    pass


class CoolException(Exception):
    pass


def taza(temperature):
    if temperature > 60:
        raise HotException
    elif temperature < 30:
        raise CoolException
    else:
        return "Just right"


def drink(temperature):
    try:
        return taza(temperature)
    except HotException:
        return "Too hot"
    except CoolException:
        return "Too cold"


print(drink(50))

clientes = [{"cliente": "Emilio", "temperatura": random.randint(1, 100)},
            {"cliente": "Oscar", "temperatura": random.randint(1, 100)},
            {"cliente": "Laura", "temperatura": random.randint(1, 100)}]

for cliente in clientes:
    temperatura = cliente["temperatura"]
    print(drink(temperatura))
