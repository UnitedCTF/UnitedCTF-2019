import socketserver
from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes

from flag import FLAG


def get_flag(req):
    global key

    req.sendall(b"Send ciphertext as number:\n")

    try:
        ciphertext = req.recv(1024).decode().strip()
        ciphertext = int(ciphertext)
        plaintext = pow(ciphertext, key.d, key.n)
        plaintext = long_to_bytes(plaintext)
        plaintext = plaintext.decode()

        if plaintext == "I want the flag :)":
            req.sendall(FLAG.encode() + b"\n")
            return
    except:
        pass

    req.sendall(b"Wrong :S\n")


def encrypt(req):
    global key

    req.sendall(b"Send string to encrypt:\n")
    plaintext = req.recv(1024).decode().strip()

    if plaintext == "I want the flag :)":
        req.sendall(b"I can't encrypt that ;)\n")
        return

    ciphertext = pow(bytes_to_long(plaintext.encode()), key.e, key.n)
    req.sendall(b"%d\n" % ciphertext)


def main(req):
    global key

    while True:
        req.sendall(b"""================================
1. Get the flag
2. Encrypt something (e = %d)
3. Exit
>  Your choice:
""" % key.e)

        choice = req.recv(1024).decode().strip()

        if choice == "1":
            get_flag(req)
        elif choice == "2":
            encrypt(req)
        elif choice == "3":
            return


class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
        main(self.request)


if __name__ == '__main__':
    with open("key", "r") as f:
        key = RSA.importKey(f.read())

    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 3000), TaskHandler)
    server.serve_forever()