import time
from multiprocessing import Process


def fibonacci(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


start = time.time()

a = Process(target=lambda: fibonacci(35))
b = Process(target=lambda: fibonacci(30))

a.start()
b.start()

a.join()
b.join()

print(f"Time: {time.time() - start}")
