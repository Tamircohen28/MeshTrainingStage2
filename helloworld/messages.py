from hydration import *


class Header(Struct):
    opcode = UInt8(value=0x00)
    body_len = UInt16(value=4)


class BodyPing(Struct):
    magic = UInt32(value=0xDEADBEEF)
