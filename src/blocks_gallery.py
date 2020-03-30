import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# Mostramos toda la galería de bloques disponible
# No todos se reflejan en mcpi.block

# Nombre del jugador que va a construir las cosas
BUILDER_NAME = "ElasticExplorer"

# Datos del servidor de Minecraft
MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Construyendo cubos")

# Buscamos la posición en el mundo de nuestro jugador
# Esto sólo vale en singleplayer
# p = mc.player.getTilePos()

p = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

# Coordenadas del jugador en las que se crea el bloque
# Nos separamos de donde estamos para no quedarnos dentro
init_x = p.x + 1
init_y = p.y
init_z = p.z


# Probamos a poner todos los tipos de bloques en línea
MAX_BLOCK_NUMBER = 247

for i in range(1, MAX_BLOCK_NUMBER):
    mc.setBlock(init_x, init_y, init_z + i, block.Block(i))

REDSTONE = block.Block(55)  # Not included officially
SIGN = block.Block(63)

# Salimos del programa
sys.exit(0)
