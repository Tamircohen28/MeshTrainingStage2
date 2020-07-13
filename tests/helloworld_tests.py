from helloworld.messages import Header

G_OPCODE_VAL = 0x00
G_BODY_LEN = 4


def get_header():
    return bytes(Header(opcode=G_OPCODE_VAL, body_len=G_BODY_LEN))


def test_answer():
    msg = Header.from_bytes(get_header())
    assert msg.opcode == G_OPCODE_VAL
    assert msg.body_len == G_BODY_LEN

