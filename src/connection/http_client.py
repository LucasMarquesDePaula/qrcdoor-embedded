'''
Created on 14 de set de 2017

@author: Lucas
'''

import login_cfg, server_cfg

def login():
    print('INFO: Criando sessao com o servidor')
    import requests
    # Create session
    session = requests.Session()
    url = server_cfg.login()
    data = login_cfg.data()

    print('INFO: URL: "{0}"'.format(url))
    print('INFO: PAYLOAD: "{0}"'.format(data))
    print('INFO: Enviando dados ao servidor')
    
    response = session.post(url, data)
    print('INFO: Resposta do servidor')
    print('INFO: URL: "{0}"'.format(url))
    print('INFO: RESPONSE: "{0}"'.format(response))

    url = server_cfg.home()
    response = session.post(url)
    print('INFO: Validando a sessao')
     
    print('INFO: URL: "{0}"'.format(url))
    print('INFO: RESPONSE: "{0}"'.format(response))
     
    if(response.status_code == 200):
        print('INFO: Sessao validada')
    else:
        print('INFO: Sessao invalida')
        raise Exception('Invalid status code', 'Expected: 200, Received: {0}'.format(response.status_code))
     
    cookies = session.cookies.get_dict()
    print('INFO: COOKIES: "{0}"'.format(cookies))

    return cookies
    
if __name__ == '__main__':
    print(login())
