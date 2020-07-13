from helloworld.messages import *
import pytest

G_PING_OPCODE = 0x00
G_BODY_LEN = 4
G_DOCKER_IP = "192.168.99.100"
G_DOCKER_PORT = 1515


@pytest.fixture
def server_connection():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((G_DOCKER_IP, G_DOCKER_PORT))
    yield s
    s.close()


def build_msg():
    return Header(opcode=G_PING_OPCODE, body_len=G_BODY_LEN) / BodyPing()


def test_answer(server_connection):
    s = server_connection
    msg = build_msg()
    s.send(bytes(msg))
    ans = s.recv(len(bytes(msg)))

    header = Header.from_bytes(ans[:len(bytes(Header()))])
    body = BodyPing.from_bytes(ans[len(bytes(Header())):])

    assert header.opcode == G_PING_OPCODE
    assert header.body_len == G_BODY_LEN
    assert body.magic == msg[1].magic

