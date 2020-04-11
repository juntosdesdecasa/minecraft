from .object import Object


class Block(Object):
    """ Base class for all objects in mcpython library """

    def build(self):
        self.server.setBlock(self.position.x+1, self.position.y,
                             self.position.z, self.block)
