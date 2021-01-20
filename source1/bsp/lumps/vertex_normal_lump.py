import numpy as np

from .. import Lump, lump_tag


@lump_tag(30, 'LUMP_VERTNORMALS')
class VertexNormalLump(Lump):
    def __init__(self, bsp, lump_id):
        super().__init__(bsp, lump_id)
        self.normals = np.array([])

    def parse(self):
        reader = self.reader
        self.normals = np.frombuffer(reader.read(self._lump.size), np.float32, self._lump.size // 4)
        self.normals = self.normals.reshape((-1, 3))
        return self


@lump_tag(31, 'LUMP_VERTNORMALINDICES')
class VertexNormalIndicesLump(Lump):
    def __init__(self, bsp, lump_id):
        super().__init__(bsp, lump_id)
        self.indices = np.array([])

    def parse(self):
        reader = self.reader
        self.indices = np.frombuffer(reader.read(self._lump.size), np.int16, self._lump.size // 2)
        return self
