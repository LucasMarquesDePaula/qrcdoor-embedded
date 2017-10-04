'''
Created on 12 de set de 2017

@author: Lucas
'''
from qrc_scanner import QRCScanner
from connection.ws_client import WSThread

class LoopScanner(QRCScanner):       
    def on_stop(self):
        QRCScanner.on_stop(self)
        self.run()
    
class WS(WSThread):
    def __init__(self):
        WSThread.__init__(self)

    def on_open(self, ws):
        WSThread.on_open(self, ws)
        ls = LoopScanner()
        ls.on_scan = lambda qrcode: ws.send(qrcode)

    def on_message(self, ws, message):
        WSThread.on_message(self, ws, message) 
            
ws = WS()
ws.daemon = True
ws.run()


