import socket
import os.path
import sys

from rich.console import Console
import dearpygui.dearpygui as dpg
import pyperclip

console = Console(highlight=False)

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
    server_status = 'The server is not working!'
    console.print('[red]The server is not working![red]')



def copy_your_token():
    pyperclip.copy(f'{your_host} {your_port}')
    dpg.set_value('copied', 'Token is copied!')

dpg.create_context()
with dpg.window( tag = 'Primary Window'):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="    Messeger    "):
            i_tems=['1 friend', '2 friend', '3 friend', '4 friend']
            dpg.add_listbox(items=i_tems)
        with dpg.menu(label = '    Account    '):
            dpg.add_text('', tag = 'host')
            dpg.set_value('host', your_host) 

            dpg.add_text('', tag = 'port')
            dpg.set_value('port', your_port)  

            # dpg.add_text('', tag = 'your_token')
            # dpg.set_value('your_token',f'{your_host} {your_port}' )

            dpg.add_button(label = 'Copy your account token', callback = copy_your_token)
            dpg.add_text('', tag = 'copied')
        
        with dpg.menu(label = '     Setting     '):
            dpg.add_text('', tag = 'server_status')
            dpg.set_value('server_status', server_status)
            

dpg.create_viewport(title='SoMess', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()