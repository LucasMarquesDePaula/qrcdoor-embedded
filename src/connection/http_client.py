'''
Created on 14 de set de 2017

@author: Lucas
'''

from connection import login_cfg, server_cfg
#import login_cfg, server_cfg

def login():
    print('INFO: Creating session')
    import requests
    # Create session
    session = requests.Session()
    url = server_cfg.login()
    data = login_cfg.data()

    print('INFO: URL: "{0}"'.format(url))
    print('INFO: PAYLOAD: "{0}"'.format(data))
    print('INFO: Sending data to server')

    response = session.post(url, data)
    print('INFO: Server\'s response')
    print('INFO: URL: "{0}"'.format(url))
    print('INFO: RESPONSE: "{0}"'.format(response))

    url = server_cfg.home()
    response = session.post(url)
    print('INFO: Cheking session')

    print('INFO: URL: "{0}"'.format(url))
    print('INFO: RESPONSE: "{0}"'.format(response))

    if(response.status_code == 200):
        print('INFO: Session valid')
    else:
        print('INFO: Sessao unvalid')
        raise Exception('Invalid status code', 'Expected: 200, Received: {0}'.format(response.status_code))

    cookies = session.cookies.get_dict()
    print('INFO: COOKIES: "{0}"'.format(cookies))

    return cookies

if __name__ == '__main__':
    print(login())
