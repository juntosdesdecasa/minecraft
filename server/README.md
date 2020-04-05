# Servidor de Minecraft Spigot dockerizado y vitaminado
Esta carpeta incluye todos los artefactos necesarios para levantar un **servidor de Minecraft Spigot**, **accessible desde Internet** y **programable con Python**.
La única dependencia para hacerlo funcionar es Docker, además de la herramienta `docker-compose` para levantar varios contenedores de manera sencilla.

Toda la funcionalidad está encapsulada en dos imágenes Docker:

1. **spigotngrok.-** contiene el servidor Spigot, con el plugin `raspberryjuice-1.11.jar` y el servicio [ngrok](https://ngrok.com/) instalado para crear un tunel TCP para que los usuarios se puedan conectar desde cualquier parte de Internet.
2. **mcjupyter.-** contiene [Jupyter](https://jupyter.org/) y la biblioteca Python [mcpi](https://github.com/martinohanlon/mcpi) para interaccionar con nuestro servidor de Minecraft.
## Instrucciones para hacerlo funcionar en tu red local
Asegúrate que tu máquina tiene una versión reciente de [Docker](https://www.docker.com/), además de la herramienta `docker-compose`. Con estos prerrequisitos satisfechos, lleva a cabo los siguientes pasos:
1. Descarga el contenido de este directorio o haz un clonado del repositorio, y entra dentro del directorio server:
   ```
   $ cd server
   ```
2. Crea una variable de entorno que se llame MINECRAFTSRV_PATH que apunte a ese directorio en el que estás:
   ```
   $ export MINECRAFTSRV_PATH=`pwd`
   ```
3. Crea los contenedores para levantar todos los servicios que vamos a utilizar. La primera vez que lo hagas tardará un poco más porque personalizará las imágenes que hemos utilizado como base:
   ```
   $ docker-compose up -d
   ```
4. Si todo va bien, deberías ver las siguientes líneas al cabo de unos minutos:
   ```
   ...
   Creating server_mcjupyter_1 ... done
   Creating server_minecraft_1 ... done
   ```
5. Esto quiere decir que el contenedor con el servidor de Minecraft vitaminado (`server_minecraft_1`) y la herramienta Jupyter para interactuar con el servidor vía Python (`server_jupyter_1`) ya están arrancando. A continuación debemos asegurarnos de que ambos contenedores han arrancado correctamente, para ello usaremos los siguientes comandos y comprobaremos que obtenemos una salida similar a la que se incluye aquí:
   ```
   $ docker logs server_minecraft_1
   ...
   [15:11:23 INFO]: Loaded 441 spawn chunks for world world_the_end
   [15:11:23 INFO]: Time elapsed: 3044 ms
   [15:11:23 INFO]: [RaspberryJuice] Enabling RaspberryJuice v1.11*
   [15:11:23 INFO]: [RaspberryJuice] Using port 4711
   [15:11:23 INFO]: [RaspberryJuice] Using RELATIVE locations
   [15:11:23 INFO]: [RaspberryJuice] Using RIGHT clicks for hits
   [15:11:23 INFO]: [RaspberryJuice] ThreadListener Started
   [15:11:23 INFO]: Done (55.834s)! For help, type "help"
   [15:11:23 INFO]: Timings Reset
   --
   $ docker logs server_mcjupyter_1
   Executing the command: jupyter notebook
   [I 15:10:16.286 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
   [W 15:10:16.466 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
   [I 15:10:16.899 NotebookApp] JupyterLab extension loaded from /opt/conda/lib/python3.7/site-packages/jupyterlab
   [I 15:10:16.900 NotebookApp] JupyterLab application directory is /opt/conda/share/jupyter/lab
   [I 15:10:16.903 NotebookApp] Serving notebooks from local directory: /home/jovyan/work
   [I 15:10:16.903 NotebookApp] The Jupyter Notebook is running at:
   [I 15:10:16.903 NotebookApp] http://0ec7d3014376:8888/
   [I 15:10:16.904 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
   ```

Si consigues llevar a cabo estos pasos de manera satisfactoria, ya tendrás tu servidor de Minecraft vitaminado y programable con Python en tu entorno local:

* El servidor de Minecraft está mapeado al **puerto TCP 25565** de la máquina donde se haya creado el contenedor, y el **puerto TCP 4711** para interaccionar con el servidor con Python.
* La herramienta Jupyter para facilitar la tarea de escritura de código Python está disponible en el **puerto TCP 8888** de la máquina donde se creó el contenedor. Jupyter es una herramienta web, por lo que podrás acceder a ella mediante tu navegador favorito especificando la URL correspondiente (ej. http://localhost:8888 si están en la misma máquina donde se creó el contenedor). La **contraseña para acceder** a esta herramienta es **hola123**.

## Juega con otros jugadores aunque no estén en tu red local
Como comentaba antes, la imagen que tiene el servidor de Minecraft vitaminado tiene un binario asociado al servicio [ngrok](https://ngrok.com/) que se encarga de crear túneles de comunicaciones que permitan a usuarios de Internet conectarse a equipos que están en redes privadas, como la que probablemente tengas en tu casa. Para crear este túnel y conectarlo con tu servidor de Minecraft vitaminado, tendrás que seguir estos pasos:

1. Créate una cuenta gratuita en ngrok para obtener tu token de autenticación. Los pasos para configurar el tunel se especifican en la URL [https://dashboard.ngrok.com/get-started](https://dashboard.ngrok.com/get-started) una vez que has creado tu usuario.
2. Una vez identificado tu token, debes ejecutar el siguiente comando en la línea de comandos donde habías creado previamente los contenedores para proporcionar tu token al servidor de Minecraft:
   ```
   $ docker exec server_minecraft_1 /opt/ngrok/ngrok authtoken <pon tu token aquí>
   Authtoken saved to configuration file: /opt/minecraft/.ngrok2/ngrok.yml
   ```
3. Inicia el tunel con el siguiente comando:
   ```
   $ docker exec server_minecraft_1 /opt/ngrok/ngrok tcp 25565&
   [1] 2658
   ```
4. Pregúntale al contenedor cuál es la dirección que tienen que utilizar los usuarios de Internet para entrar a tu nuevo servidor de Minecraft vitaminado:
   ```
   $ docker exec server_minecraft_1 python /opt/ngrok/minecraft_url.py
     % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                    Dload  Upload   Total   Spent    Left  Speed
   100   388  100   388    0     0   189k      0 --:--:-- --:--:-- --:--:--  189k
   Tu servidor de minecraft es accesible en esta direccion: **0.tcp.ngrok.io:14386**
   ```

Corre y dile a tus amigos que tu servidor de Minecraft vitaminado está listo para que se unan a la fiesta utilizando el servidor **0.tcp.ngrok.io:14386**.


