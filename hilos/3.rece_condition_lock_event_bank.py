import time
import logging
from threading import Thread, Lock, Event
from itertools import cycle

'''
RACE CONDITION
Es un problema que se presenta cuando dos o más hilos de ejecución acceden a un recurso compartido, 
como una variable, sin la sincronización adecuada.
'''

'''
PARA CONTROLAR EL PROBLEMA DE LA RACE CONDITION SE PUEDE UTILIZAR UNA CLASE LLAMADA LOCK
SACRIFICA RENDIMIENTO PORQUE BLOQUEA Y LIBERA EL RECURSO CADA VEZ QUE SE NECESITA ACCEDER A ÉL.
PERO, GARANTIZA QUE NO SE PRODUZCA EL ERROR MENCIONADO.
'''
lock = Lock()


logging.basicConfig(
    level=20,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class BackFacilito:

    def __init__(self):
        self.balance = 0
    '''
    def deposit(self):
        for i in range(10_000_000):
            # lock.acquire() bloquea el recurso
            lock.acquire()
            self.balance += 1
            # lock.release() libera el recurso
            lock.release()

    def withdraw(self):
        for i in range(10_000_000):
            # lock.acquire() bloquea el recurso
            lock.acquire()
            self.balance -= 1
            # lock.release() libera el recurso
            lock.release()
    '''

    def deposit(self):
        for i in range(10_000_000):
            with lock:
                self.balance += 1

    def withdraw(self):
        for i in range(10_000_000):
            with lock:
                self.balance -= 1


def loading(evento):
    for c in cycle(['|', '/', '-', '\\']):
        if evento.wait(.05):
            break
        print(c, end='\r', flush=True)


bank = BackFacilito()

start = time.time()

'''
FUTUTO o PROMESA (js)
Permite ejecutar código asincrónico (CALLBACKS) y manejar el resultado de una operación que puede tardar en completarse.
'''
# La clase Event tiene dos metodos, set y wait.
event = Event()


thread_a = Thread(target=bank.deposit)
thread_b = Thread(target=bank.withdraw)
thread_loading = Thread(target=loading, args=(event,))


thread_a.start()
thread_b.start()
thread_loading.start()

thread_a.join()
thread_b.join()

event.set()

print("El programa demoró: ", time.process_time(), "segundos")

print(f'Balance final: {bank.balance}')

