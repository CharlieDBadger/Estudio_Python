import time
from threading import Thread

'''
Los hilos son una forma de ejecutar multiples tareas de forma simultanea o concurrente.
En caso de ser simultanea, se ejecutan al mismo tiempo, 
en caso de ser concurrente, se ejecutan al mismo tiempo pero de forma alternada.


- Procesos Consecutivos / Preparamos y horneamos 1 pizza -> Comemos 1 pizza 
- Procesos Concurrentes / Preparamos 1 pizza mientras la otra se hornea -> Comemos 2 pizzas 
- Procesos Simultaneos / Preparamos y horneamos ambas pizzas al mismo tiempo -> Comemos 2 pizzas 
'''

# DEFINIMOS DOS FUNCIONES CON UN CONTADOR TEMPORAL
def cook_pizza_a():
    time.sleep(3)
    return "cook_pizza_a"


def cook_pizza_b():
    time.sleep(3)
    return "cook_pizza_b"


# INICIAMOS UNA VARIABLE DE TIEMPO
start = time.time()

# INICIAMOS DOS HILOS DE EJECUCION
thread_a = Thread(target=lambda: print(cook_pizza_a()))
thread_b = Thread(target=lambda: print(cook_pizza_b()))

# INICIAMOS LOS HILOS
thread_a.start()
thread_b.start()

# EL METODO JOIN NOS OBLIGA A ESPERAR QUE LOS HILOS TERMINEN
thread_a.join()
thread_b.join()

# IMPRIMIMOS EL TIEMPO DE EJECUCION
print("Eating...")
print("Time:", time.time() - start)
