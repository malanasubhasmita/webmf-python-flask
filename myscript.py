print("this line is printed")
ip = '192.168.12.42'
sock = socket.socket()
sock.bind((ip, 9090))
