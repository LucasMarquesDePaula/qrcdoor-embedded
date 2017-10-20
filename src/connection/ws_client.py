'''
Created on 12 de set de 2017

@author: Lucas
'''
from threading import Thread
import websocket

class WSThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        from connection import http_client, server_cfg
#        import http_client, server_cfg

        print('INFO: Connecting to server by websocket')
        url = server_cfg.ws()
        cookies = http_client.login()
        cookie = 'SESSION={0}'.format(cookies['SESSION'])

        print('INFO: URL: "{0}"'.format(url))
        print('INFO: COOKIE: "{0}"'.format(cookie))

        ws = websocket.WebSocketApp(url,
                                  on_message=self.on_message,
                                  on_error=self.on_error,
                                  on_close=self.on_close,
                                  cookie=cookie)

        ws.on_open = self.on_open
        ws.run_forever()

        return ws

    def on_message(self, ws, message):
        print('INFO: WS message has been received')
        print(message)

    def on_error(self, ws, error):
        print('ERROR: WS error occurred')
        print(error)

    def on_close(self, ws):
        print('INFO: WS connection has been closed')

    def on_open(self, ws):
        print('INFO: WS connection has been opened')  

if __name__ == '__main__':  

    class WS(WSThread):
        def __init__(self):
            WSThread.__init__(self)

        def on_open(self, ws):
            import time
            WSThread.on_open(self, ws)
            for i in range(3):
                time.sleep(1)
                ws.send('Test {0}'.format(i))
            time.sleep(1)


        def on_message(self, ws, message):
            WSThread.on_message(self, ws, message) 
            if ('Hello, Test 2!' == message):
                ws.close()

    ws = WS()
    ws.daemon = True
    ws.run()

