import sys

import mcpi.block
import mcpi.minecraft

from mcpython.blocks_gallery import BlocksGallery

BUILDER_NAME = "ElasticExplorer"

MC_SEVER_HOST = "localhost"
MC_SEVER_PORT = 4711


def main():
    try:
        mc = mcpi.minecraft.Minecraft.create(address=MC_SEVER_HOST, port=MC_SEVER_PORT)

        mc.postToChat("Construyendo todos los bloques posibles")
        pos = mc.entity.getTilePos(mc.getPlayerEntityId(BUILDER_NAME))

        blocks = BlocksGallery(mcpi.block.BRICK_BLOCK, pos, mc)
        blocks.build()

    except mcpi.connection.RequestError:
        print("Can't connect to Minecraft server " + MC_SEVER_HOST)


if __name__ == "__main__":
    main()
    sys.exit(0)
