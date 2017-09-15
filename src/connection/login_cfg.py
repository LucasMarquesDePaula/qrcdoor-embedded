'''
Created on 14 de set de 2017

@author: Lucas
'''

import json

file_name = 'login.cfg.json'

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

def cli():
    print('INFO: Iniciando configuracao de login')
    try: 
        print('INFO: Configuracoes atuais:')
        print(read())
    except IOError as e:
        print('ERRO: As configuracoes atuais nao puderam ser lidas')

    try:
        usr = input('INPUT: Digite o usuario: ')
        pwd = input('INPUT: Digite a senha: ')
        write({ 'username': usr, 'password': pwd })
        
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
    
        