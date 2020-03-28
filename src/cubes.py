import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# El objetivo de este tutorial es aprender a trabajar
# con cubos en Minecraft con el objetivo de hacer casas


MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
CUBE_HEIGHT = 20
CUBE_BLOCK = block.BRICK_BLOCK

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Construyendo cubos")

# Buscamos la posición en el mundo de nuestro jugador
p = mc.player.getTilePos()

# El cubo lo hacemos delante del jugador
init_x = p.x + 1
init_y = p.y
init_z = p.z

mc.setBlocks(init_x,               init_y,               init_z,
             init_x + CUBE_HEIGHT, init_y + CUBE_HEIGHT, init_z + CUBE_HEIGHT,
             CUBE_BLOCK)

# Y lo rellenamos de aire para que pueda ser una casa
# El grosor de las paredes podemos regularlo
WALL_WIDTH = 1
mc.setBlocks(init_x + WALL_WIDTH,               init_y + WALL_WIDTH,               init_z + WALL_WIDTH,
             init_x + CUBE_HEIGHT - WALL_WIDTH, init_y + CUBE_HEIGHT - WALL_WIDTH, init_z + CUBE_HEIGHT - WALL_WIDTH,
             block.AIR)


sys.exit(0)
