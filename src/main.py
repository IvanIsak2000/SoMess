import socket
import os.path
import sys

import dearpygui.dearpygui as dpg

try:
    from config import HOST, PORT

except ModuleNotFoundError:
    server_host = input('Добро пожаловтаь в SoMess!\nВведите host к которому необходимо подключиться: ')
    server_port = input('Введите port: ')
    config_data = f"HOST = '{server_host}'\nPORT = {server_port}"

    with open ('config.py', 'w') as file:

        file.write(config_data)
        print('config was created!') 

    from config import HOST, PORT


def connection_to_server(server_socket) -> None:
    pass
    


your_host = socket.gethostbyname(socket.gethostname())
your_port = 5000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((HOST, PORT))
    server_status = 'OK'
 
except ConnectionRefusedError:
    server_status = 'Error'
    print('сервер не работает!')

dpg.create_context()
with dpg.window( tag = 'Primary Window'):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="    Messeger    "):
            pass
        with dpg.menu(label = '    Account    '):
            dpg.add_text('', tag = 'host')
            dpg.set_value('host', your_host) 

            dpg.add_text('', tag = 'port')
            dpg.set_value('port', your_port)  
        
        with dpg.menu(label = '     Setting     '):
            dpg.add_text('', tag = 'server_status')
            dpg.set_value('server_status', server_status)
            

dpg.create_viewport(title='Custom Title', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()