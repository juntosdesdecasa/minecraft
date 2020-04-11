import sys

from mcpi import block
from mcpi.minecraft import Minecraft

import mcpython.block

# El objetivo de este tutorial es aprender a trabajar
# con la pieza mínima: un bloque

# Nombre del jugador que va a construir las cosas
BUILDER_NAME = "ElasticExplorer"

# Datos del servidor de Minecraft
MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711

# Nos conectamos al servidor de Minecraft
mc = Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)
mc.postToChat("Construyendo cubos")

# Buscamos la posición en el mundo de nuestro jugador
# Esto sólo vale en singleplayer
# p = mc.player.getTilePos()

pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

block = mcpython.block.Block(block.BRICK_BLOCK, pos, mc)

block.build()

sys.exit(0)
