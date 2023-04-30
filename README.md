# Simulación del Productor y Cosumidor: RESTAURANTE

1)EXPLICACIÓN
El modelo de productor y consumidor se utiliza en programación concurrente para resolver el problema de espera cuando el productor y el consumidor tienen diferentes velocidades de procesamiento. Los beneficios de este modelo incluyen el equilibrio entre productores y consumidores y la eliminación de la necesidad de que estén directamente conectados. 

2) SIMULACIÓN 
El código presentado utiliza una cola sincronizada para comunicarse entre el productor y el consumidor, donde el productor genera datos y los agrega a la cola, y el consumidor consume los datos de la cola. En este caso, el productor genera comida para los clientes y los consumidores, los comensales, se la comen.

Hemos creado cocineros y clientes que corresponden al productor y consumidor respectivamente.
También hemos creado las comidas que serán de dos tipos: Hamburguesas o Sushi. ---> Uso de dos colas limitadas.
La comida que se coma el comensal será elegida de forma aleatoria.
Para una mejor simulación ponemos un retardo aleatorio tanto al comer como al cocinar un plato de comida.
Tener en cuenta que una cola puede estar vacía o llena.
