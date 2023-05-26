import socket
import sys
import os 

connection_file = 'connection_list.txt'

try: 


    def create_file() -> None:
        with open (connection_file,'w') as new_file:
            pass

    def host_is_new(client_data) -> bool:
        with open (connection_file, 'r') as file:
            file = file.read()
            if client_data not in file:
                return True
        return False


    def add_new_connection(client_data: str) -> None:
        global connection_file

        if not os.path.exists(connection_file):
                print(f'{connection_file} was created!')
                create_file()

        if host_is_new(client_data):
            print(f'New clietn from {client_data} was added in list!')
            with open(connection_file,'a') as f:
                f.write(client_data + '\n')

        else:
            print(f'Client from {client_data} is know!')
            


    def await_conenction(server_socket) -> str:
        while True:

            print('Await')
            conn, address = server_socket.accept()
            add_new_connection(address[0])
            print('New Connetion!')




    host = socket.gethostbyname(socket.gethostname())
    port = 5000

    server_socket = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM
    )
    server_socket.bind((host, port))
    server_socket.listen(2)
    await_conenction(server_socket)
    
except Exception as e:
    print(e)