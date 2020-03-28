import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# El objetivo de este tutorial es aprender a constuir una aldea con casas

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
# Tiene que ser mayor que 3
HOUSE_HEIGHT = 3
# Tiene que ser mayor que 4
HOUSE_WIDTH = 10
# Espacio entre las casas
HOUSE_SPACE = 3

HOUSE_BLOCK = block.WOOD
HOUSES_NUMBER = 10

WALL_BLOCK = block.STONE
WALL_HEIGHT = HOUSE_HEIGHT + 2
WALL_SPACE = 10


CLEAN = False

if CLEAN:
    HOUSE_BLOCK = block.AIR
    WALL_BLOCK = block.AIR

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
    # Las casas van en horizontal según el eje z
    init_z = init_z + (HOUSE_WIDTH + HOUSE_SPACE)

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

# Create a wall around the town: 4 walls are needed

# The height is the same always
wall_init_y = p.y
wall_final_y = p.y + WALL_HEIGHT

# First wall
wall1_init_x = p.x + HOUSE_WIDTH/1.5 - WALL_SPACE
wall1_init_z = p.z - HOUSE_WIDTH/2 + WALL_SPACE
wall1_final_z = wall1_init_z + (HOUSES_NUMBER - 1) * (HOUSE_WIDTH + HOUSE_SPACE) + 2 * WALL_SPACE

mc.setBlocks(wall1_init_x, wall_init_y, wall1_init_z,
             wall1_init_x, wall_final_y, wall1_final_z,
             WALL_BLOCK)

# Second wall
wall2_init_x = wall1_init_x
wall2_final_x = wall1_init_x + HOUSE_WIDTH + 2 * WALL_SPACE
wall2_init_z = wall1_final_z

mc.setBlocks(wall2_init_x, wall_init_y, wall2_init_z,
             wall2_final_x, wall_final_y, wall2_init_z,
             WALL_BLOCK)

# Third wall
wall3_init_x = wall2_final_x
wall3_init_z = wall2_init_z
wall3_final_z = wall3_init_z - (HOUSES_NUMBER - 1) * (HOUSE_WIDTH + HOUSE_SPACE) - 2 * WALL_SPACE

mc.setBlocks(wall3_init_x, wall_init_y, wall3_init_z,
             wall3_init_x, wall_final_y, wall3_final_z,
             WALL_BLOCK)

# Fourth wall
wall4_init_x = wall3_init_x
wall4_final_x = wall4_init_x - HOUSE_WIDTH - 2 * WALL_SPACE
wall4_init_z = wall3_final_z

mc.setBlocks(wall4_init_x, wall_init_y, wall4_init_z,
             wall4_final_x, wall_final_y, wall4_init_z,
             WALL_BLOCK)


sys.exit(0)
