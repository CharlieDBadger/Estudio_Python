import time
from threading import Thread


def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


start = time.time()

a = Thread(target=lambda: fibonacci(35))
b = Thread(target=lambda: fibonacci(30))

a.start()
b.start()

a.join()
b.join()

print(f"Time: {time.time() - start}")