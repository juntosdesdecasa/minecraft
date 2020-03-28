import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# El objetivo de este tutorial es aprender a constuir una aldea con casas

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
# Tiene que ser mayor que 3
HOUSE_HEIGHT = 4
# Tiene que ser mayor que 4
HOUSE_WIDTH = 10

HOUSE_BLOCK = block.WOOD
HOUSES_NUMBER = 25

CLEAN = False

if CLEAN:
    HOUSE_BLOCK = block.AIR

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Construyendo un pueblo")

# Buscamos la posición en el mundo de nuestro jugador
# Esto sólo vale en singleplayer
# p = mc.player.getTilePos()
p = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

mc.postToChat("Origen de construcción " + str(p))

# Hacemos la aldea delante del jugador
init_x = p.x + HOUSE_WIDTH/1.5
init_y = p.y
init_z = p.z - HOUSE_WIDTH/2

WIDTH = HOUSE_WIDTH - 1
HEIGHT = HOUSE_HEIGHT - 1

for i in range(0, HOUSES_NUMBER):
    # Las casas están separadas entre si HOUSE_HEIGHT

    init_z = init_z + (HOUSE_WIDTH + HOUSE_HEIGHT)

    # Construimos el bloque principal
    mc.setBlocks(init_x,         init_y,          init_z,
                 init_x + WIDTH, init_y + HEIGHT, init_z + WIDTH,
                 HOUSE_BLOCK)

    # Y lo rellenamos de aire para que pueda ser una casa
    # El grosor de las paredes podemos regularlo
    WALL_WIDTH = 1
    mc.setBlocks(init_x + WALL_WIDTH,         init_y,                       init_z + WALL_WIDTH,
                 init_x + WIDTH - WALL_WIDTH, init_y + HEIGHT - WALL_WIDTH, init_z + WIDTH - WALL_WIDTH,
                 block.AIR)

    # Y le hacemos una puerta
    DOOR_SIZE = 1
    mc.setBlocks(init_x,     init_y,             init_z + WALL_WIDTH,
                 init_x + 1, init_y + DOOR_SIZE, init_z + DOOR_SIZE,
                 block.AIR)

sys.exit(0)
