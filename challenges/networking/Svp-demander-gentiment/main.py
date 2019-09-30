import socket
import logging
import threading


class ClientThread(threading.Thread):

    def __init__(self, log, ip, port, clientsocket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        log.info(f"New thread for {self.ip}:{self.port}")

    def run(self):
        client.send(b"Salut que veux-tu? :) \n\n")
        response = client.recv(5000)
        if len(response) > 0:
            if response.startswith(bytes(key.lower(), "utf-8")):
                log.info("Bonne réponse donnée")
                client.send(b"Merci de demander gentiment, voici le drapeau: FLAG-SoisPoliMemeSiTuEsJoli\n")
                client.close()
            else:
                client.send(b"Quoi? je ne comprend que les gens polis.\n")
                client.close()
                log.info(f"Mauvaise réponse donnée: {response}")


if __name__ == '__main__':
    log = logging.getLogger("main")
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    log.info("Starting app")
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    log.info("Socket created")
    port = 42000
    listener.bind(('0.0.0.0', port))
    log.info(f"Socket bound to {port}")
    key = "S'il-vous-plait Monsieur le serveur j'aimerais obtenir le drapeau.".lower()
    threads = []
    while True:
        listener.listen(30)
        log.info("Socket listening")
        client, address = listener.accept()
        log.info(f"Client connected {client} {address}")
        thread = ClientThread(log, address[0], address[1], client)
        threads.append(thread)
        thread.run()

