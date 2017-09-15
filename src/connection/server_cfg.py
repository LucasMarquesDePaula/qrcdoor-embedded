'''
Created on 14 de set de 2017

@author: Lucas
'''

import json

file_name = 'server.cfg.json'


def read():
    global file_name
    with open(file_name, 'r', encoding='utf8') as file:
        return file.readline()


def data():
    return json.loads(read())


def write(data):
    with open(file_name, 'w', encoding='utf8') as file:
        json.dump(data, file)
    return data


def login():
    obj = data()
    return 'http://{0}/{1}'.format(obj['server-location'], obj['login-path'])


def ws():
    obj = data()
    return 'ws://{0}/{1}/websocket'.format(obj['server-location'], obj['websocket-path'])


def home():
    obj = data()
    return 'http://{0}'.format(obj['server-location'])


def cli():
    print('INFO: Iniciando configuracao do servidor')
    try: 
        print('INFO: Configuracoes atuais:')
        print(read())
    except IOError as e:
        print('ERRO: As configuracoes atuais nao puderam ser lidas')

    try:
        server = input('INPUT: Digite a localizacao do Servidor: ')
        ws = input('INPUT: Digite o caminho para o WebSocket: ')
        login = input('INPUT: Digite o caminho para o Login: ')
        write({ 'server-location': server, 'login-path': login, 'websocket-path': ws })
        
    except IOError as e:
        print('ERRO: Erro ao configurar, tente novamente')
        print('ERRO: I/O error({0}): {1}'.format(e.errno, e.strerror))
        
    except Exception as e:
        print('ERRO: Erro ao configurar, tente novamente')
        print(e)
        
    finally:
        print('INFO: Fim da configuracao')
        
if __name__ == '__main__':
    cli()