# Proyecto de AnInfo: Ahorcado

## Reglas de Juego

Bienvenidos al Ahorcado! En nuestro proyecto intentamos recrear el clásico juego, desde nuestro propio punto de vista. El nuestro es un juego de terminal, donde se puede escribir tanto una palabra entera si se quiere intentar adivinar la palabra de una, o se pueden ir mandando letras para ir jugando. 

- Antes de empezar a jugar, tenés que registrarte en el juego. Para esto, se te pedirá únicamente un nombre de usuario. Una vez registrado, podrás comenzar a jugar. 
- Luego de haberte registrado, la próxima vez que quieras jugar, se te pedirá que ingreses tu nombre de usuario. 
- Las dificultades son: Fácil, Media y Difícil. La principal diferencia entre estas se encuentra en la cantidad de intentos que tenés para adivinar la palabra/frase y la dificultad de la palabra/frase en sí. La dificultad por default es Media, y si deseas, la podes cambiar desde la opción correspondiente en el menú principal.
- Inicialmente, vas a comenzar con un puntaje y una cantidad de pistas de 0. A medida que vayas jugando, tu puntaje se modificará de la siguiente forma, de acuerdo a la dificultad:
       - Fácil: Se te sumarán 5 puntos por partida ganada, y se te restarán 20 puntos por partida perdida.
       - Media: Se te sumarán 10 puntos por partida ganada, y se te restarán 10 puntos por partida perdida.
       - Difícil: Se te sumarán 20 puntos por partida ganada, y se te restarán 5 puntos por partida perdida.

Cabe aclarar que el puntaje nunca puede ser menor a 0.
- El juego tiene dos tipos de pistas:
       - pistas simples: revelan una letra de la palabra, y tienen un costo de 2 puntos.
       - pistas bonus: arrojan una breve descripcion de la palabra, y tienen un costo de 10 puntos.

Las pistas se pueden comprar desde el menú principal o mientras se está jugando la partida mediante las opciones disponibles en la interfaz correspondiente.

- Al iniciar el juego se elige una palabra aleatoria que está oculta, tu objetivo es intentar adivinarla antes de que se complete el ahorcado. 
- Para adivinar la palabra/frase se puede ingresar de a una letra o la palabra/frase completa.
       - Si se elige la palabra/frase completa y se acierta, ganás el juego!
       - Si se elige la palabra/frase completa y no se acierta, perdés un intento
       - Si se elige una letra que está en la palabra/frase, se revelan todas las ocurrencias de esa letra en la palabra/frase.
       - Si se elige una letra que no está en la palabra/frase, se pierde un intento

- Cada vez que se pierde un intento, se agrega una parte al ahorcado. Si te quedás sin intentos, se completa el ahorcado y pierdes el juego.
- Si logras adivinar la palabra/frase antes de que se complete el ahorcado, ganas el juego!
- A lo largo del juego, tus estadisticas como usuario (puntos acumulados y pistas compradas) se irán actualizando, y podrás verlas desde el menú principal. Estas estadisticas se guardan en tu sesión y se cargan cada vez que se inicia el juego.

## Ejecucion del juego (Windows)

1. Para conseguir el codigo del juego se puede:

       a. Clonar el repositorio localmente usando:
          ~$ git clone https://github.com/Brubrux/Proyecto-AnInfo-

       b. Descargar el zip directamente desde el repo

3. Como el juego está hecho con Python va a ser necesario que tengas Python descargado, se puede descargar desde acá: https://www.python.org/downloads/
4. Se va a tener que agregar Python a la variable de entorno PATH, en este link se explica como hacerlo: https://realpython.com/add-python-to-path/
5. Antes de comenzar a jugar, se deben instalar las dependencias del proyecto. Para esto, abrir la terminal y ejecutar:
   ```
   ~$ python <path-a-dependencies.py>/dependencies.py
   ```
6. Finalmente, para ejecutar el juego, abrir la terminal y ejecutar:
   ```
   ~$ python <path-a-main.py>/main.py
   ```

## Ejecucion del juego (Ubuntu)

1. Para conseguir el código, idem ejecución en Windows
2. Descarga de Python:
   ```
   ~$ sudo apt update
   ~$ sudo apt install python3
   ```
4. Agregado de Python a la variable de entorno PATH
   ```
   ~$ cd ~
   ~$ ls -a
   ```
   Buscar un archivo con alguno de estos nombres: .profile, .bash_profile, .bash_login, .zprofile, .zlogin, en caso de ubuntu, .profile
   ```
   ~$ cat .profile
   ```
   Asegurarse de que se encuentre la siguiente sección
   ```
   # set PATH so it includes user's private bin if it exists
   if [ -d "$HOME/.local/bin" ] ; then
   PATH="$HOME/.local/bin:$PATH"
   fi
   export PATH=<ruta al binario de python>/python
   ```
6. Instalar dependencias del proyecto
   ```
   ~$ python3 <ruta a raiz del proyecto>/dependencies.py
   ```
8. Ejecución del juego
   ```
   ~$ python3 <ruta a raiz del proyecto>/main.py
   ```


## Miembros del grupo
- Alan Valdevenito
- Bruno Ortielli
- Juan Francisco Gulden
- Brayan Ricaldi
- Iñaki Llorens
