import socket
import threading
import sys
import time
from random import randint
import signal

def sigint_handler(sig, stack):
        run = False
        print('Shutting down...')

signal.signal(signal.SIGINT, sigint_handler)


p2p_svr_addr = ('0.0.0.0', 10101)
p2p_cli_addr = ('localhost', 10101)
run = True

class Server:
    conns = list()
    peers = list()

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(p2p_svr_addr)
        sock.listen(1)
        print("Server running")

        while run:
            conn, ip = sock.accept()
            serv_th = threading.Thread(target=self.handler, args=(conn, ip))
            serv_th.daemon = True
            serv_th.start()
            self.conns.append(c)
            self.peers.append(ip[0])
            print(ip[0], ':', ip[1], ' connected')
            self.sendPeers()

    def handler(self, conn, ip):
        while run:
            data = conn.recv(1024)
            for connection in self.conns:
                connection.send(data)
            if not data:
                print(ip[0], ':', ip[1], ' disconnected')
                self.conns.remove(ip)
                self.peers.remove(ip[0])
                conn.close()
                self.sendPeers()
                break
    
    def sendPeers(self):
        peers_string = ''
        for peer in self.peers:
            peers_string += peer + ','
        for connection in self.conns:
            connection.send(b'\x11' + bytes(peers_string, 'utf-8'))

class Client:

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(p2p_cli_addr)

        cli_th = threading.Thread(target=self.sendMsg, args=(sock,))
        cli_th.daemon = True
        cli_th.start()

        while run:
            data = sock.recv(1024)
            if not data:
                break
            if data[0:1] == b'\x11':
                self.update_peers(data[1:])
            else:
                print(str(data, 'utf-8'))

    def send_msg(self, sock):
        while run:
            sock.send(bytes(input(''), 'utf-8'))

    def update_peers(self, peerData):
        p2p.peers = str(peerData, 'utf-8').split(',')[:-1]

class p2p:
    peers = ['127.0.0.1']

# if(len(sys.argv) > 1):
#     client = Client()
# else:
#     server = Server()

while run:
    try:
        print('Trying to connect')
        time.sleep(randint(1,10))

        for peer in p2p.peers:
            try:
                client = Client(peer)
            except:
                pass
            
            try:
                server = Server()
            except:
                print('No server found')

    except:
        sys.exit(0)