import socket
from messages import *

if __name__ == '__main__':
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect(("192.168.99.100", 1515))

    msg = Header() / BodyPing()
    s.send(bytes(msg))

    ans = s.recv(len(bytes(msg)))
    print("Received:")
    header = Header.from_bytes(ans[:len(bytes(Header()))])
    body = BodyPing.from_bytes(ans[len(bytes(Header())):])

    print(header)
    print(body)