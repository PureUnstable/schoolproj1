# import socket

# client_list = list()

# serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv.bind(('localhost', 8888))
# serv.listen(5)
# while True:
#     conn, addr = serv.accept()
#     from_client = ''
#     while True:
#         data = conn.recv(1024)
#         if not data: break
#         from_client += data
#         print from_client
#         conn.send("I am SERVER\n")
#     conn.close()
#     print 'client disconnected'

