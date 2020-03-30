import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# El objetivo de este tutorial es aprender a trabajar
# con la pieza mínima: un bloque

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

block_type = block.BRICK_BLOCK
# block_type = block.AIR
blocks_number = 5

# Creamos una línea en x crecientes
for x in range(1, blocks_number):
    mc.setBlock(init_x+x, init_y, init_z, block_type)

# Creamos una línea en x decrecientes
for x in range(1, blocks_number):
    mc.setBlock(init_x-x, init_y, init_z, block_type)

# Creamos una línea en y crecientes
for y in range(1, blocks_number):
    mc.setBlock(init_x, init_y + y, init_z, block_type)

# Creamos una línea en y decrecientes
for y in range(1, blocks_number):
    mc.setBlock(init_x, init_y - y, init_z, block_type)

# Creamos una línea en z crecientes
for z in range(1, blocks_number):
    mc.setBlock(init_x, init_y, init_z + z, block_type)

# Creamos una línea en z decrecientes
for z in range(1, blocks_number):
    mc.setBlock(init_x, init_y, init_z - z, block_type)


# Salimos del programa
sys.exit(0)
