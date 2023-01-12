import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",9999))

done= False

while not done:
    client.send(input("Enter command : ").encode('utf-8'))
    msg=client.recv(2048).decode('utf-8')
    if msg=='quit':
        done=True
    else:
        print("..........................")
    

