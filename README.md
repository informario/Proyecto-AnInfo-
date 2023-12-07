# Proyecto de AnInfo: Ahorcado

## Reglas de Juego

Bienvenidos al Ahorcado! En nuestro proyecto intentamos recrear el clásico juego, desde nuestro propio punto de vista. El nuestro es un juego de terminal, donde se puede escribir tanto una palabra entera si se quiere intentar adivinar la palabra de una, o se pueden ir mandando letras para ir jugando. 

- Antes de empezar a jugar, tenés que registrarte en el juego. Para esto, se te pedirá únicamente un nombre de usuario. Una vez registrado, podrás comenzar a jugar. 
- Luego de haberte registrado, la próxima vez que quieras jugar, se te pedirá que ingreses tu nombre de usuario. 
- Las dificultades son: Fácil, Media y Difícil. La diferencia entre estas se encuentra en la cantidad de intentos que tenés para adivinar la palabra y la dificultad de la palabra en sí. La dificultad por default es Media, y si deseas, la podes cambiar desde la opción correspondiente en el menú principal.
- Inicialmente, vas a comenzar con un puntaje y una cantidad de pistas de 0. A medida que vayas jugando, tu puntaje se modificará de la siguiente forma, de acuerdo a la dificultad:
       - Fácil: Se te sumarán 5 puntos por partida ganada, y se te restarán 20 puntos por partida perdida.
       - Media: Se te sumarán 10 puntos por partida ganada, y se te restarán 10 puntos por partida perdida.
       - Difícil: Se te sumarán 20 puntos por partida ganada, y se te restarán 5 puntos por partida perdida.
- El juego tiene dos tipos de pistas:
       - pistas simples: revelan una letra de la palabra, y tienen un costo de 2 puntos.
       - pistas bonus: arrojan una breve descripcion de la palabra, y tienen un costo de 10 puntos.

Las pistas se pueden comprar desde el menú principal o mientras se está jugando la partida mediante las opciones disponibles en la interfaz correspondiente.

- Al iniciar el juego se elige una palabra aleatoria que está oculta, tu objetivo es intentar adivinarla antes de que se complete el ahorcado. 
- Para adivinar la palabra se puede ingresar de a una letra o la palabra completa.
       - Si se elige la palabra completa y se acierta, ganás el juego!
       - Si se elige la palabra completa y no se acierta, perdés un intento
       - Si se elige una letra que está en la palabra, se revelan todas las ocurrencias de esa letra en la palabra.
       - Si se elige una letra que no está en la palabra, se pierde un intento

- Cada vez que se pierde un intento, se agrega una parte al ahorcado. Si te quedás sin intentos, se completa el ahorcado y pierdes el juego.
- Si logras adivinar la palabra antes de que se complete el ahorcado, ganas el juego!
- A lo largo del juego, tus estadisticas como usuario (puntos acumulados y pistas compradas) se irán actualizando, y podrás verlas desde el menú principal. Estas estadisticas se guardan en tu sesión y se cargan cada vez que se inicia el juego.

## Ejecucion del juego

1. Para conseguir el codigo del juego se puede:

       a. Clonar el repositorio localmente usando: git clone https://github.com/tu-nombre-de-usuario/hangman.git

       b. Descargar el zip directamente desde el repo

2. Como el juego está hecho con Python va a ser necesario que tengas Python descargado, se puede descargar desde acá: https://www.python.org/downloads/
3. Se va a tener que agregar Python a la variable de entorno PATH, en este link se explica como hacerlo: https://realpython.com/add-python-to-path/
4. Antes de comenzar a jugar, se deben instalar las dependencias del proyecto. Para esto, abrir la terminal y ejecutar: `python <path-a-dependencies.py>/dependencies.py`
5. Finalmente, para ejecutar el juego, abrir la terminal y ejecutar: `python <path-a-main.py>/main.py`

## Miembros del grupo
- Alan Valdevenito
- Bruno Ortielli
- Juan Francisco Gulden
- Brayan Ricaldi
- Iñaki Llorens
