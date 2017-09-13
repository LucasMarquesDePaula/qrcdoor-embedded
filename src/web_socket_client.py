'''
Created on 12 de set de 2017

@author: Lucas
'''
import websocket
import thread
import time
import requests

class Obj(dict):
    def __getattr__(self, name):
        return self[name]

def on_message(ws, message):
    print "### message ###"
    print message

def on_error(ws, error):
    print "### error ###"
    print error

def on_close(ws):
    print "### close ###"

def on_open(ws):
    print "### open ###"
    def run(*args):
        for i in range(3):
            time.sleep(1)
            ws.send('Test %d' % i)
#             ws.send("Hello %d" % i)
        time.sleep(1)
#         ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    
    # Create session
    session = requests.Session()
    session.cookies.get_dict()
    response = session.post('http://localhost:8070/login', Obj(username='user1', password='user1'))

#     websocket.enableTrace(True)
    ws = websocket.WebSocketApp('ws://localhost:8070/open/websocket',
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close,
                              cookie='SESSION=%s' % session.cookies.get_dict()['SESSION'])
    ws.on_open = on_open
    ws.run_forever()

