import sys

from mcpi import block
from mcpi.minecraft import Minecraft


# El objetivo de este tutorial es construir una gran muralla

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "javierete.com"
MC_SEVER_PORT = 8711
WALL_HEIGHT = 10
WALL_LENGTH = 1000
WALL_WIDTH = 3

WALL_BLOCK = block.IRON_BLOCK

CLEAN = False

if CLEAN:
    WALL_BLOCK = block.AIR

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Construyendo la gran muralla de longitud %s altura %s y anchura %s" %
              (str(WALL_LENGTH), str(WALL_HEIGHT), str(WALL_WIDTH)))

# Buscamos la posición en el mundo de nuestro jugador
# Esto sólo vale en singleplayer
# p = mc.player.getTilePos()
p = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

# La muralla la hacemos delante del jugador
init_x = p.x + 1
init_y = p.y
init_z = p.z

mc.setBlocks(init_x,                 init_y,                 init_z,
             init_x + WALL_LENGTH-1, init_y + WALL_HEIGHT-1, init_z + WALL_WIDTH-1,
             WALL_BLOCK)


sys.exit(0)
