#!/bin/bash

MINECRAFTSRV_PATH=/home/rmarin/Documents/repos/minecraft/server
NGROK_AUTHTOKEN=1VeVCFYFgnwSeaie1zYW5RqrfK6_6EAF8L2svnoBiTgrLURpM

check_env() {
    # 1. Se comprueba existencia de la variable de entorno MINECRAFTSRV_PATH
    echo "Comprobando variable de entorno MINECRAFTSRV_PATH..."
    if [[ -z "${MINECRAFTSRV_PATH}" ]]
    then
       echo "   ERROR: La variable de entorno MINECRAFTSRV_PATH no se ha configurado"
       exit -1
    else
       echo "   MINECRAFTSRV_PATH apunta a $MINECRAFTSRV_PATH"
       export MINECRAFTSRV_PATH
    fi
    # 2. Se comprueba existencia de la variable de entorno NGROK_AUTHTOKEN
    echo "Comprobando variable de entorno NGROK_AUTHTOKEN..."
    if [[ -z "${NGROK_AUTHTOKEN}" ]]
    then
       echo "   WARNING: La variable de entorno NGROK_AUTHTOKEN no está definida."
    fi
}

check_ngrok() {
    # 1. Se comprueba existencia de la variable de entorno NGROK_AUTHTOKEN
    echo "Comprobando variable de entorno NGROK_AUTHTOKEN..."
    if [[ -z "${NGROK_AUTHTOKEN}" ]]
    then
       echo "   ERROR: La variable de entorno NGROK_AUTHTOKEN no está definida."
       exit -1
    fi
}

check_prereq() {
    folders="etc log data/spigot/worlds data/spigot/data"

    # 1. Se comprueba existencia de la variable de entorno
    check_env
    # 2. Se comprueba estructura de directorios
    cd $MINECRAFTSRV_PATH
    echo "Comprobando existencia de directorios..."
    for folder in $folders; do
       if [ ! -d $folder ]
       then
         echo "   Creando directorio $folder"
         mkdir -p $folder
       fi
    done

}

start() {
    echo "Iniciando tu servidor de Minecraft dockerizado y vitaminado..."

    cd $MINECRAFTSRV_PATH
    docker-compose up -d
}

stop() {
    echo "Parando tu servidor de Minecraft dockerizado y vitaminado..."

    cd $MINECRAFTSRV_PATH
    docker-compose down
}

case "$1" in 
start)
   check_prereq
   start
   ;;
stop)
   check_env
   stop
   ;;
status)
   check_env

   cd $MINECRAFTSRV_PATH
   docker-compose ps
   ;;
ngrok-setup)
   echo "Configurando tu cuenta ngrok para publicar tu servidor..."
   check_ngrok

   docker exec server_minecraft_1 /opt/ngrok/ngrok authtoken $NGROK_AUTHTOKEN
   docker exec server_minecraft_1 /opt/ngrok/ngrok tcp 25565&
   ;;
ngrok-status)
   echo "Este es el estado de ngrok..."
   check_ngrok

   docker exec server_minecraft_1 python /opt/ngrok/minecraft_url.py
   ;;
*)
   echo "Bienvenido al script para administrar tu servidor de Minecraft dockerizado y vitaminado"
   echo "Uso: $0 {start|stop|status|ngrok-setup|ngrok-status}"
esac

exit 0 
