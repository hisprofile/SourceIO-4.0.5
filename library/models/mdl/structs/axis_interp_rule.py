from dataclasses import dataclass


from SourceIO.library.shared.types import Vector3, Vector4
from SourceIO.library.utils import Buffer


@dataclass(slots=True)
class AxisInterpRule:
    control: int
    pos: tuple[Vector3[float], ...]
    quat: tuple[Vector4[float], ...]

    @classmethod
    def from_buffer(cls, buffer: Buffer):
        control = buffer.read_uint32()
        pos = tuple(buffer.read_fmt('3f') for _ in range(6))
        quat = tuple(buffer.read_fmt('4f') for _ in range(6))
        return cls(control, pos, quat)
