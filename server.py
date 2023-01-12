import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()

client,addr=server.accept()

total_db={}
managerial_db={}
managers={'111','222','333'}

done=False

while not done:
    msg=client.recv(2048).decode('utf-8')
    list_of_msg=msg.split(" ")

    #parts of msg
    recv_id=list_of_msg[0]
    request_type=list_of_msg[1]
    
    
    if list_of_msg[0] =='quit':
        done=True
    elif request_type=='put':
        key_send=list_of_msg[2]
        value_sent=list_of_msg[3]
        #implementing put req
        
            
        managerial_db[key_send]=value_sent
        if recv_id in total_db:
            total_db[recv_id][key_send] = value_sent
        else:
            total_db[recv_id]={}
            total_db[recv_id][key_send] = value_sent
        print(total_db)
    elif request_type=='get':
        key_send=list_of_msg[2]
        if recv_id in managers:
            print(managerial_db[key_send])
        elif recv_id in total_db:
            
            print(total_db[recv_id][key_send])




    client.send(input("Enter 'next' to continue : ").encode('utf-8'))

