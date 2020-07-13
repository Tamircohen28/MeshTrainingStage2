from hydration import *


class Header(Struct):
    opcode = UInt8
    body_len = UInt16


class BodyPing(Struct):
    magic = UInt32(value=0xDEADBEEF)


class BodyCard(Struct):
    value = UInt8(value=0x02)
    suit = UInt8(value=0x03)


class BodyTest(Struct):
    Hand1 = [BodyCard() for i in range(5)]
    Hand2 = [BodyCard() for j in range(5)]


class BodyTestResult(Struct):
    result = UInt8


if __name__ == '__main__':
    msg = Header() / BodyCard()
    print(bytes(msg))
