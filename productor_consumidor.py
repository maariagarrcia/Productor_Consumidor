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
##                                - cocinar
#                                 - comer: hamburguesas y sushi
#                                 - crear colas
#                                 - crear procesos 
#  

def crear_cocineros():
    pass

def crear_comensales():
    pass

def cocinar():
    pass

def comer():
    pass

def arrancar_todo():
    pass

def esperar_finalizacion_procesos():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
