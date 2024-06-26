from dataclasses import dataclass

from SourceIO.library.shared.types import Vector3
from SourceIO.library.utils import Buffer


@dataclass(slots=True)
class StudioBone:
    parent: int
    flags: int
    pos: Vector3[float]

    @classmethod
    def from_buffer(cls, buffer: Buffer):
        return cls(buffer.read_int32(), buffer.read_int32(), buffer.read_fmt('3f'))
