# Servidor de Minecraft Spigot dockerizado y vitaminado
Esta carpeta incluye todos los artefactos necesarios para levantar un **servidor de Minecraft Spigot**, **accessible desde Internet** y **programable con Python**.
La única dependencia para hacerlo funcionar es Docker, además de la herramienta `docker-compose` para levantar varios contenedores de manera sencilla.

Toda la funcionalidad está encapsulada en dos imágenes Docker:

1. **spigotngrok.-** contiene el servidor Spigot, con el plugin `raspberryjuice-1.11.jar` y el servicio [ngrok](https://ngrok.com/) instalado para crear un tunel TCP para que los usuarios se puedan conectar desde cualquier parte de Internet.
2. **mcjupyter.-** contiene [Jupyter](https://jupyter.org/) y la biblioteca Python [mcpi](https://github.com/martinohanlon/mcpi) para interaccionar con nuestro servidor de Minecraft.

## [Linux] Instrucciones para hacerlo funcionar en tu red local si usas Linux para tu servidor
Asegúrate que tu máquina tiene una versión reciente de [Docker](https://www.docker.com/), además de la herramienta `docker-compose`. Con estos prerrequisitos satisfechos, lleva a cabo los siguientes pasos:
1. Descarga el contenido de este directorio o haz un clonado del repositorio, entra dentro del directorio `server` e identifica la ruta absoluta donde te encuentras:
   ```
   $ cd server
   $ pwd
   /home/rmarin/Documents/repos/minecraft/server
   ```
2. Dentro del directorio `bin` verás un fichero llamado `server-linux.sh`. Utiliza un editor de texto para editar este fichero y asignar la ruta absoluta que descubrimos en el punto anterior a la variable de entorno MINECRAFTSRV_PATH:
   ```
   #!/bin/bash
   
   MINECRAFTSRV_PATH=/home/rmarin/Documents/repos/minecraft/server
   ```
3. Utiliza el script de administración del servidor `server-linux.sh` para arrancar y parar tu servidor a voluntad:
   ```
   $ bin/server-linux.sh 
   Bienvenido al script para administrar tu servidor de Minecraft dockerizado y vitaminado
   Uso: bin/server-linux.sh {start|stop|status|ngrok-setup|ngrok-status}
   ```

### Arranca tu servidor de Minecraft dockerizado y vitaminado
Para arrancar tu servidor tienes que pasar el parámetro `start` al script de administración del servidor. La primera vez que lo hagas, el proceso tardará un poco más de lo habitual porque tiene que construir las imágenes, después todo será mucho más rápido:
   ```
   $ bin/server-linux.sh start
   Comprobando variable de entorno MINECRAFTSRV_PATH...
      MINECRAFTSRV_PATH apunta a /home/rmarin/Documents/repos/minecraft/server
   Comprobando variable de entorno NGROK_AUTHTOKEN...
   Comprobando existencia de directorios... 
      Creando directorio etc
      Creando directorio log
      Creando directorio data/spigot/worlds 
      Creando directorio data/spigot/data
   Iniciando tu servidor de Minecraft dockerizado y vitaminado...
   Creating network "server_default" with the default driver
   Creating server_mcjupyter_1 ... done
   Creating server_minecraft_1 ... done
   ```

Comprueba que todo está correctamente iniciado pasando el parámetro `status` al script de administración del servidor:
   ```
   $ bin/server-linux.sh status
   Comprobando variable de entorno MINECRAFTSRV_PATH...
      MINECRAFTSRV_PATH apunta a /home/rmarin/Documents/repos/minecraft/server
   Comprobando variable de entorno NGROK_AUTHTOKEN...
          Name                    Command                 State                            Ports                      
   -------------------------------------------------------------------------------------------------------------------
   server_mcjupyter_1   tini -g -- start-notebook.sh   Up             0.0.0.0:8888->8888/tcp                          
   server_minecraft_1   ./docker-entrypoint.sh serve   Up (healthy)   0.0.0.0:25565->25565/tcp, 0.0.0.0:4711->4711/tcp
   ```

Si consigues una salida similar a esta, ya tendrás tu servidor de Minecraft vitaminado y programable con Python en tu entorno local:

* El servidor de Minecraft está mapeado al **puerto TCP 25565** de la máquina donde se haya creado el contenedor, y el **puerto TCP 4711** para interaccionar con el servidor con Python.
* La herramienta Jupyter para facilitar la tarea de escritura de código Python está disponible en el **puerto TCP 8888** de la máquina donde se creó el contenedor. Jupyter es una herramienta web, por lo que podrás acceder a ella mediante tu navegador favorito especificando la URL correspondiente (ej. http://localhost:8888 si están en la misma máquina donde se creó el contenedor). La **contraseña para acceder** a esta herramienta es **hola123**.

### Finaliza tu servidor de Minecraft dockerizado y vitaminado
Una vez que hayáis terminado de jugar, es recomendable que finalices tu servidor hasta el proximo día que reanudéis la partida. Para ello sólo tienes que pasar el parámetro `stop` al script the adminitración del servidor:
   ```
   $ bin/server-linux.sh stop
   Comprobando variable de entorno MINECRAFTSRV_PATH...
      MINECRAFTSRV_PATH apunta a /home/rmarin/Documents/repos/minecraft/server
   Comprobando variable de entorno NGROK_AUTHTOKEN...
   Parando tu servidor de Minecraft dockerizado y vitaminado...
   Stopping server_mcjupyter_1 ... done
   Stopping server_minecraft_1 ... done
   Removing server_mcjupyter_1 ... done
   Removing server_minecraft_1 ... done
   Removing network server_default
   ```
### Juega con otros jugadores aunque no estén en tu red local
Como comentaba antes, la imagen que tiene el servidor de Minecraft vitaminado tiene un binario asociado al servicio [ngrok](https://ngrok.com/) que se encarga de crear túneles de comunicaciones que permitan a usuarios de Internet conectarse a equipos que están en redes privadas, como la que probablemente tengas en tu casa. Para crear este túnel y conectarlo con tu servidor de Minecraft vitaminado, tendrás que seguir estos pasos:

1. Créate una cuenta gratuita en ngrok para obtener tu token de autenticación. Los pasos para configurar el tunel se especifican en la URL [https://dashboard.ngrok.com/get-started](https://dashboard.ngrok.com/get-started) una vez que has creado tu usuario.
2. Una vez identificado tu token, deberás editar de nuevo el script de administración del servidor para guardar el token y que se utilice cuando sea necesario:
   ```
   #!/bin/bash

   MINECRAFTSRV_PATH=/home/rmarin/Documents/repos/minecraft/server
   NGROK_AUTHTOKEN=1VeVCFYFgnwSeaie1zYW5RqrfK6_6EAF8L2svnoBiTgrLURpM
   ```
   **NOTA:** El token del ejemplo no es válido y lo tendrás que reemplazar por el tuyo.
3. Ya podemos utilizar el script de administración del servidor para configurar nuestra cuenta de ngrok. El parámetro `ngrok-setup` hará las configuraciones oportunas e iniciará el tunel:
   ```
   $ bin/server-linux.sh ngrok-setup
   Configurando tu cuenta ngrok para publicar tu servidor...
   Comprobando variable de entorno NGROK_AUTHTOKEN...
   Authtoken saved to configuration file: /opt/minecraft/.ngrok2/ngrok.yml
   ```
4. Comprueba cuál es la dirección pública para acceder a tu servidor de Minecraft utilizando el parámetro `ngrok-status` del script de administración del servidor:
   ```
   $ bin/server-linux.sh ngrok-status
   Este es el estado de ngrok...
   Comprobando variable de entorno NGROK_AUTHTOKEN...
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
   100   388  100   388    0     0   378k      0 --:--:-- --:--:-- --:--:--  378k
   Tu servidor de minecraft es accesible en esta direccion: 0.tcp.ngrok.io:17069
   ```

Corre y dile a tus amigos que tu servidor de Minecraft vitaminado está listo para que se unan a la fiesta utilizando el servidor **0.tcp.ngrok.io:17069**.
