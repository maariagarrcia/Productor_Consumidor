from multiprocessing import Process, Queue
from colorama import Fore
import time
import random



## 3 CLASES: Cocinero, Comensal, Comida
class Cocinero(Process):
    def __init__(self, id_cocinero: int, nombre_comida: str, cola: Queue):
        super().__init__()
        self.id_cocinero = id_cocinero
        self.nombre_comida = nombre_comida
        self.cola = cola

    def cocinar(self) -> None:
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
                self.cola.put([self.id_cocinero, num_plato, self.nombre_comida],
                              block=True, timeout=1)
                num_plato += 1
                print(Fore.YELLOW+"+ Cocinero"+Fore.WHITE, self.id_cocinero, "cocinando", self.nombre_comida)
            except:
                print(Fore.RED+"+ Cocinero", self.id_cocinero,
                      "No me necesitan más!!!", num_plato, "<----------"+Fore.WHITE)
                return


class Comensal(Process):
    def __init__(self, id_comensal: int, colas: list):
        super().__init__()
        self.id_comensal = id_comensal
        self.colas = colas

    def comer(self) -> None:
        # Decidir cuantos platos quier comer
        # max_platos = random.randint(2, 5)
        max_platos = 2

        for num_platos in range(1, max_platos+1):
            # Seleccionar comida
            comida: Queue = random.choice(self.colas)

            # Si hay comida en la cola coger plato.
            # Si no hay comida este proceso se bloquea.
            # Si la espera supera 5s se genera un error.
            try:
                plato = comida.get(block=True, timeout=3)

                # Comer -> Simular tiempo consumición plato
                time.sleep(random.random()*10)
                print(Fore.GREEN+"- Comensal"+Fore.WHITE, self.id_comensal, "Comiendo", plato)

            except:
                # Se ha superado el tiempo máximo de espera de un
                # plato por parte del cliente que decide abandonar
                # el restaurante enfadado :-0
                print(Fore.RED+"- Comensal", self.id_comensal,
                    "Me voy!!!. Son muuy lentos :-(", num_platos-1,"<-----------"+Fore.WHITE)
                return 

        print(Fore.RED+"- Comensal", self.id_comensal, "He comido suficiente...", max_platos, "<-----------"+Fore.WHITE)

class Comida:

    