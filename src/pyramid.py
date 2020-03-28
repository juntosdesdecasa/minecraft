import sys

from mcpi import block
from mcpi.minecraft import Minecraft

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
PYRAMID_HEIGHT = 10
PYRAMID_BLOCK = block.SAND

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Building a Pyramid of " + str(PYRAMID_HEIGHT) + " height!")

# Buscamos la posición en el mundo de nuestro jugador
p = mc.player.getTilePos()

# La pirámide la hacemos delante del jugador
init_x = p.x + 1
init_y = p.y
init_z = p.z

# La longitud (x) y la anchura (z) siempre son iguales
# La relación entre la altura y la longitud/anchura es Longitud/Anchura = 2 * Altura - 1
length = 2 * PYRAMID_HEIGHT - 1
width = 2 * PYRAMID_HEIGHT - 1

# Dibujamos la pirámide por niveles hasta llegar a 1 bloque en la altura final
for i in range(0, PYRAMID_HEIGHT):
    level = i
    mc.setBlocks(init_x + level,              init_y + level, init_z + level,
                 init_x + (length-1) - level, init_y + level, init_z + (width-1) - level,
                 block.SAND)

# TODO: Movemos al jugador a la cima de la pirámide
sys.exit(0)
