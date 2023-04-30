# Colas
# =====
#   https://docs.python.org/3/library/queue.html#queue.Queue
#   https://superfastpython.com/multiprocessing-queue-in-python/
#
#
# Descripción de la simulación del productor/consumidor
# =====================================================
# · Se usa multprocessing.
# · Simulamos un restaurante. (Buffet)
# · Los productores son COCINEROS que producen comida.
# · Hay dos tipos de comida: hambuguesas y suchi.
# · Los cocineros seleccionan el tipo de comida aleatoriamente.
# · Los consumidores son los COMENSALES.
# · Los comensales escojen comida aleatoriamente.
# · Creo una cola por tipo de comida
#       (Muy importante: las colas son seguras para multiprocesamiento).
# · Despues de cocinar un plato de comida hay un retardo aleatorio.
# · Despues de consumir un plato hay un retardo aleatorio.
# · Se limita el tamaño de las colas de comida a 5 platos.
# · Si las colas estan llenas los cocineros paran.
# · Si las colas estan vacias los comensales esperan.
#
# Parámetros de la simulación
# ===========================
# · Se crean 2 cocineros.
# · Se crean 10 comensales.
# · Los comensales comensales comen de 2 a 5 platos máximo.
#

## FUNCIONES QUE NECESITAMOS ---> - crear cocineros y comensales
#                                 - cocinar: hamburguesas y sushi
#                                 - comer: hamburguesas y sushi
#                                 - crear colas
#                                 - crear procesos 
#  


from multiprocessing import Process, Queue
from colorama import Fore
import time
import random

### DPS PASARLO A POO Y A VISTA CONTROLADOR

def arrancar_todo(procesos) -> None:
    print("* Arrancando procesos...")
    for p in procesos:
        p.start()

def cocinar(id_cocinero: int, nombre_comida: str, cola: Queue) -> None:
    # Contador de platos producidos
    num_plato = 0

    while True:
        # Cocinar -> Simular tiempo cocinado
        time.sleep(random.random())

        # Si no está llena la cola dejar plato
        # Si la cola esta llena se espera a que algun cliente
        # consuma algún plato.
        # Si timeout se supera el cocinero se va a su casa ya
        # que los clientes han dejado de comer

        try:
            cola.put([id_cocinero, num_plato, nombre_comida],
                     block=True, timeout=1)
            num_plato += 1
            print(Fore.YELLOW+"+ Cocinero"+Fore.WHITE, id_cocinero, "cocinando", nombre_comida)
        except:
            print(Fore.RED+"+ Cocinero", id_cocinero,
                  "No me necesitan más!!!", num_plato, "<----------"+Fore.WHITE)
            return

def comer(id_comensal, colas: list) -> None:
    # Decidir cuantos platos quier comer
    # max_platos = random.randint(2, 5)
    max_platos = 2

    for num_platos in range(1, max_platos+1):
        # Seleccionar comida
        comida: Queue = random.choice(colas)

        # Si hay comida en la cola coger plato.
        # Si no hay comida este proceso se bloquea.
        # Si la espera supera 5s se genera un error.
        try:
            plato = comida.get(block=True, timeout=3)

            # Comer -> Simular tiempo consumición plato
            time.sleep(random.random()*10)
            print(Fore.GREEN+"- Comensal"+Fore.WHITE, id_comensal, "Comiendo", plato)

        except:
            # Se ha superado el tiempo máximo de espera de un
            # plato por parte del cliente que decide abandonar
            # el restaurante enfadado :-0
            print(Fore.RED+"- Comensal", id_comensal,
                  "Me voy!!!. Son muuy lentos :-(", num_platos-1,"<-----------"+Fore.WHITE)
            return 

    print(Fore.RED+"- Comensal", id_comensal, "He comido suficiente...", max_platos, "<-----------"+Fore.WHITE)


def crear_cocineros(cantidad, cola_hamburguesas, cola_suchi) -> list():
    print("* Creando cocineros...")
    cocineros = []
    nombres_comida = ["hamburguesa", "sushi"]
    colas_comida = [cola_hamburguesas, cola_suchi]

    for id_cocinero in range(0, cantidad):
        # Seleccionar que comida elabora el cocinero
        nombre_comida = nombres_comida[id_cocinero % 2]
        cola_comida = colas_comida[id_cocinero % 2]

        cocineros.append(
            Process(target=cocinar, args=[id_cocinero, nombre_comida, cola_comida]))

    return cocineros


def crear_comensales(cantidad, cola_hamburguesas, cola_suchi) -> list():
    cocineros = []

    print("* Creando comensales...")
    for id_comensal in range(0, cantidad):
        cocineros.append(
            Process(target=comer, args=[id_comensal, [cola_hamburguesas, cola_suchi]]))

    return cocineros


def esperar_finalizacion_procesos(procesos):
    print("* Esperando finalización procesos...")
    print("·")
    for p in procesos:
        p.join()

def main():
    print()
    print("Simulacion de Productor/Consumidor: Restaurante")
    print("· Se crean 2 cocineros")
    print("· Se crean 10 comensales")
    print("· Se limita el tamaño de las colas de comida")
    print("· Si las colas estan llenas los cocineros paran")
    print("· Si las colas estan vacias los comensales esperan")
    print("· Los comensales comensales comen un máximo de 4 platos")
    print("·")

    # Crear colas (una por comida) capacidad máxima para 5 elementos
    max_hamburguesas = 3
    cola_hamburguesas = Queue(max_hamburguesas)
    max_sushi = 2
    cola_suchi = Queue(max_sushi)

    # Crear procesos
    procesos = []
    procesos = crear_cocineros(2, cola_hamburguesas, cola_suchi)
    procesos = procesos + crear_comensales(10, cola_hamburguesas, cola_suchi)

    # Ejecutar procesos consumidores y productores (comensales y cocineros)
    arrancar_todo(procesos)

    esperar_finalizacion_procesos(procesos)

    print("*** Simulación finalizada ***")

if __name__ == "__main__":
    main()




        



