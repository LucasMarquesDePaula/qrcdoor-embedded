'''
Created on 12 de set de 2017

@author: Lucas
'''
from qrc_scanner import QRCScanner
from connection.ws_client import WSThread

class LoopScanner(QRCScanner):
    def on_error(self, error):
        QRCScanner.on_stop(self)
        self.run()

class WS(WSThread):
    def __init__(self):
        WSThread.__init__(self)

    def send_qrcode(self, ls, qrcode, ws):
        print('INFO: Sending QR code: {0}'.format(qrcode))
        ws.send(qrcode)

    def on_open(self, ws):
        WSThread.on_open(self, ws)
        ls = LoopScanner()
        ls.on_scan = lambda qrcode: self.send_qrcode(ls, qrcode, ws)
        ls.daemon = True
        ls.start()

    def on_message(self, ws, message):
        print('INFO: A message has been received: {0}'.format(message))

ws = WS()
ws.daemon = True
ws.start()
ws.join()

